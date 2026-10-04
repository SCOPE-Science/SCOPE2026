#!/usr/bin/env python3
from itertools import permutations, product, combinations
from collections import Counter, defaultdict
from fractions import Fraction
import hashlib

AGENTS = (0,1,2)
HOUSES = (0,1,2)
RANKINGS = list(permutations(HOUSES))
ORDERS = list(permutations(AGENTS))
MATCHINGS = list(permutations(HOUSES))  # matching[i] = house of agent i


def serial_dictatorship(profile, order):
    available = set(HOUSES)
    out = [None]*3
    for i in order:
        for h in profile[i]:
            if h in available:
                out[i] = h
                available.remove(h)
                break
    return tuple(out)


def serial_dictatorship_recursive(profile, order):
    out = [None]*3
    used = ()
    for k,i in enumerate(order):
        forbidden = set(used)
        h = min((h for h in HOUSES if h not in forbidden), key=lambda x: profile[i].index(x))
        out[i] = h
        used = used + (h,)
    return tuple(out)


def ttc(profile, endowment):
    # endowment[i] is the house initially owned by agent i
    owner = {h:i for i,h in enumerate(endowment)}
    active = set(AGENTS)
    out = [None]*3
    while active:
        available = set(owner)
        top = {i: next(h for h in profile[i] if h in available) for i in active}
        f = {i: owner[top[i]] for i in active}
        cycle_agents = set()
        for start in sorted(active):
            path=[]; pos={}; x=start
            while x not in pos:
                pos[x]=len(path); path.append(x); x=f[x]
            cycle_agents.update(path[pos[x]:])
        removed=[]
        for i in cycle_agents:
            h=top[i]
            out[i]=h
            removed.append((i,h))
        for i,h in removed:
            active.remove(i)
            owner.pop(h)
    return tuple(out)


def prefers(profile, i, h1, h2):
    return profile[i].index(h1) < profile[i].index(h2)


def core_by_blocking(profile, endowment):
    core=[]
    for m in MATCHINGS:
        blocked=False
        for r in (1,2,3):
            for coalition in combinations(AGENTS,r):
                endowed = [endowment[i] for i in coalition]
                for reassignment in permutations(endowed):
                    weak_all=True
                    strict_any=False
                    for i,h in zip(coalition,reassignment):
                        if h == m[i]:
                            continue
                        if prefers(profile,i,h,m[i]):
                            strict_any=True
                        else:
                            weak_all=False
                            break
                    if weak_all and strict_any:
                        blocked=True
                        break
                if blocked: break
            if blocked: break
        if not blocked:
            core.append(m)
    assert len(core)==1, (profile,endowment,core)
    return core[0]


def structure_cell(profile):
    tops=[p[0] for p in profile]
    counts=sorted(Counter(tops).values(), reverse=True)
    distinct=len(set(profile))
    if counts == [1,1,1]:
        return 'distinct_tops'
    if counts == [3]:
        if distinct == 1:
            return 'common_top_one_order'
        assert distinct == 2
        return 'common_top_two_orders'
    assert counts == [2,1]
    if distinct == 3:
        return 'two_one_tops_three_orders'
    assert distinct == 2
    duplicated = Counter(profile).most_common(1)[0][0]
    singleton = next(p for p in profile if p != duplicated)
    assert duplicated[0] != singleton[0]
    if singleton[0] == duplicated[1]:
        return 'two_one_tops_two_orders_singleton_on_second'
    assert singleton[0] == duplicated[2]
    return 'two_one_tops_two_orders_singleton_on_third'

EXPECTED_SPECTRUM = {
    'distinct_tops': (6,),
    'common_top_one_order': (1,1,1,1,1,1),
    'common_top_two_orders': (2,2,1,1),
    'two_one_tops_three_orders': (3,2,1),
    'two_one_tops_two_orders_singleton_on_second': (2,2,1,1),
    'two_one_tops_two_orders_singleton_on_third': (3,3),
}
EXPECTED_CELLS = Counter({
    'distinct_tops':48,
    'common_top_one_order':6,
    'common_top_two_orders':18,
    'two_one_tops_three_orders':72,
    'two_one_tops_two_orders_singleton_on_second':36,
    'two_one_tops_two_orders_singleton_on_third':36,
})
EXPECTED_SPECTRA = Counter({
    (6,):48,
    (3,3):36,
    (3,2,1):72,
    (2,2,1,1):54,
    (1,1,1,1,1,1):6,
})

cells=Counter(); spectra=Counter(); support=Counter(); digest_lines=[]
for profile in product(RANKINGS, repeat=3):
    rsd = Counter()
    for order in ORDERS:
        a=serial_dictatorship(profile,order)
        b=serial_dictatorship_recursive(profile,order)
        assert a==b
        rsd[a]+=1
    cre = Counter()
    for endowment in MATCHINGS:
        a=ttc(profile,endowment)
        b=core_by_blocking(profile,endowment)
        assert a==b
        cre[a]+=1
    assert rsd == cre
    spec=tuple(sorted(rsd.values(), reverse=True))
    cell=structure_cell(profile)
    assert spec == EXPECTED_SPECTRUM[cell]
    cells[cell]+=1
    spectra[spec]+=1
    support[len(rsd)]+=1
    digest_lines.append(repr((profile,sorted(rsd.items()),cell)))

assert cells == EXPECTED_CELLS
assert spectra == EXPECTED_SPECTRA
assert support == Counter({1:48,2:36,3:72,4:54,6:6})
assert 5 not in support
mean_support = Fraction(sum(k*v for k,v in support.items()),216)
assert mean_support == Fraction(49,18)

sha=hashlib.sha256('\n'.join(digest_lines).encode('utf-8')).hexdigest()
print('VERIFY_OK')
print('profiles',216)
print('cells',dict(cells))
print('spectra',{str(k):v for k,v in spectra.items()})
print('support',dict(sorted(support.items())))
print('mean_support',str(mean_support))
print('no_support_5',True)
print('rsd_cre_equal_all_profiles',True)
print('digest_sha256',sha)
