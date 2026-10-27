"""Independent finite checks of exact formulas for a critical bipartite phase map.
Run: python verify_parabolic_cycle.py
Finite diagnostics support, but do not prove, the all-graph assertions.
"""
import math
import numpy as np

def graph(n,a,b,edges):
    w=np.zeros((n,n))
    for i,j,wt in edges:
        assert ((i in a and j in b) or (i in b and j in a)) and wt>0
        w[i,j]=w[j,i]=float(wt)
    da=np.array([w[i].sum() for i in a]);db=np.array([w[i].sum() for i in b]);
    assert max(da)-min(da)<1e-12 and max(db)-min(db)<1e-12
    lap=np.diag(w.sum(1))-w
    lam=da[0]+db[0]
    assert np.linalg.eigvalsh(lap)[-1]-lam<1e-11
    return w,lap,lam

def F(x,h,w):
    d=x[:,None]-x[None,:]
    return x+h*(w*np.sin(d)).sum(axis=1)

def Q(x,h,w,a,b):
    z=np.zeros(len(x));
    for i in a:
        for j in b:
            wt=w[i,j];d=x[i]-x[j];z[i]+=h*wt*d*d/2;z[j]-=h*wt*d*d/2
    return z

def W(x,h,w,a,b):
    y=Q(x,h,w,a,b);return .5*y@y

def gradient_W(x,h,w,a,b):
    q=Q(x,h,w,a,b)
    J=np.zeros((len(x),len(x)))
    for i in a:
        for j in b:
            wt=w[i,j];t=h*wt*(x[i]-x[j]);
            J[i,i]+=t;J[j,j]+=t;J[i,j]-=t;J[j,i]-=t
    return J@q

graphs={
 'K_1_4':(5,[0],[1,2,3,4],[(0,j,1.) for j in range(1,5)]),
 'K_2_3':(5,[0,1],[2,3,4],[(i,j,1.) for i in [0,1] for j in [2,3,4]]),
 'weighted_C4':(4,[0,2],[1,3],[(0,1,1.),(1,2,2.),(2,3,1.),(0,3,2.)]),
 'C6':(6,[0,2,4],[1,3,5],[(i,(i+1)%6,1.) if i%2==0 else ((i+1)%6,i,1.) for i in range(6)])
}
rs=np.random.default_rng(7342)
count=0
for name,(n,a,b,edges) in graphs.items():
    w,L,lam=graph(n,a,b,edges)
    h=math.pi/lam
    # Weighted group mean zero and differences 3*pi/2.
    d=1.5*math.pi
    theta=np.zeros(n)
    theta[a]=len(b)*d/n;theta[b]=-len(a)*d/n
    after=F(theta,h,w)
    assert max(abs(F(after,h,w)-theta))<2e-14
    assert abs((after[a[0]]-after[b[0]])-.5*math.pi)<2e-14
    assert np.max(np.abs((np.eye(n)-h*np.cos(d)*L)-np.eye(n)))<1e-13
    for eps in [.08,.04,.02,.01]:
        v=rs.normal(size=n);v-=v.mean();v/=np.linalg.norm(v)
        u=eps*v
        actual=F(F(theta+u,h,w),h,w)-theta
        expected=u-gradient_W(u,h,w,a,b)
        assert np.linalg.norm(actual-expected)<20*eps**4
        newnorm=np.dot(actual,actual)
        oldnorm=np.dot(u,u)
        assert newnorm<oldnorm
        assert W(u,h,w,a,b)>0
        count+=1
    # Direct spectral test for stable / repelling constructed two-cycle.
    for delta in [.1,.6,1.3,math.pi/2,1.9]:
        h2=2*delta/(lam*math.sin(delta))
        mu=(1-h2*math.cos(delta)*np.linalg.eigvalsh(L)[1:])**2
        if delta<math.pi/2: assert max(mu)<1+1e-13
        elif delta>math.pi/2: assert min(mu)>1-1e-13
        else: assert max(abs(mu-1))<1e-13
        count+=1
    print('GRAPH_FORMULAS_PASS',name,'vertices',n,'lambda',int(lam))
print('TAYLOR_AND_SPECTRAL_TESTS_PASS',count)
# Universal cubic coefficient for scalar two-color mode.
import sympy as s
u=s.symbols('u',real=True)
# f_+(u)=u+pi*(1-cos(u)); f_-(v)=v+pi*(cos(v)-1)
p=s.symbols('p', positive=True)
v=u+p*(1-s.cos(u))
f2=v+p*(s.cos(v)-1)
assert s.simplify(s.diff(f2,u,3).subs(u,0))==-3*p**2
print('EXACT_CUBIC_COEFFICIENT_PASS','-pi^2/2')
print('INFINITE_GRAPH_AND_ASYMPTOTIC_CLAIMS_REQUIRE_ANALYTIC_PROOF')
