#!/usr/bin/env python3
from itertools import combinations, product

# Integer masses on {0,1} x {0,1} x {0,1,2}; omitted cells have mass 0.
W = {
    (0,0,2):14,
    (0,1,0):18,
    (0,1,1):3,
    (1,0,0):17,
    (1,0,1):5,
    (1,1,0):27,
    (1,1,1):2,
}
DOM = [range(2), range(2), range(3)]
PTS = list(product(*DOM))
TOTAL = sum(W.values())


def leq(a,b):
    return all(x <= y for x,y in zip(a,b))


def nontrivial_upper_sets(indices):
    vals = list(product(*[DOM[i] for i in indices]))
    out = []
    for mask in range(1, (1 << len(vals)) - 1):
        U = {vals[k] for k in range(len(vals)) if mask >> k & 1}
        ok = True
        for x in U:
            for y in vals:
                if leq(x,y) and y not in U:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            out.append(U)
    return out


def project(x, inds):
    return tuple(x[i] for i in inds)


def marginal_mass(J, y):
    return sum(W.get(x,0) for x in PTS if project(x,J) == y)


def event_mass(I, U, J, y):
    return sum(W.get(x,0) for x in PTS
               if project(x,J) == y and project(x,I) in U)


def comparable_pairs(J):
    vals = list(product(*[DOM[j] for j in J]))
    return [(a,b) for a in vals for b in vals if a != b and leq(a,b)]

formal = applicable = strict = equal = 0
min_positive = None
by_block = []
for rI in (1,2):
    for I in combinations(range(3), rI):
        remaining = [j for j in range(3) if j not in I]
        for rJ in range(1, len(remaining)+1):
            for J in combinations(remaining, rJ):
                local_app = local_strict = local_eq = 0
                local_min = None
                uppers = nontrivial_upper_sets(I)
                for y,y2 in comparable_pairs(J):
                    for U in uppers:
                        formal += 1
                        d1 = marginal_mass(J,y)
                        d2 = marginal_mass(J,y2)
                        if d1 == 0 or d2 == 0:
                            continue
                        applicable += 1
                        local_app += 1
                        n1 = event_mass(I,U,J,y)
                        n2 = event_mass(I,U,J,y2)
                        slack = n1*d2 - n2*d1
                        assert slack >= 0, (I,J,y,y2,U,slack)
                        if slack == 0:
                            equal += 1
                            local_eq += 1
                        else:
                            strict += 1
                            local_strict += 1
                            min_positive = slack if min_positive is None else min(min_positive,slack)
                            local_min = slack if local_min is None else min(local_min,slack)
                if local_app:
                    by_block.append((I,J,local_app,local_min,local_strict,local_eq))

assert TOTAL == 86
assert len(W) == 7
assert formal == 74
assert applicable == 64
assert strict == 57
assert equal == 7
assert min_positive == 6

# Right-tail failure: condition first on X3 >= 1 and then on X2=1, X3>=1.
den_lo = sum(w for x,w in W.items() if x[2] >= 1)
num_lo = sum(w for x,w in W.items() if x[2] >= 1 and x[0] == 1)
den_hi = sum(w for x,w in W.items() if x[1] == 1 and x[2] >= 1)
num_hi = sum(w for x,w in W.items() if x[1] == 1 and x[2] >= 1 and x[0] == 1)
assert (num_lo, den_lo, num_hi, den_hi) == (7,24,2,5)
assert num_lo * den_hi < num_hi * den_lo
assert num_lo * den_hi - num_hi * den_lo == -13

print(f'total_mass={TOTAL}')
print(f'support_size={len(W)}')
print(f'formal_nrd_comparisons={formal}')
print(f'applicable_nrd_comparisons={applicable}')
print(f'nrd_strict={strict}')
print(f'nrd_equalities={equal}')
print(f'min_positive_integer_slack={min_positive}')
for I,J,c,mn,s,e in by_block:
    print(f'I={I} J={J} count={c} min_positive={mn} strict={s} equal={e}')
print(f'nrtd_low={num_lo}/{den_lo}')
print(f'nrtd_high={num_hi}/{den_hi}')
print(f'nrtd_cross_slack={num_lo*den_hi-num_hi*den_lo}')
print('VERIFY_OK')
