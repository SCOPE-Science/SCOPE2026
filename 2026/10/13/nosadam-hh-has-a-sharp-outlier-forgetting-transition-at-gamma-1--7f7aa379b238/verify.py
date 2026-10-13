import math

def direct(gamma, G, H, tau, T):
    B=0.0
    v=0.0
    out={}
    for t in range(1,T+1):
        b=t**(-gamma)
        Bn=B+b
        beta=B/Bn
        q=H*H if t==tau else G*G
        v=beta*v+(1-beta)*q
        B=Bn
        if t in (tau,T):
            out[t]=(B,v)
    return out

def closed(gamma,G,H,tau,t):
    B=sum(k**(-gamma) for k in range(1,t+1))
    return B, G*G+(H*H-G*G)*(tau**(-gamma))/B

for gamma in (0.0,0.1,0.7,1.0,1.3,2.0):
    G,H,tau,T=2.0,11.0,7,5000
    d=direct(gamma,G,H,tau,T)
    for t in (tau,T):
        B,v=closed(gamma,G,H,tau,t)
        assert abs(d[t][0]-B)<2e-10*max(1.0,B)
        assert abs(d[t][1]-v)<2e-10*max(1.0,v)

G,H,tau=2.0,11.0,7
C=(H*H-G*G)*(tau**(-0.1))
for T in (20000,100000,400000):
    B,v=direct(0.1,G,H,tau,T)[T]
    scaled=(T**0.9)*(v-G*G)
    target=0.9*C
    assert abs(scaled-target)/target < 0.08

for T in (20000,100000,400000):
    B,v=direct(1.0,G,H,tau,T)[T]
    scaled=math.log(T)*(v-G*G)
    target=(H*H-G*G)/tau
    assert abs(scaled-target)/target < 0.12

# For gamma > 1, partial sums converge and the imprint stays bounded away from zero.
vals=[]
for T in (10000,100000,500000):
    B,v=direct(1.5,G,H,tau,T)[T]
    vals.append(v-G*G)
assert vals[-1] > 0.0
assert abs(vals[-1]-vals[-2]) < 0.01*vals[-1]

# Source comparison exponent gamma=0.1: outlier normalized weight ~ 0.9 tau^-0.1 T^-0.9.
T=400000
B,_=direct(0.1,G,H,tau,T)[T]
w=(tau**(-0.1))/B
approx=0.9*(tau**(-0.1))*(T**(-0.9))
assert abs(w-approx)/approx < 0.05

# Exact denominator-rescaling behavior.
for gamma in (0.1,1.0,1.5):
    T=500000
    B,v=direct(gamma,G,H,tau,T)[T]
    R=G/math.sqrt(v)
    assert 0.0<R<1.0
    if gamma<=1.0:
        # Increasing horizon moves the rescaling back toward one.
        B2,v2=direct(gamma,G,H,tau,T//5)[T//5]
        assert R > G/math.sqrt(v2)

print("verification passed")
