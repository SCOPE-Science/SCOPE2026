#!/usr/bin/env python3
from itertools import permutations, product
from collections import Counter
from fractions import Fraction
import hashlib

AGENTS = (0,1,2)
RANKINGS = list(permutations(AGENTS))


def ttc_functional(profile):
    """TTC by agent-to-current-owner functional graph; all cycles per round."""
    remaining_agents = set(AGENTS)
    remaining_houses = set(AGENTS)
    owner = {h:h for h in AGENTS}
    alloc = [None]*3
    trace = []
    while remaining_agents:
        top_house = {}
        next_agent = {}
        for i in remaining_agents:
            h = next(h for h in profile[i] if h in remaining_houses)
            top_house[i] = h
            next_agent[i] = owner[h]
        # Every finite functional digraph has cycles. Extract all cyclic vertices.
        cyc_sets = set()
        seen_global = set()
        for start in sorted(remaining_agents):
            if start in seen_global:
                continue
            order = []
            pos = {}
            v = start
            while v not in pos and v not in seen_global:
                pos[v] = len(order)
                order.append(v)
                v = next_agent[v]
            seen_global.update(order)
            if v in pos:
                cyc = tuple(sorted(order[pos[v]:]))
                cyc_sets.add(cyc)
        cycle_agents = sorted(set().union(*map(set,cyc_sets)))
        assert cycle_agents
        lengths = sorted(len(c) for c in cyc_sets)
        trace.append(tuple(lengths))
        for i in cycle_agents:
            alloc[i] = top_house[i]
        for i in cycle_agents:
            remaining_houses.remove(alloc[i])
            remaining_agents.remove(i)
    return tuple(alloc), tuple(trace)


def ttc_bipartite(profile):
    """Independent explicit 6-node agent/house graph replay."""
    remaining_agents = set(AGENTS)
    remaining_houses = set(AGENTS)
    owner = {h:h for h in AGENTS}
    alloc = [None]*3
    trace = []
    while remaining_agents:
        # nodes: ('a',i), ('h',h)
        nxt = {}
        top = {}
        for i in remaining_agents:
            h = next(h for h in profile[i] if h in remaining_houses)
            top[i] = h
            nxt[('a',i)] = ('h',h)
        for h in remaining_houses:
            nxt[('h',h)] = ('a',owner[h])
        nodes = sorted(nxt)
        cycle_node_sets = []
        used_cycles = set()
        for start in nodes:
            order=[]; pos={}; v=start
            while v not in pos:
                pos[v]=len(order); order.append(v); v=nxt[v]
            cyc_nodes = order[pos[v]:]
            key = frozenset(cyc_nodes)
            if key not in used_cycles:
                used_cycles.add(key)
                cycle_node_sets.append(cyc_nodes)
        # In this graph all directed cycles alternate agent/house; cycles contain agents to execute.
        execute = []
        cycle_lengths=[]
        for cyc in cycle_node_sets:
            agents = sorted(x[1] for x in cyc if x[0]=='a')
            if not agents:
                continue
            # Only execute cycles fully contained in current graph (all are).
            execute.extend(agents)
            cycle_lengths.append(len(agents))
        execute = sorted(set(execute))
        # The graph may find same directed cycle from multiple starts; dedup via used_cycles above.
        assert execute
        trace.append(tuple(sorted(cycle_lengths)))
        for i in execute:
            alloc[i]=top[i]
        for i in execute:
            remaining_houses.remove(alloc[i])
            remaining_agents.remove(i)
    return tuple(alloc), tuple(trace)


def first_choice_map(profile):
    return tuple(pref[0] for pref in profile)


def first_round_type(f):
    loops = sum(i==f[i] for i in AGENTS)
    # 3-cycle iff no loops and f is a permutation of all three with no fixed point.
    is3 = loops==0 and len(set(f))==3
    twocycles = 0
    for i in AGENTS:
        for j in AGENTS:
            if i<j and f[i]==j and f[j]==i:
                twocycles += 1
    if loops==3: return '3loops'
    if loops==1 and twocycles==1: return 'loop+2cycle'
    if is3: return '3cycle'
    if loops==2: return '2loops+tail'
    if loops==0 and twocycles==1: return '2cycle+tail'
    if loops==1 and twocycles==0: return '1loop_no2cycle'
    raise AssertionError(f)

