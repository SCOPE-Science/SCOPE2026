"""Exact checks for successful-hop activity in two hard-core persistent walkers.

Execute: python verify_activity.py  (requires sympy; see requirements.txt).
Finite rational tests supplement the stated symbolic derivation; they are not
exhaustive tests over positive real reversal rates.
"""
from itertools import product
import sympy as sp

A = sp.Symbol('a', positive=True)

def orbits(n):
    remaining = [(d,u,v) for d in range(1,n) for u,v in product((-1,1), repeat=2)]
    ans = []
    while remaining:
        d,u,v = remaining[0]
        o = {(d,u,v),(n-d,-u,-v),(n-d,v,u),(d,-v,-u)}
        ans.append(tuple(sorted(o)))
        remaining = [z for z in remaining if z not in o]
    return ans

def matrices(n, a, lump):
    classes = orbits(n) if lump else [((d,u,v),) for d in range(1,n) for u,v in product((-1,1), repeat=2)]
    index = {state:i for i,cls in enumerate(classes) for state in cls}
    size = len(classes)
    q, j = sp.zeros(size), sp.zeros(size)
    for i, cls in enumerate(classes):
        d,u,v = cls[0]
        transitions = [((d,-u,v), a, False), ((d,u,-v), a, False),
                       (((d-u)%n,u,v), sp.Integer(1), True),
                       (((d+v)%n,u,v), sp.Integer(1), True)]
        for dest, rate, counted in transitions:
            if dest[0] == 0:  # blocked motion is not counted
                continue
            k = index[dest]
            q[i,k] += rate
            q[i,i] -= rate
            if counted:
                j[i,k] += rate  # includes within-orbit counted transitions
    assert q*sp.ones(size,1) == sp.zeros(size,1)
    return q,j

def cumulants(q,j):
    m = q.rows
    stationary_matrix=q.T.copy();stationary_matrix[m-1,:]=sp.ones(1,m)
    rhs=sp.zeros(m,1);rhs[m-1]=1
    p=stationary_matrix.LUsolve(rhs)
    h=j*sp.ones(m,1)
    mean=sp.factor((p.T*h)[0])
    correction=q.copy();correction[0,:]=p.T
    brhs=mean*sp.ones(m,1)-h;brhs[0]=0
    g=correction.LUsolve(brhs)
    variance=sp.factor(mean+2*(p.T*j*g)[0])
    return mean,variance,sp.factor(variance/mean)

def target(n):
    if n==3:
        mean=(2*A+1)/(2*(A+1))
        f=(4*A**3+6*A**2+5*A+1)/(4*A*(A+1)**2)
    elif n==4:
        mean=2*(2*A+1)**2/(6*A**2+8*A+3)
        f=(40*A**5+96*A**4+104*A**3+66*A**2+22*A+3)/(A*(6*A**2+8*A+3)**2)
    else:raise ValueError(n)
    return mean,f

for n in (3,4):
    q,j=matrices(n,A,True)
    mean,var,f=cumulants(q,j)
    target_mean,target_f=target(n)
    assert sp.cancel(mean-target_mean)==0
    assert sp.cancel(f-target_f)==0
    print('symbolic quotient PASS n=',n,'dimension=',q.rows)
    for a in (sp.Rational(1,3),sp.Rational(1,2),sp.Integer(1),sp.Rational(5,2),sp.Integer(5)):
        qfull,jfull=matrices(n,a,False)
        mf,vf,ff=cumulants(qfull,jfull)
        assert mf==sp.factor(target_mean.subs(A,a))
        assert ff==sp.factor(target_f.subs(A,a))
        print('full-state exact PASS n=',n,'a=',a,'mean=',mf,'F=',ff)

f3=target(3)[1];f4=target(4)[1]
assert sp.cancel((f3-1)+(A-1)*(2*A+1)/(4*A*(A+1)**2))==0
assert sp.cancel((f4-1)-(A+1)*(A**2*(2*A-1)**2+7*A**2+10*A+3)/(A*(6*A**2+8*A+3)**2))==0
assert sp.cancel(sp.diff(f3,A)-(2*A**3-4*A**2-3*A-1)/(4*A**2*(A+1)**3))==0
assert sp.cancel(sp.diff(f4,A)-(64*A**6-324*A**4-432*A**3-244*A**2-72*A-9)/(A**2*(6*A**2+8*A+3)**3))==0
assert sp.limit(f3,A,sp.oo)==1
assert sp.limit(f4,A,sp.oo)==sp.Rational(10,9)
print('sign, derivative, and limits PASS')
print('All exact checks passed.')
