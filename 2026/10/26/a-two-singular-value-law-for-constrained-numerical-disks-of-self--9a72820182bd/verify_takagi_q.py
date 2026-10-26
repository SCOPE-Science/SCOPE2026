"""Finite-dimensional numerical corroboration of the sharp q-numerical radius formula."""
import numpy as np

def run():
    rng=np.random.default_rng(613)
    checks=0
    max_excess=0.
    for n in (3,4,6):
        for trial in range(7):
            vals=np.sort(rng.uniform(.0,3.,n))[::-1]
            # A=diag(vals) conjugation; Takagi singular values are vals.
            for q in (0.0,0.23,0.5,0.9,1.0):
                alpha=np.sqrt((1+q)/2)
                beta=np.sqrt((1-q)/2)
                x=np.zeros(n,complex);y=np.zeros(n,complex)
                x[0]=y[0]=alpha
                x[1]=1j*beta;y[1]=-1j*beta
                assert np.isclose(np.vdot(x,y),q,atol=1e-12)
                predicted=(1+q)*vals[0]/2+(1-q)*vals[1]/2
                assert np.isclose(abs(np.dot(x*vals,y)),predicted,atol=1e-12)
                for _ in range(100):
                    a=rng.normal(size=n)+1j*rng.normal(size=n)
                    a/=np.linalg.norm(a)
                    b=rng.normal(size=n)+1j*rng.normal(size=n)
                    b-=np.vdot(a,b)*a
                    b/=np.linalg.norm(b)
                    y=q*a+np.sqrt(1-q*q)*b
                    value=abs(np.dot(a*vals,y))
                    max_excess=max(max_excess,value-predicted)
                    assert value<=predicted+1e-9,(n,q,value,predicted)
                    checks+=1
    print('PASS finite trials',checks,'max_excess',max_excess)
if __name__=='__main__':run()