profiles = list(product(RANKINGS, repeat=3))
assert len(profiles)==216
trace_hist=Counter(); mover_hist=Counter(); rounds_hist=Counter(); first_hist=Counter(); rank_hist=Counter()
alloc_digest_rows=[]

for P in profiles:
    a1,t1 = ttc_functional(P)
    a2,t2 = ttc_bipartite(P)
    assert a1==a2 and t1==t2, (P,a1,t1,a2,t2)
    trace_hist[t1]+=1
    movers=sum(a1[i]!=i for i in AGENTS)
    mover_hist[movers]+=1
    rounds_hist[len(t1)]+=1
    first_hist[first_round_type(first_choice_map(P))]+=1
    ranks=tuple(P[i].index(a1[i])+1 for i in AGENTS)
    rank_hist[ranks]+=1
    alloc_digest_rows.append(repr((P,a1,t1)))

expected_trace = Counter({
    ((1,1),(1,)):48,
    ((2,),(1,)):48,
    ((1,),(1,),(1,)):36,
    ((1,),(2,)):30,
    ((1,2),):24,
    ((3,),):16,
    ((1,1,1),):8,
    ((1,),(1,1)):6,
})
assert trace_hist == expected_trace
assert mover_hist == Counter({2:102,0:98,3:16})
assert rounds_hist == Counter({2:132,1:48,3:36})
assert first_hist == Counter({
    '1loop_no2cycle':72,
    '2loops+tail':48,
    '2cycle+tail':48,
    'loop+2cycle':24,
    '3cycle':16,
    '3loops':8,
})

# Analytic split of the one-loop/no-two-cycle first-round maps.
sub=Counter()
for P in profiles:
    f=first_choice_map(P)
    if first_round_type(f)!='1loop_no2cycle':
        continue
    fixed=[i for i in AGENTS if f[i]==i]
    assert len(fixed)==1
    r=fixed[0]
    others=[i for i in AGENTS if i!=r]
    # Star: both outsiders point directly to fixed-point owner.
    if all(f[i]==r for i in others):
        kind='star'
    else:
        kind='chain'
    _,tr=ttc_functional(P)
    sub[(kind,tr)] += 1

assert sub == Counter({
    ('star',((1,),(1,),(1,))):12,
    ('star',((1,),(2,))):6,
    ('star',((1,),(1,1))):6,
    ('chain',((1,),(1,),(1,))):24,
    ('chain',((1,),(2,))):24,
})

assert Fraction(mover_hist[0],216)==Fraction(49,108)
assert Fraction(mover_hist[2],216)==Fraction(17,36)
assert Fraction(mover_hist[3],216)==Fraction(2,27)
assert Fraction(mover_hist[2]+mover_hist[3],216)==Fraction(59,108)
assert Fraction(sum(k*v for k,v in mover_hist.items()),216)==Fraction(7,6)
assert Fraction(rounds_hist[1],216)==Fraction(2,9)
assert Fraction(rounds_hist[2],216)==Fraction(11,18)
assert Fraction(rounds_hist[3],216)==Fraction(1,6)
assert Fraction(sum(k*v for k,v in rounds_hist.items()),216)==Fraction(35,18)

# Every first-choice map has exactly 2^3 full-ranking refinements.
fm=Counter(first_choice_map(P) for P in profiles)
assert len(fm)==27 and set(fm.values())=={8}

digest=hashlib.sha256('\n'.join(sorted(alloc_digest_rows)).encode('ascii')).hexdigest()
print('VERIFY_OK')
print('profiles',216)
print('trace_hist',dict(sorted(trace_hist.items(), key=lambda kv: repr(kv[0]))))
print('first_round_type_hist',dict(first_hist))
print('one_loop_split',dict(sub))
print('mover_hist',dict(mover_hist))
print('rounds_hist',dict(rounds_hist))
print('p_no_trade','49/108')
print('p_exactly_two_movers','17/36')
print('p_exactly_three_movers','2/27')
print('p_any_trade','59/108')
print('expected_movers','7/6')
print('expected_rounds','35/18')
print('replay_sha256',digest)
