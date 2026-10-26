"""Independent finite-instance verification for state-minimal reversal witnesses.
Uses graph-edge state encoding and explicit automata minimization, without
relying on the proof's incidence lower bound.
"""
from itertools import combinations, permutations
from collections import deque
from math import comb


def minimization_classes(transitions, final):
    """Moore refinement, over complete reachable DFA states."""
    n=len(transitions)
    cls=[int(i in final) for i in range(n)]
    while True:
        signatures=[(cls[i],)+(tuple(cls[j] for j in transitions[i])) for i in range(n)]
        index={v:k for k,v in enumerate(sorted(set(signatures)))}
        new=[index[v] for v in signatures]
        if len(set(new))==len(set(cls)) and all((cls[i]==cls[j])==(new[i]==new[j]) for i in range(n) for j in range(n)):
            return len(set(new))
        cls=new


def star_edge_automaton(m):
    v=m+1
    Q=list(combinations(range(v),2))
    pos={e:i for i,e in enumerate(Q)}
    pi_cycle=lambda x:(x+1)%v
    pi_swap=lambda x:(1-x if x<=1 else x)
    perms=(pi_cycle,pi_swap)
    transitions=[tuple(pos[tuple(sorted((p(x),p(y))))] for p in perms) for x,y in Q]
    start=pos[(0,1)]
    finals={pos[e] for e in Q if 0 in e}
    return Q,transitions,start,finals


def reversed_subset_dfa(transitions,start,finals):
    k=len(transitions[0]); n=len(transitions)
    initial=frozenset(finals)
    reached=[initial]; num={initial:0}; todo=deque([initial]); out=[]
    while todo:
        S=todo.popleft()
        r=[]
        for a in range(k):
            T=frozenset(i for i in range(n) if transitions[i][a] in S)
            if T not in num:
                num[T]=len(reached);reached.append(T);todo.append(T)
            r.append(num[T])
        out.append(tuple(r))
    final_r={i for i,S in enumerate(reached) if start in S}
    return reached,out,final_r


def reachable_count(transitions,start):
    got={start}; todo=[start]
    for q in todo:
        for r in transitions[q]:
            if r not in got:got.add(r);todo.append(r)
    return len(got)


def test_family():
    for m in range(2,13):
        Q,transitions,start,finals=star_edge_automaton(m)
        assert reachable_count(transitions,start)==comb(m+1,2)
        assert len(finals)==m
        assert minimization_classes(transitions,finals)==len(Q)
        states,rtrans,rfinals=reversed_subset_dfa(transitions,start,finals)
        assert len(states)==m+1
        assert len(rfinals)==2
        assert minimization_classes(rtrans,rfinals)==len(states)
        assert {frozenset(Q[e] for e in S) for S in states}=={frozenset(e for e in Q if vertex in e) for vertex in range(m+1)}
        print(f'm={m} forward_states={len(Q)} reverse_states={len(states)} reverse_final={len(rfinals)} OK')


def exhaustive_small_lower_bound():
    # Binary complete permutation DFAs, initial state fixed at 0.
    # Exhaust all ordered pairs of permutation transitions and all final sets.
    # Count only automata with minimal forward DFA and exactly m final states.
    # Reverse acceptance always computed by subset orbit, not by direct formula.
    for m in (2,3):
        count=0; good=0; max_n=comb(m+1,2)-1
        for n in range(m,max_n+1):
            perms=list(permutations(range(n)))
            for p in perms:
                for q in perms:
                    trans=[(p[i],q[i]) for i in range(n)]
                    if reachable_count(trans,0)!=n:continue
                    for F in combinations(range(n),m):
                        count+=1
                        if minimization_classes(trans,set(F))!=n:continue
                        got,rtrans,rF=reversed_subset_dfa(trans,0,set(F))
                        if minimization_classes(rtrans,rF)!=len(got):raise AssertionError('reverse should be minimal for transitive PFA')
                        assert len(rF)!=2, f'counterexample with m={m},n={n},p={p},q={q},F={F}'
                        good+=1
        print(f'exhaustive_lower_m={m} smaller_minimal_forward_DFAs={good}, candidate_instances={count}, reverse_final_2=0')

if __name__=='__main__':
    test_family()
    exhaustive_small_lower_bound()
    print('VERIFY_OK')
