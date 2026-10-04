#!/usr/bin/env python3
import math

TABLE=[
(0.1,1.13105,0.00161554),(0.2,1.12029,0.00654425),(0.3,1.10193,0.0150472),
(0.4,1.07525,0.0276166),(0.5,1.03904,0.045085),(0.6,0.991262,0.068864),
(0.7,0.928278,0.101495),(0.8,0.842666,0.148196),(0.9,0.714112,0.223103)]

def threshold_x(eta):
    def f(x): return math.sinh(x)-math.cosh(eta*x)
    lo,hi=0.0,1.0
    while f(hi)<=0: hi*=2
    for _ in range(100):
        mid=(lo+hi)/2
        if f(mid)>0: hi=mid
        else: lo=mid
    return (lo+hi)/2

def lambertw(z):
    w=math.log(z)-math.log(max(1.0,math.log(z)))
    for _ in range(30):
        ew=math.exp(w); f=w*ew-z
        den=ew*(w+1)-((w+2)*f)/(2*w+2)
        nw=w-f/den
        if abs(nw-w)<1e-15*max(1.0,abs(nw)): return nw
        w=nw
    return w

def fidelity(x,eta):
    return (math.cosh(eta*x)+2*math.cosh(x)+math.sinh(x))/(3*(math.cosh(eta*x)+math.cosh(x)))

def concurrence(x,eta):
    return max((math.sinh(x)-1)/(math.cosh(eta*x)+math.cosh(x)),0.0)

def main():
    rows=0; identities=0
    for eta,Ttab,Ctab in TABLE:
        x=threshold_x(eta); T=1/x; C=concurrence(x,eta)
        assert abs(T-Ttab)<6e-6
        assert abs(C-Ctab)<8e-7
        assert abs(fidelity(x,eta)-2/3)<2e-14
        assert abs(math.tanh((1-eta)*x/2)-math.exp(-(1+eta)*x))<2e-14
        assert abs(C-(0.5-math.exp(-x)-0.5*math.exp(-2*x)))<2e-14
        rows+=1; identities+=3

    vals=[]
    for eta in (0.99,0.999,0.9999,0.99999):
        d=1-eta; x=threshold_x(eta)
        W1=lambertw(2*(1+eta)/d)
        tr=(1/x)/((1+eta)/W1)
        C=concurrence(x,eta)
        W2=lambertw(4/d)
        gr=(0.5-C)/(0.5*math.sqrt(d*W2))
        vals.append((tr,gr))
    assert abs(vals[-1][0]-1)<abs(vals[0][0]-1)
    assert abs(vals[-1][1]-1)<abs(vals[0][1]-1)
    assert abs(vals[-1][0]-1)<1e-7
    assert abs(vals[-1][1]-1)<0.005
    print("VERIFY_OK")
    print("published_table_rows =",rows)
    print("exact_identity_checks =",identities)
    print("endpoint_temperature_ratio =",vals[-1][0])
    print("endpoint_concurrence_gap_ratio =",vals[-1][1])

if __name__=="__main__":
    main()
