#!/usr/bin/env python3
"""Standalone exact checks of Catalan triangulation inclusion inequalities.

Run: python check.py
Uses only Python's standard library. Checks are finite evidence, not the general proof.
"""
from functools import lru_cache
from itertools import combinations
from math import comb

@lru_cache(None)
def triangulations(i,j):
    if j-i<=2:
        return (frozenset(),)
    ans=[]
    for k in range(i+1,j):
        for l in triangulations(i,k):
            for r in triangulations(k,j):
                s=l|r
                if k-i>1:s=s|{(i,k)}
                if j-k>1:s=s|{(k,j)}
                ans.append(s)
    return tuple(ans)

def catalan(k):
    return comb(2*k,k)//(k+1)

def all_subsets(s):
    ss=tuple(s)
    for b in range(1<<len(ss)):
        yield frozenset(ss[i] for i in range(len(ss)) if (b>>i)&1)

def count_extensions_by_catalan(n,s):
    # For a noncrossing set s, faces are recovered by splitting polygon cells.
    faces=[tuple(range(n))]
    for e in sorted(s):
        a,b=e
        for k,F in enumerate(faces):
            if a in F and b in F:
                ia,ib=F.index(a),F.index(b)
                if ia>ib:ia,ib=ib,ia
                F1=F[ia:ib+1]
                F2=F[ib:]+F[:ia+1]
                if len(F1)<3 or len(F2)<3:
                    raise AssertionError(('invalid diagonal',n,s,e,F))
                faces.pop(k)
                faces.extend((F1,F2))
                break
        else:
            raise AssertionError(('crossing or invalid',n,s,e))
    prod=1
    for F in faces:
        prod*=catalan(len(F)-2)
    return prod

checks=0
for n in range(4,10):
    ts=triangulations(0,n-1)
    assert len(ts)==catalan(n-2)
    assert len(ts)==len(set(ts))
    frequency={frozenset():len(ts)}
    for t in ts:
        for s in all_subsets(t):
            frequency[s]=frequency.get(s,0)+1 if s else len(ts)
    # The preceding loop double-counts the empty set only if it were updated;
    # in this implementation the empty set remains exactly len(ts).
    for s,k in frequency.items():
        assert k==sum(s<=t for t in ts),(n,s,k)
        assert count_extensions_by_catalan(n,s)==k,(n,s,k)
        checks+=2
    # Every compatible pair is tested, with all shared diagonals allowed.
    # All pairs A,B drawn as subsets of one triangulation have compatible union.
    for t in ts:
        subsets=tuple(all_subsets(t))
        for A in subsets:
            for B in subsets:
                lhs=frequency[A|B]*frequency[A&B]
                rhs=frequency[A]*frequency[B]
                assert lhs>=rhs,(n,A,B,lhs,rhs)
                # When union compatible and A,B nonempty, unconditional covariance is strict.
                if A and B:
                    assert frequency[A|B]*len(ts)>frequency[A]*frequency[B],(n,A,B)
                checks+=1
    # Conditional two-edge signs for all feasible partial triangulations.
    diagonals=set().union(*ts)
    for S,w in frequency.items():
        extensions=[t for t in ts if S<=t]
        allowed=[d for d in diagonals-S if any(d in t for t in extensions)]
        for d,e in combinations(allowed,2):
            c1=sum(d in t for t in extensions)
            c2=sum(e in t for t in extensions)
            both=sum(d in t and e in t for t in extensions)
            sign=both*w-c1*c2
            compatible=both>0
            # If d,e belong to different residual cells, then independent.
            # If both can co-occur but are in one cell, covariance is positive.
            # The cell criterion is detected geometrically by splitting along S.
            faces=[tuple(range(n))]
            for a,b in sorted(S):
                for k,F in enumerate(faces):
                    if a in F and b in F:
                        ia,ib=F.index(a),F.index(b)
                        if ia>ib:ia,ib=ib,ia
                        faces.pop(k)
                        faces.extend((F[ia:ib+1],F[ib:]+F[:ia+1]));break
            fd=next(i for i,F in enumerate(faces) if d[0] in F and d[1] in F)
            fe=next(i for i,F in enumerate(faces) if e[0] in F and e[1] in F)
            if fd!=fe:assert sign==0,(n,S,d,e,sign)
            elif compatible:assert sign>0,(n,S,d,e,sign)
            else:assert sign<0,(n,S,d,e,sign)
            checks+=1
    print(f'N={n} triangulations={len(ts)} admissible_diagonal_sets={len(frequency)} PASS')
for b in range(0,35):
    for a in range(1,20):
        for c in range(1,20):
            assert catalan(b)*catalan(b+a+c)>catalan(b+a)*catalan(b+c)
            checks+=1
print('PASS:', checks, 'exact assertions (exhaustive triangulations through 9 vertices)')
