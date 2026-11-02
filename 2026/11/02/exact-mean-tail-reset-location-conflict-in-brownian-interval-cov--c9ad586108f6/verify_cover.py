"""Independent finite-state and spectral checks for reflected resetting cover times."""
import math
import numpy as np
from scipy.sparse import lil_matrix, csc_matrix
from scipy.sparse.linalg import spsolve, eigs
from scipy.optimize import brentq


def exact_mean(s, z, r):
    a = math.cosh(s)
    c = math.cosh(s / 2)
    return (a / math.cosh(s*z) + a / math.cosh(s*(1-z))
            - c / math.cosh(s*(z-.5)) - 1) / r


def finite_chain_mean(n, r, j):
    d = n*n
    states = ([('U', i) for i in range(1, n)]
              + [('A', i) for i in range(n)]
              + [('B', i) for i in range(1, n+1)])
    idx = {state:k for k,state in enumerate(states)}
    Q = lil_matrix((len(states),len(states)), dtype=float)
    for key, k in idx.items():
        flag, i = key
        transitions = []
        if flag == 'U':
            transitions = [(('A',0) if i==1 else ('U',i-1),d),
                           (('B',n) if i==n-1 else ('U',i+1),d)]
        elif flag == 'A':
            transitions = [(('A',1),2*d)] if i==0 else [(('A',i-1),d)]
            if i < n-1:
                transitions.append((('A',i+1), d))
            else:
                transitions.append((None,d))
        elif flag == 'B':
            transitions = [(('B',n-1),2*d)] if i==n else [(('B',i+1),d)]
            if i > 1:
                transitions.append((('B',i-1),d))
            else:
                transitions.append((None,d))
        transitions.append(((flag,j),r))
        for target, rate in transitions:
            if target==key:
                continue
            Q[k,k] -= rate
            if target is not None:
                Q[k,idx[target]] += rate
    sol = spsolve((-Q).tocsc(), np.ones(len(states)))
    return sol[idx[('U',j)]]


def phi(q,z):
    if abs(q)<1e-9:
        return 1-q*(2*z-z*z)/2
    if q>0:
        sq=math.sqrt(q)
        return math.cosh(sq*(1-z))/math.cosh(sq)
    sq=math.sqrt(-q)
    return math.cos(sq*(1-z))/math.cos(sq)


def s0(q,z):
    if abs(q)<1e-7:
        # E tau0=(2z-z²)/2; second moment from solving -D m2''=2*m1
        # m2(z) = (2/3)*z - z^3/3 + z^4/12? exact via symbolic integration below
        return (2*z-z*z)/2
    return (1-phi(q,z))/q


def decay_lambda(r,z):
    delta=math.pi**2/4
    q=brentq(lambda w:r*s0(w,z)-1,-delta+1e-8,r,xtol=1e-13)
    return r-q


def finite_chain_lambda(n,r,j):
    d=n*n
    Q=lil_matrix((n,n),dtype=float)
    for i in range(1,n+1):
        k=i-1
        trans=[(i-1,d),(i+1,d)] if i<n else [(i-1,2*d)]
        for target,rate in trans+[(j,r)]:
            if target==i: continue
            Q[k,k]-=rate
            if 1<=target<=n:Q[k,target-1]+=rate
    return -float(eigs(Q.tocsc(),k=1,which='LR',return_eigenvectors=False,tol=1e-11,v0=np.ones(n))[0].real)


def check():
    count=0
    c0=(1+math.sqrt(17))/4
    s0=2*math.acosh(c0)
    s_spinodal=2*math.asinh(5**(-.25))
    assert s_spinodal<s0
    count+=1
    for s in [.4,1.1,1.4,s0,1.6,2.5,5.]:
        r=s*s
        vals=np.array([exact_mean(s,float(z),r) for z in np.linspace(0,.5,1001)])
        expected=min(exact_mean(s,0,r),exact_mean(s,.5,r))
        assert vals.min()>=expected-5e-11
        assert abs(vals[0]-vals[-1])<1e-9 if abs(s-s0)<1e-9 else True
        count+=2
    for r in [0.5,2.0,5.0]:
        for j in [10,25,40,50]:
            approx=finite_chain_mean(100,r,j)
            exact=exact_mean(math.sqrt(r),j/100,r)
            assert abs(approx-exact)<.018, (r,j,approx,exact)
            count+=1
    for r in [.25,1,3,7]:
        ls=[decay_lambda(r,z) for z in [.1,.2,.4,.5,.6,.8,.9]]
        assert all(a>b for a,b in zip(ls,ls[1:])),(r,ls)
        assert abs(ls[0]-ls[-1])>1e-2
        count+=2
        for z in [.2,.35,.5]:
            lc=min(decay_lambda(r,z),decay_lambda(r,1-z))
            assert lc<=decay_lambda(r,.5)+1e-11
            count+=1
    for r in [1.,3.]:
        for j in [15,30,45]:
            exact=decay_lambda(r,j/60)
            approx=finite_chain_lambda(60,r,j)
            assert abs(exact-approx)<.08,(r,j,exact,approx)
            count+=1
    print('PASS checks',count,'spinodal',format(s_spinodal,'.12f'),
          'global',format(s0,'.12f'), 'global rho',format(s0*s0,'.12f'))
    for r in [1.,2.,3.,5.]:
        print('r',r,'mean edge',exact_mean(math.sqrt(r),0,r),
            'mean mid',exact_mean(math.sqrt(r),.5,r),
            'tail edge',decay_lambda(r,1),
            'tail mid',decay_lambda(r,.5))

if __name__=='__main__':check()
