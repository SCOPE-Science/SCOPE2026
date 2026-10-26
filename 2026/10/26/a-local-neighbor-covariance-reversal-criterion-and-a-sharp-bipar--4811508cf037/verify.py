"""Independent finite-state checks for covariance under deterministic resetting.
Run: python verify.py. Analytical all-graph and all-m theorems require the written proof.
"""
import itertools
import math
from fractions import Fraction
import numpy as np
import sympy as sp

R=sp.symbols('r',positive=True)
checks=0

def assert_equal(a,b):
    global checks
    assert sp.simplify(a-b)==0,(a,b)
    checks+=1

def assert_close(a,b,tol=1.e-10):
    global checks
    assert abs(a-b)<tol,(a,b)
    checks+=1

def CTMC(n,edges,occupied,rate):
    # Column-generator convention; the resetting transition replaces any state by occupied.
    k=len(occupied)
    states=list(itertools.combinations(range(n),k))
    idx={s:i for i,s in enumerate(states)}
    q=np.zeros((len(states),len(states)))
    for i,s in enumerate(states):
        occupied_here=set(s)
        for x,y in edges:
            if (x in occupied_here) != (y in occupied_here):
                neighbor=tuple(sorted(occupied_here.symmetric_difference((x,y))))
                j=idx[neighbor]
                q[j,i]+=1.
                q[i,i]-=1.
    a=np.eye(len(states))*rate-q
    initial=np.zeros(len(states));initial[idx[tuple(sorted(occupied))]]=1.
    return states,rate*np.linalg.solve(a,initial),q

def numerical_cov(states,probs,x,y):
    ex=sum(p for s,p in zip(states,probs) if x in s)
    ey=sum(p for s,p in zip(states,probs) if y in s)
    joint=sum(p for s,p in zip(states,probs) if x in s and y in s)
    return joint-ex*ey

def bipartite_exact(m,r):
    return m*((m-2)*r-4)/((m+r+2)**2*(2*m+r+2))

# Exact symbolic reduction of the 3-state occupation-number chain (j=0,1,2).
for m in range(1,10):
    Q=sp.Matrix([[-4,m-1,0],[4,-(m+R),2*m],[0,1+R,-2*m]])
    v=(R*sp.eye(3)-Q.subs(R,0)).inv()*sp.Matrix([0,0,R])
    # Independently solving the steady reset generator tests its rates and normalization.
    assert_equal(sum(v),1)
    p0,p1,p2=map(sp.factor,v)
    den=(m+R+2)*(2*m+R+2)
    assert_equal(p0,2*m*(m-1)/den)
    assert_equal(p1,2*m*(R+4)/den)
    assert_equal(p2,(R**2+(m+4)*R+4)/den)
    assert_equal(sp.factor(p2-(p2+p1/2)**2),bipartite_exact(m,R))
    assert_equal(sp.limit(R**2*bipartite_exact(m,R),R,sp.oo),m*(m-2))

for m in range(1,8):
    n=m+2
    edges=[(i,j) for i in (0,1) for j in range(2,n)]
    for rate in (.01,.1,.7,1.,3.,10.,200.,2000.):
        states,pi,q=CTMC(n,edges,(0,1),rate)
        assert_close(sum(pi),1)
        assert_close(numerical_cov(states,pi,0,1),bipartite_exact(m,rate))
        assert np.min(pi)>-1.e-13
        checks+=1

# One-dimensional rings with half occupied sites: sign reversal between weak/strong resets.
for m in range(2,5):
    n=2*m
    edges=[(i,(i+1)%n) for i in range(n)]
    s=tuple(range(m));x,y=0,m-1
    for rate in (.0001,.01,.1,1.,10.,100.,10000.):
        states,pi,q=CTMC(n,edges,s,rate)
        c=numerical_cov(states,pi,x,y)
        if rate==.0001:
            eq=-m*(n-m)/(n*n*(n-1))
            assert_close(c,eq,tol=.002)
        if rate==10000.:
            assert_close(rate*rate*c,1.,tol=.01)
        checks+=1

# Exact four-cycle pair covariance, using a rational full 6-state generator.
n=4;edges=[(i,(i+1)%n) for i in range(n)]
cs=list(itertools.combinations(range(n),2));ix={a:i for i,a in enumerate(cs)}
Q=sp.zeros(len(cs))
for i,state in enumerate(cs):
    st=set(state)
    for a,b in edges:
        if (a in st)!=(b in st):
            j=ix[tuple(sorted(st.symmetric_difference((a,b))))]
            Q[j,i]+=1
            Q[i,i]-=1
pi=R*(R*sp.eye(len(cs))-Q).inv()*sp.eye(len(cs))[:,ix[(0,1)]]
ex=sum(pi[i] for i,s in enumerate(cs) if 0 in s)
ey=sum(pi[i] for i,s in enumerate(cs) if 1 in s)
exy=sum(pi[i] for i,s in enumerate(cs) if 0 in s and 1 in s)
assert_equal(sp.factor(exy-ex*ey),(R-2)/((R+2)**2*(R+6)))

# Shared-neighbor witness: occupied endpoints of three-vertex path.
states,pi,q=CTMC(3,[(0,1),(1,2)],(0,2),10.0)
assert_close(numerical_cov(states,pi,0,2),-1/(10.+3.)**2)
print('PASS',checks,'symbolic and independent finite-state checks')
