#!/usr/bin/env python3
"""Finite checks for reflection characters of ordinary three-cut cycle-power complexes.

Python standard library only; exhaustive checks here are finite, not an infinite proof.
"""
from itertools import combinations
from math import gcd

def perm_sign(values):
    return -1 if sum(values[i]>values[j] for i in range(len(values)) for j in range(i+1,len(values)))%2 else 1

def dist(a,b,n):
    k=(a-b)%n
    return min(k,n-k)

def good(S,n,p):
    """Every 3-subset of S connected, via direct triples rather than complements."""
    for a,b,c in combinations(S,3):
        e=(dist(a,b,n)<=p)+(dist(a,c,n)<=p)+(dist(b,c,n)<=p)
        if e<2:return False
    return True

def orbits(n,map_vertex):
    seen=set();out=[]
    for a in range(n):
        if a in seen:continue
        x=a;orb=[]
        while x not in seen:
            seen.add(x);orb.append(x);x=map_vertex(x)
        assert x==a
        out.append(tuple(sorted(orb)))
    return out

def direct_dual_trace(n,p,map_vertex):
    """Exact signed simplicial chain trace on dual, invariant simplex by simplex."""
    orb=orbits(n,map_vertex)
    result=0;fixed=0
    def explore(k,selected):
        nonlocal result,fixed
        if k==len(orb):
            if not selected:return
            fixed+=1
            w=sorted(selected)
            # image permutation of oriented simplex
            order=[map_vertex(x) for x in w]
            sgn=perm_sign(order)
            result+=(-1)**(len(w)-1)*sgn
            return
        explore(k+1,selected)
        ss=selected+list(orb[k])
        if good(ss,n,p):explore(k+1,ss)
    explore(0,[])
    return result,fixed

def expected_reflection(n,p,c):
    if n%2:return ((-1)**((n+1)//2))*((n-4*p+1)//2)
    k=n//2
    if c%2==0:return (-1)**k*(k-2*p-1)
    return (-1)**(k+1)*(k-2*p+1)

def cut_face(mask,n,p):
    T=[i for i in range(n) if not (mask>>i)&1]
    return any((dist(a,b,n)>p and dist(a,c,n)>p) or
               (dist(b,a,n)>p and dist(b,c,n)>p) or
               (dist(c,a,n)>p and dist(c,b,n)>p)
               for a,b,c in combinations(T,3))

def direct_cut_trace(n,p,c):
    """Independent direct complex, not using Alexander dual to enumerate faces."""
    L=-1 # reduced empty simplex contribution
    for mask in range(1,1<<n):
        if not cut_face(mask,n,p):continue
        vs=[i for i in range(n) if mask>>i&1]
        im=[(c-i)%n for i in vs]
        if set(im)!=set(vs):continue
        L+=(-1)**(len(vs)-1)*perm_sign(im)
    return ((-1)**(n-4))*L

def gf2_b1(n,p):
    edges=list(combinations(range(n),2)); eid={e:i for i,e in enumerate(edges)}
    pivots={}; t=0
    for a,b,c in combinations(range(n),3):
        if not good((a,b,c),n,p):continue
        t+=1
        v=(1<<eid[a,b])^(1<<eid[a,c])^(1<<eid[b,c])
        while v:
            bit=v.bit_length()-1
            if bit in pivots:v^=pivots[bit]
            else:
                pivots[bit]=v;break
    return len(edges)-(n-1)-len(pivots),t

def main():
    num=0
    for p in range(2,8):
        for n in range(6*p-3,6*p+7):
            for c in ([0,1] if n%2==0 else [0]):
                e,_=direct_dual_trace(n,p,lambda x,c=c,n=n:(c-x)%n)
                # dual connected, cohomology H^1 only by published theorem
                trace_on_K=perm_sign([(c-i)%n for i in range(n)])*(1-e)
                assert trace_on_K==expected_reflection(n,p,c),(p,n,c,e,trace_on_K,expected_reflection(n,p,c))
                num+=1
    print('DUAL_REFLECTION_CHECKS',num)
    num2=0
    for p,n in [(2,9),(2,10),(2,11),(2,12)]:
        for c in ([0,1] if n%2==0 else [0]):
            res=direct_cut_trace(n,p,c)
            assert res==expected_reflection(n,p,c),(p,n,c,res)
            num2+=1
    print('DIRECT_CUT_CHAIN_CHECKS',num2)
    dihedral_checks=0
    for p in range(2,5):
        for n in range(6*p-3,6*p+4):
            # Each character value comes from the signed simplicial chain action.
            # No closed-form rotation character is used in this averaging step.
            total=0
            for a in range(n):
                for sign in (1,-1):
                    permutation=lambda x,a=a,sign=sign,n=n:(sign*x+a)%n
                    lef,_=direct_dual_trace(n,p,permutation)
                    character=perm_sign([permutation(x) for x in range(n)])*(1-lef)
                    total+=character
            assert total%(2*n)==0,(p,n,total)
            computed=total//(2*n)
            if n%4==1:expect=0
            elif n%4==3:expect=(n-4*p+1)//2
            elif n%4==0:expect=(n-4*p-4)//4
            else:expect=(n-4*p+2)//4
            assert computed==expect,(p,n,computed,expect)
            dihedral_checks+=1
    print('FULL_DIHEDRAL_QUOTIENT_CHECKS',dihedral_checks)
    for n,p in [(9,2),(10,2),(11,2),(12,2),(15,3)]:
        b,t=gf2_b1(n,p)
        known=1+n*(n-4*p-1)//2
        assert b==known,(n,p,b,known)
        print('DUAL_GF2_H1',n,p,b,'TRIANGLES',t)
    print('VERIFY_OK')

if __name__=='__main__':main()
