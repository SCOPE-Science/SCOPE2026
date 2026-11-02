"""Independent finite-grid stress test of a periodic linear orbital heating proxy.
No finite test is a proof of the all-parameter theorem.
"""
import numpy as np

def forcing(e, N=32768):
    x=np.arange(N)*2*np.pi/N
    low=np.zeros_like(x)
    high=np.full_like(x, 2*np.pi)
    for _ in range(52):
        mid=(low+high)/2
        left=(mid-e*np.sin(mid))<x
        low=np.where(left,mid,low)
        high=np.where(left,high,mid)
    E=(low+high)/2
    f=(1-e*np.cos(E))**-2
    return x, f

def filter_out(f,tau):
    N=len(f)
    k=np.fft.rfftfreq(N,d=1/N)
    return np.fft.irfft(np.fft.rfft(f)/(1+1j*k*tau), n=N)

def peak_time(x,y):
    N=len(x); j=np.argmax(y)
    # quadratic subgrid peak
    ym,y0,yp=y[(j-1)%N],y[j],y[(j+1)%N]
    den=ym-2*y0+yp
    d=(ym-yp)/(2*den) if abs(den)>1e-24 else 0
    return (j+d)*2*np.pi/N

def bound(e):
    E0=np.arccos((1-(1-e*e)**.25)/e)
    return E0-e*np.sin(E0)

for e in [0.1,0.5,0.9,0.99]:
    x,f=forcing(e, N=131072 if e>.95 else 32768)
    ts=[]
    for tau in [0.002,0.01,0.05,0.2,1,5,30,150]:
        y=filter_out(f,tau)
        ts.append(peak_time(x,y))
        k=np.fft.rfftfreq(len(f),d=1/len(f))
        dydx=np.fft.irfft(np.fft.rfft(y)*(1j*k),n=len(f))
        residual=np.max(np.abs(dydx-(f-y)/tau))/max(1,np.max(np.abs((f-y)/tau)))
        assert residual<3e-4,(e,tau,residual)
    assert all(a<b for a,b in zip(ts,ts[1:])),(e,ts)
    assert 0<ts[0]<ts[-1]<bound(e)<np.pi/2,(e,ts,bound(e))
    assert abs(ts[-1]-bound(e))<.11
    print('e=',e,'bound=',round(bound(e),10),'peaks=',[round(t,10) for t in ts])
print('NUMERICAL STRESS TEST PASSED')
