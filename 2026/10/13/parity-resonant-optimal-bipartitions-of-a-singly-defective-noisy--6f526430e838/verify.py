"""Independent finite-dimensional checks for the single-defect GHZ negativity formula."""
import math
import itertools
import numpy as np

Z=np.array([[1.,0.],[0.,0.]])
O=np.array([[0.,0.],[0.,1.]])
X=np.array([[0.,1.],[0.,0.]])
Y=X.T

def dep(x,v):
    return v*x+(1.-v)*np.trace(x)*np.eye(2)/2.

def tensor(factors):
    r=np.array([[1.]])
    for mat in factors:
        r=np.kron(r,mat)
    return r

def noisy_ghz(n,s,d):
    vis=[s]*(n-1)+[d]
    return 0.5*sum(tensor([dep(a,v) for v in vis]) for a in (Z,O,X,Y))

def ppt_neg(rho,n,sub):
    axes=list(range(2*n))
    for j in sub:
        axes[j],axes[n+j]=axes[n+j],axes[j]
    p=rho.reshape((2,)*(2*n)).transpose(axes).reshape((2**n,2**n))
    ev=np.linalg.eigvalsh(p)
    return float(-ev[ev<0].sum())

def ell(v):
    return 2*math.atanh(v)

def gain(v):
    return math.log(2*v/math.sqrt(1-v*v))

def formula(n,s,d,k):
    a=lambda v:(1+v)/2
    b=lambda v:(1-v)/2
    p=(a(s)*b(s))**((n-1)/2)*math.sqrt(a(d)*b(d))
    r=n-1-2*k
    return p/2*max(0.0,math.exp((n-1)*gain(s)+gain(d))-2*math.cosh((r*ell(s)-ell(d))/2))

def all_checks():
    runs=0; cut_tests=0
    for n in range(2,7):
        for s,d in [(0.15,0.73),(0.45,0.55),(0.8,0.63),(0.98,0.88)]:
            R=noisy_ghz(n,s,d)
            assert abs(np.trace(R)-1)<1.e-11
            assert np.linalg.eigvalsh(R).min()>-1.e-12
            for k in range(n-1):
                for bulk in itertools.combinations(range(n-1),k):
                    neg=ppt_neg(R,n,(*bulk,n-1))
                    ana=formula(n,s,d,k)
                    assert abs(neg-ana)<1.e-11,(n,s,d,k,neg,ana)
                    cut_tests+=1
            runs+=1
    star=1/math.sqrt(5)
    kap=1/(star*(1-star**2))
    for p in [0,1]:
        for d in [0.20,0.42,0.78]:
            rr=range(p,40,2)
            delta=min(abs(r*ell(star)-ell(d)) for r in rr)
            ucrit=(math.log(2*math.cosh(delta/2))-gain(d))/kap
            for u in [ucrit-2,ucrit+2]:
                errors=[]
                for n in ([399,999,2999] if p==0 else [400,1000,3000]):
                    s=star+u/n
                    kstar=min(range(n-1),key=lambda k:abs((n-1-2*k)*ell(s)-ell(d)))
                    q=(n-1)*gain(s)+gain(d)
                    e=abs((n-1-2*kstar)*ell(s)-ell(d))
                    actual=max(0.,math.exp(q)-2*math.cosh(e/2))
                    predicted=max(0.,math.exp(kap*u+gain(d))-2*math.cosh(delta/2))
                    errors.append(abs(actual-predicted))
                assert errors[-1]/max(1.,predicted)<0.008,(n,d,u,errors,predicted)
    for n,j,s in [(7,1,.75),(8,2,.70),(9,3,.75),(10,4,.77)]:
        d=math.tanh(j*math.atanh(s))
        choices=[(k,abs((n-1-2*k)*ell(s)-ell(d))) for k in range(n-1)]
        m=min(q for k,q in choices)
        winner=[k for k,q in choices if abs(q-m)<1.e-11]
        assert len(winner)==2,(n,j,winner)
        vals=[formula(n,s,d,k) for k in winner]
        assert vals[0]>0 and abs(vals[0]-vals[1])<1.e-11
        for delta in [-1.e-4,+1.e-4]:
            shifted=math.tanh((j+delta)*math.atanh(s))
            choices2=[(k,abs((n-1-2*k)*ell(s)-ell(shifted))) for k in range(n-1)]
            mn=min(q for k,q in choices2)
            assert sum(abs(q-mn)<1.e-10 for k,q in choices2)==1
    print(f'VERIFY_OK channel_states={runs} partial_transposes={cut_tests} critical_parities=2 critical_sequences=12 resonance_cases=4')
if __name__=='__main__':
    all_checks()
