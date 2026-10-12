import math


def simulate(d, lam, eta, r0, n=20):
    c=eta*math.sqrt(d)
    x=r0
    R=abs(x)
    out=[x]
    for _ in range(n):
        mult=1-c/R
        x=mult*x
        out.append(x)
        R=max(R,abs(x))
    return c,out

for d in (1,2,7,64):
    for lam in (0.2,1.0,9.0):
        for r0 in (0.3,1.0,5.0):
            # lambda cancels from the exact normalized recurrence.
            for z in (0.2,0.8,1.0,1.4,1.9):
                eta=z*r0/math.sqrt(d)
                c,x=simulate(d,lam,eta,r0,12)
                for t,val in enumerate(x):
                    closed=(1-z)**t*r0
                    assert abs(val-closed)<2e-12*max(1.0,abs(closed))
            z=2.0
            eta=z*r0/math.sqrt(d)
            c,x=simulate(d,lam,eta,r0,12)
            for t,val in enumerate(x):
                assert abs(val-((-1)**t)*r0)<2e-12*max(1.0,r0)
            for z in (2.01,2.2,3.0,10.0,100.0):
                eta=z*r0/math.sqrt(d)
                c,x=simulate(d,lam,eta,r0,12)
                A=z-1.0
                assert abs(x[1]+A*r0)<3e-12*max(1.0,A*r0)
                assert abs(x[2]-r0)<3e-12*max(1.0,r0)
                for t in range(1,len(x)):
                    closed=((-1)**t)*(A**(2-t))*r0
                    assert abs(x[t]-closed)<5e-11*max(1.0,abs(closed))
                q=1/A
                assert abs(A*q-1.0)<1e-15
                assert abs((x[1]*x[1])/(r0*r0)-A*A)<5e-12*max(1.0,A*A)
                assert abs((x[3]*x[3])/(x[2]*x[2])-q*q)<5e-12

print('verification passed')
