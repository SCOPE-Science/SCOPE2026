#!/usr/bin/env python3
"""Exact finite checks of three-shell degree-two Walsh sampling criteria.
All identities in the theorem are proved separately; these are finite checks.
"""
from fractions import Fraction
from math import comb, isqrt

def node_solutions(n):
    # Pair enumeration plus algebraic elimination of the third node.
    values=range(-n,n+1,2)
    for a in values:
        for b in range(a+2,n+1,2):
            den=a*b+n
            num=-n*(a+b)
            if den==0:
                continue
            if num % den: continue
            c=num//den
            if not (b<c<=n) or (c-n)%2: continue
            if a*b+a*c+b*c!=-(3*n-2): continue
            assert a*b*c==-n*(a+b+c)
            yield (a,b,c)

def node_solutions_one_parameter(n):
    # Algebraically exhaustive O(n) single-root discriminant algorithm.
    from math import isqrt
    for a in range(-n,n+1,2):
        den=a*a-n
        if den==0: continue
        num=-2*a*(n-1)
        if num%den:continue
        u=num//den
        v=-(3*n-2)-a*u
        disc=u*u-4*v
        if disc<=0:continue
        d=isqrt(disc)
        if d*d!=disc or (u-d)%2:continue
        b=(u-d)//2; c=(u+d)//2
        if a<b<c<=n and (b-n)%2==0 and (c-n)%2==0:
            yield (a,b,c)

def weights(n,tr):
    res=[]
    for j,x in enumerate(tr):
        others=[y for k,y in enumerate(tr) if k!=j]
        u,v=others
        res.append(Fraction(n+u*v,(x-u)*(x-v)))
    return res

def krawtchouk(n,k,t):
    return sum((-1)**j*comb(k,j)*comb(n-k,t-j)
               for j in range(t+1) if j<=k and t-j<=n-k)

def check(n,tr):
    ws=weights(n,tr)
    assert all(w>0 for w in ws)
    assert sum(ws)==1
    assert sum(w*node for w,node in zip(ws,tr))==0
    assert sum(w*node**2 for w,node in zip(ws,tr))==n
    assert sum(w*node**3 for w,node in zip(ws,tr))==0
    assert sum(w*node**4 for w,node in zip(ws,tr))==3*n*n-2*n
    for t in range(1,5):
        assert sum(w*krawtchouk(n,(n-s)//2,t) for w,s in zip(ws,tr))==0
    return ws

def main():
    total=0; dims=[]; pole=0; symmetric=0
    for n in range(4,251):
        triples=list(node_solutions(n))
        assert triples==list(node_solutions_one_parameter(n))
        if triples:dims.append(n)
        for tr in triples:
            ws=check(n,tr);total+=1
            pole_here=(abs(tr[0])==n or abs(tr[2])==n)
            if pole_here:
                pole+=1
                assert isqrt(n-1)**2==n-1
            symmetric_here=tr[0]==-tr[2] and tr[1]==0
            if symmetric_here:
                symmetric+=1
                assert (3*n-2)==tr[2]**2
    for n in range(4,65):
        triples=list(node_solutions(n))
        assert len(triples)<=2
        if len(triples)==2:assert triples[1]==tuple(-x for x in reversed(triples[0]))
    first_nonunique=min(n for n in range(4,251) if len(list(node_solutions(n)))>2)
    assert first_nonunique==65
    pell_pairs=[]
    sr,rr=14,8
    for j in range(20):
        assert sr*sr-3*rr*rr==4
        n=rr*rr+1
        endpoint=(-n,1-rr,1+rr)
        interior=(-sr-1,-1,sr-1)
        assert endpoint!=interior
        check(n,endpoint);check(n,interior)
        pell_pairs.append((n,sr,rr))
        sr,rr=2*sr+3*rr,sr+2*rr
    for r in range(2,101):
        n=r*r+1
        tr=(-n,1-r,1+r)
        ws=check(n,tr)
        assert ws[0]==Fraction(2,n*n+n+2)
        assert ws[1]==Fraction(n,2*(n+1-r))
        assert ws[2]==Fraction(n,2*(n+1+r))
    for r in range(2,101):
        if r%3==0:continue
        n=(4*r*r+2)//3
        tr=(-2*r,0,2*r)
        assert n>=4
        check(n,tr)
    for r in range(4,101,2):
        if r%3==0:continue
        n=(r*r-1)//3
        tr=(-r-1,-1,r-1)
        assert n>=4
        check(n,tr)
    # Independent exhaustive character Gram for n=5,6: 1 + n + C(n,2) Walsh modes.
    from itertools import combinations
    gram_checks=0
    for n,tr in [(5,(-5,-1,3)),(6,(-4,0,4))]:
        ws=weights(n,tr)
        idxs=[()] + [(i,) for i in range(n)] + list(combinations(range(n),2))
        for I in idxs:
            for J in idxs:
                diff=set(I).symmetric_difference(J)
                v=0
                for shell_s,w in zip(tr,ws):
                    k=(n-shell_s)//2
                    v+=w*Fraction(krawtchouk(n,k,len(diff)),comb(n,len(diff)))
                assert v==(1 if I==J else 0)
                gram_checks+=1
    print('VERIFY_OK n_range=4..250 valid_triples=%d dimensions=%d endpoint_triples=%d symmetric_triples=%d infinite_family_parameter_checks=100+66+%d full_gram_entries=%d' % (total,len(dims),pole,symmetric,len([r for r in range(4,101,2) if r%3]),gram_checks))
    print('first_nonunique_dimension=',first_nonunique,'Pell_start=',pell_pairs[:4])
    print('first_30_dimensions_with_three_shell_designs',dims[:30])
    for n in (5,6,10,21,22,33,65,145,226):
        sols=list(node_solutions(n))
        print('n',n,'solutions',[(tr,[str(w) for w in weights(n,tr)]) for tr in sols])
if __name__=='__main__':main()
