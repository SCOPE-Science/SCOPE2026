#!/usr/bin/env python3
"""Finite frame proof check for ordered binary-modal associativity."""
from itertools import product

def tuples(n):
    return tuple(product(range(n), repeat=3))

def is_upset(S,n):
    return all(v in S for x in S for v in range(x,n))

def upsets(n):
    return [frozenset(range(k,n)) for k in range(n+1)]

def bmi(R,n):
    for u,a,b in R:
        for v in range(u,n):
            if not any((v,x,y) in R for x in range(a,n) for y in range(b,n)):
                return False
        for x in range(a,n):
            for y in range(b,n):
                if not any((v,x,y) in R for v in range(u,n)):
                    return False
    return True

def cmp_rel(R,n):
    E = {(u,a,b) for u,a,b in tuples(n) if any((v,a,b) in R for v in range(u,n))}
    return E

def composed(T,n):
    L = {u:set() for u in range(n)}
    M = {u:set() for u in range(n)}
    for u,a,b,c,t in product(range(n),repeat=5):
        if (t,a,b) in T and (u,t,c) in T:
            L[u].add((a,b,c))
        if (t,b,c) in T and (u,a,t) in T:
            M[u].add((a,b,c))
    return L,M

def closure_equal(L,M,n,up):
    def is_member(p, T):
        if up:
            return any(all(t[i]<=p[i] for i in range(3)) for t in T)
        return any(all(p[i]<=t[i] for i in range(3)) for t in T)
    return all(is_member(p,L)==is_member(p,M) for p in product(range(n),repeat=3))

def closure_assoc(R,n):
    L,M=composed(R,n)
    E=cmp_rel(R,n)
    P,Q=composed(E,n)
    return (all(closure_equal(L[u],M[u],n,False) for u in range(n)),
            all(closure_equal(P[u],Q[u],n,True) for u in range(n)))

def semantic_assoc(R,n):
    ups=upsets(n)
    def circle(A,B):
        return frozenset(u for u in range(n) if any((u,a,b) in R for a in A for b in B))
    def bullet(A,B):
        return frozenset(u for u in range(n) if all(a in A or b in B for v in range(u,n) for a in range(n) for b in range(n) if (v,a,b) in R))
    cr=br=True
    for A,B,C in product(ups,repeat=3):
        cr &= circle(circle(A,B),C)==circle(A,circle(B,C))
        br &= bullet(bullet(A,B),C)==bullet(A,bullet(B,C))
    return bool(cr),bool(br)

def raw_assoc(R,n):
    return all((any((t,a,b) in R and (u,t,c) in R for t in range(n)) ==
                any((t,b,c) in R and (u,a,t) in R for t in range(n)))
               for u,a,b,c in product(range(n),repeat=4))

def main():
    for n in (1,2):
        summary={}
        for mask in range(1 << n**3):
            R={t for k,t in enumerate(tuples(n)) if (mask>>k)&1}
            if not bmi(R,n): continue
            direct=semantic_assoc(R,n)
            relational=closure_assoc(R,n)
            assert direct==relational, (n,mask,direct,relational)
            assert direct[1]==raw_assoc(cmp_rel(R,n),n)
            r=raw_assoc(R,n)
            key=(direct==(True,True),r)
            summary[key]=summary.get(key,0)+1
        print('n =',n,'BMI frames:',sum(summary.values()),'joint associative versus strict relational:',summary)
        if n==1: assert summary=={(True,True):2}
        if n==2: assert summary=={(True,True):32,(False,False):24,(True,False):11}
    witness={(0,0,0),(0,1,0),(0,1,1),(1,0,1),(1,1,1)}
    assert bmi(witness,2) and semantic_assoc(witness,2)==(True,True)
    assert not raw_assoc(witness,2)
    # Check explicit deviation at the advertised indices.
    u,a,b,c=0,1,0,1
    assert not any((t,a,b) in witness and (u,t,c) in witness for t in (0,1))
    assert any((t,b,c) in witness and (u,a,t) in witness for t in (0,1))
    count3=0
    # Independent tests on ternary relations induced by all binary operations
    # on the three-element chain. The search space contains 3^9 operations.
    for output in product(range(3),repeat=9):
        R={(output[3*a+b],a,b) for a in range(3) for b in range(3)}
        if not bmi(R,3):
            continue
        assert semantic_assoc(R,3)==closure_assoc(R,3)
        assert semantic_assoc(R,3)[1]==raw_assoc(cmp_rel(R,3),3)
        count3+=1
    assert count3==95, count3
    print('n = 3 BMI functional ternary relations checked:',count3)
    witness3={(0,0,0),(0,0,1),(0,0,2),(0,1,0),(0,1,1),
              (1,1,2),(1,2,0),(1,2,1),(2,2,2)}
    assert bmi(witness3,3)
    assert semantic_assoc(witness3,3)==closure_assoc(witness3,3)==(False,False)
    print('EXPLICIT_WITNESS_OK; ASSOCIATIVITY_CLOSURE_CROSSCHECK_OK')
if __name__=='__main__':main()
