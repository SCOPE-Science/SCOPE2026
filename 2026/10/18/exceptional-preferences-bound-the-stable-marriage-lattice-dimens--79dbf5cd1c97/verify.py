#!/usr/bin/env python3
"""Exact, finite sanity checks for master-list-deviation stable matching results.
The infinite assertions in the accompanying note are proved mathematically,
not by these enumerations.
"""
from itertools import permutations, product
from collections import Counter
import json


def ranks(order):
    return [{v:i for i,v in enumerate(row)} for row in order]


def stable(men, women, matching):
    n = len(men)
    assert len(matching) == n and sorted(matching) == list(range(n))
    rm, rw = ranks(men), ranks(women)
    reverse = [0]*n
    for m,w in enumerate(matching):
        reverse[w] = m
    for m in range(n):
        for w in range(n):
            if rm[m][w]<rm[m][matching[m]] and rw[w][m]<rw[w][reverse[w]]:
                return False
    return True


def exhaustive(men,women):
    return [p for p in permutations(range(len(men))) if stable(men,women,p)]


def conditional(men,women, exceptions):
    n = len(men)
    master = women[next(w for w in range(n) if w not in exceptions)] if len(exceptions)<n else None
    possible=[]
    for agents in permutations(range(n),len(exceptions)):
        assign={w:m for w,m in zip(exceptions,agents)}
        remaining_m = [m for m in master if m not in agents] if master is not None else []
        remaining_w=set(range(n))-set(exceptions)
        matching=[-1]*n
        for w,m in assign.items():matching[m]=w
        for m in remaining_m:
            selected = next(w for w in men[m] if w in remaining_w)
            matching[m]=selected
            remaining_w.remove(selected)
        if stable(men,women,tuple(matching)):
            possible.append(tuple(matching))
    return sorted(possible)


def witness_chain(n):
    men=[]
    for i in range(n):
        if i==0:
            men.append(tuple(range(n)))
        else:
            men.append(tuple(list(range(1,i+1))+[0]+list(range(i+1,n))))
    women=[tuple(reversed(range(n)))]+[tuple(range(n)) for _ in range(1,n)]
    expected=[]
    for k in range(n):
        p=[None]*n
        for m in range(n):p[m] = m+1 if m<k else (0 if m==k else m)
        expected.append(tuple(p))
    return men,women,expected


def witness_boolean(k):
    n=2*k
    # In block i, men (2i,2i+1), women (2i,2i+1): even women exceptional.
    men=[]
    women=[]
    for i in range(k):
        a,b=2*i,2*i+1
        rest = [w for w in range(n) if w not in (a,b)]
        men.extend([(a,b,*rest),(b,a,*rest)])
        remaining_m = [m for m in range(n) if m not in (a,b)]
        women.extend([(b,a,*remaining_m),tuple(range(n))])
    expected=[]
    for bits in product((0,1),repeat=k):
        mt=[None]*n
        for i,bit in enumerate(bits):
            a=2*i
            mt[a],mt[a+1]=(a+bit,a+1-bit)
        expected.append(tuple(mt))
    return men,women,sorted(expected)


def check_chain_order(men,women,sol,exceptions):
    rankw = ranks(women)
    n=len(men)
    def exceptional_vec(p):
        inv=[None]*n
        for m,w in enumerate(p):inv[w]=m
        return tuple(-rankw[w][inv[w]] for w in exceptions)
    vec={p:exceptional_vec(p) for p in sol}
    assert len(set(vec.values()))==len(sol)
    # Coordinate order agrees with the full female dominance order.
    for p in sol:
        for q in sol:
            pv,qv=vec[p],vec[q]
            coord=all(a<=b for a,b in zip(pv,qv))
            pinv=[None]*n; qinv=[None]*n
            for m,w in enumerate(p):pinv[w]=m
            for m,w in enumerate(q):qinv[w]=m
            full=all(rankw[w][pinv[w]]>=rankw[w][qinv[w]] for w in range(n))
            assert coord==full


def main():
    stats={}
    for n in range(1,7):
        men,women,expected=witness_chain(n)
        actual=sorted(exhaustive(men,women))
        assert actual==sorted(expected),(n,actual,expected)
        assert actual==conditional(men,women,(0,))
        check_chain_order(men,women,actual,(0,))
    stats['sharp_chain_verified_n']=list(range(1,7))
    for k in range(1,4):
        men,women,expected=witness_boolean(k)
        actual=sorted(exhaustive(men,women))
        assert actual==expected,(k,actual,expected)
        assert actual==conditional(men,women,tuple(range(0,2*k,2)))
        check_chain_order(men,women,actual,tuple(range(0,2*k,2)))
    stats['boolean_lattice_verified_k']=[1,2,3]
    for n in (2,3):
        ps=list(permutations(range(n)))
        hist=Counter(); instances=0
        for dev in ps:
            women=[dev]+[tuple(range(n)) for _ in range(1,n)]
            for men in product(ps,repeat=n):
                truth=sorted(exhaustive(men,women))
                derived=conditional(men,women,(0,))
                assert truth==derived
                check_chain_order(men,women,truth,(0,))
                assert len(truth)<=n
                hist[len(truth)]+=1;instances+=1
        stats[f'all_one_deviation_n{n}']={'instances':instances,'stable_count_histogram':dict(sorted(hist.items()))}
    print(json.dumps(stats,sort_keys=True,indent=2))

if __name__=='__main__':main()
