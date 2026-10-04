#!/usr/bin/env python3
from fractions import Fraction as F
from itertools import combinations

def trim(p):
    p=list(p)
    while len(p)>1 and p[-1]==0: p.pop()
    return p

def add(a,b):
    n=max(len(a),len(b)); r=[F(0)]*n
    for i,x in enumerate(a): r[i]+=x
    for i,x in enumerate(b): r[i]+=x
    return trim(r)

def scale(a,s): return trim([x*s for x in a])
def mul(a,b):
    r=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): r[i+j]+=x*y
    return trim(r)
def deriv(a): return trim([F(i)*a[i] for i in range(1,len(a))] or [F(0)])
def degree(a): return len(trim(a))-1

def divmodp(a,b):
    a=trim(a); b=trim(b)
    if b==[0]: raise ZeroDivisionError
    if degree(a)<degree(b): return [F(0)],a
    q=[F(0)]*(degree(a)-degree(b)+1); r=a[:]
    while r!=[0] and degree(r)>=degree(b):
        k=degree(r)-degree(b); t=r[-1]/b[-1]; q[k]+=t
        sub=[F(0)]*k+scale(b,t)
        r=add(r,scale(sub,F(-1)))
    return trim(q),trim(r)

def gcdp(a,b):
    a=trim(a); b=trim(b)
    while b!=[0]:
        _,r=divmodp(a,b); a,b=b,r
    if a==[0]: return a
    return scale(a,F(1,1)/a[-1])

def prod(ps):
    r=[F(1)]
    for p in ps:r=mul(r,p)
    return r

def det3_col3(zs, vals):
    z1,z2,z3=map(F,zs); v1,v2,v3=map(F,vals)
    return v1*(z3-z2)+v2*(z1-z3)+v3*(z2-z1)

def build(n):
    z=list(range(1,n+1))
    pool=[3,11,5,19,7,23,13,29]
    u=pool[:n]
    s=[[F(1),F(zi)] for zi in z]
    P=prod(s)
    D=[F(0)]
    for i,j in combinations(range(n),2):
        term=prod([mul(s[k],s[k]) for k in range(n) if k not in (i,j)])
        D=add(D,scale(term,F((z[i]-z[j])**2)))
    N=[F(0)]
    for i,j,k in combinations(range(n),3):
        ids=(i,j,k)
        l0=det3_col3([z[q] for q in ids],[u[q] for q in ids])
        l1=det3_col3([z[q] for q in ids],[u[q]*z[q] for q in ids])
        L=[l0,l1]
        term=mul(mul(L,L),prod([mul(s[q],s[q]) for q in range(n) if q not in ids]))
        N=add(N,term)
    mean=F(sum(u),n)
    H=[F(0)]
    for i in range(n):
        H=add(H,scale(prod([s[j] for j in range(n) if j!=i]),mean-F(u[i])))
    assert H[0]==0
    S=trim(H[1:])
    J=add(mul(deriv(N),D),scale(mul(N,deriv(D)),F(-1)))
    Q,R=divmodp(J,S)
    did=add(scale(mul(deriv(P),deriv(P)),F(n-1)),scale(mul(P,deriv(deriv(P))),F(-n)))
    return N,D,S,J,Q,R,did

def main():
    for n in range(4,9):
        N,D,S,J,Q,R,did=build(n)
        assert D==did
        assert degree(N)==2*n-4 and degree(D)==2*n-4
        assert degree(gcdp(N,D))==0
        assert degree(J)==4*n-10
        assert degree(S)==n-2 and R==[0]
        assert degree(Q)==3*n-8
        assert degree(gcdp(S,Q))==0
        assert degree(gcdp(J,deriv(J)))==0
        assert degree(gcdp(D,deriv(D)))==0
        print(f'n={n}: deg(N,D,J,S,Q)=({degree(N)},{degree(D)},{degree(J)},{degree(S)},{degree(Q)})')
    print('VERIFY_OK')
if __name__=='__main__': main()
