#!/usr/bin/env python3
"""Finite diagnostics for exact monomial Dirichlet Volterra commutators.

Run: python3 verify.py  (Python 3 standard library only).
This checker verifies finitely many instances; infinite quantifiers follow from the proof.
"""
from math import log, exp, isclose

checks = 0

def check(ok, context):
    global checks
    checks += 1
    if not ok:
        raise AssertionError(context)

# These routines are independent implementations of the original operators.
def op(c, vector):
    t = log(c)
    ans = {}
    for n, val in vector.items():
        ans[c*n] = ans.get(c*n, 0.0)+val*t/log(c*n)
    return ans

def sub(x,y):
    ans=x.copy()
    for n,a in y.items():
        ans[n]=ans.get(n,0.0)-a
    return {n:a for n,a in ans.items() if abs(a)>1e-30}

def comm(a,b,v):
    return sub(op(a,op(b,v)),op(b,op(a,v)))

def coef(a,b,n):
    u,v=log(a),log(b)
    h=log(n)
    return u*v*(u-v)/((h+u+v)*(h+u)*(h+v))

def power_coef(a,b,n,k):
    return _prod(coef(a,b,n*(a*b)**j) for j in range(k))

def _prod(it):
    out=1.0
    for a in it: out *= a
    return out

def rising(x,k):
    return _prod(x+j for j in range(k))

def two_eigs_to_logs(s1,s2):
    delta=s1
    check(0<delta<1 and 0<s2<s1,'domain inverse')
    xx=(1+delta)/2
    yy=(1-delta)/2
    L=log(2)
    def ratio(t):
        return (t/(t+L)) * (xx*t/(xx*t+L))*(yy*t/(yy*t+L))
    lo,hi=0.0,1.0
    while ratio(hi)<s2/s1: hi*=2
    for _ in range(140):
        mid=(lo+hi)/2
        if ratio(mid)<s2/s1:lo=mid
        else:hi=mid
    t=(lo+hi)/2
    return sorted((xx*t,yy*t))

pairs=[(2,3),(2,4),(2,9),(3,10),(7,19),(13,47)]
for a,b in pairs:
    u,v=log(a),log(b)
    t=u+v
    K=u*v*abs(u-v)
    for n in range(1,75):
        sample=comm(a,b,{n:1.0})
        target={a*b*n:coef(a,b,n)}
        check(len(sample)==1,'single output')
        check(set(sample)==set(target),'support agreement')
        check(isclose(next(iter(sample.values())),next(iter(target.values())), rel_tol=5e-14,abs_tol=5e-16),'coefficient direct composition')
        for k in range(1,5):
            out={n:1.0}
            for _ in range(k): out=comm(a,b,out)
            key=n*(a*b)**k
            check(list(out)==[key], 'power support')
            check(isclose(out[key],power_coef(a,b,n,k),rel_tol=2e-13,abs_tol=1e-20),'power coefficient')
        if n>1:
            check(abs(coef(a,b,n))<abs(coef(a,b,n-1)), 'monotone singular sequence')
    for k in range(1,6):
        p=u/t;q=v/t
        formula=(K/t**3)**k/(rising(p,k)*rising(q,k)*__import__('math').factorial(k))
        check(isclose(formula,abs(power_coef(a,b,1,k)),rel_tol=1e-12,abs_tol=1e-21),'norm power closed form')
    s1=abs(coef(a,b,1));s2=abs(coef(a,b,2))
    check(isclose(s1,abs(u-v)/(u+v),rel_tol=1e-13),'operator norm')
    rec=two_eigs_to_logs(s1,s2)
    check(all(isclose(x,y,rel_tol=5e-12, abs_tol=1e-13) for x,y in zip(rec,sorted((u,v)))), 'first-two-singular-value inverse')

print(f'PASS: {checks} deterministic finite assertions; analytical proof needed for all infinite claims')
