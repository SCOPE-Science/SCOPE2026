import math
import random

def closed_m(t,b1,G):
    a=(1.0-b1)/(1.0+b1)
    return ((-1.0)**(t-1))*a*G*(1.0-(-b1)**t)

def closed_r(t,b1,G):
    a=(1.0-b1)/(1.0+b1)
    c=2.0*b1/(1.0+b1)
    return ((-1.0)**(t-1))*G*(c+a*(-b1)**t)

def replay(b1,b2,G,T):
    m=0.0
    s=0.0
    rows=[]
    for t in range(1,T+1):
        g=G if t%2 else -G
        denom_state=s
        m=b1*m+(1.0-b1)*g
        r=g-m
        s=b2*s+(1.0-b2)*r*r
        rows.append((t,g,m,r,denom_state,s))
    return rows

random.seed(350066)

# Exact first moment, residual, and unrolled centered state.
for _ in range(500):
    b1=random.uniform(0.01,0.99)
    b2=random.uniform(0.0,0.999)
    G=random.choice((-1.0,1.0))*10.0**random.uniform(-2.0,2.0)
    rows=replay(b1,b2,G,80)
    for t,g,m,r,den_old,s in rows:
        assert abs(m-closed_m(t,b1,G)) <= 3e-12*max(1.0,abs(G))
        assert abs(r-closed_r(t,b1,G)) <= 3e-12*max(1.0,abs(G))
        exact=(1.0-b2)*G*G*sum(
            (b2**(t-j))*(
                2.0*b1/(1.0+b1)
                +(1.0-b1)/(1.0+b1)*((-b1)**j)
            )**2
            for j in range(1,t+1)
        )
        assert abs(s-exact) <= 2e-10*max(1.0,abs(exact))

# Asymptotic denominator floor for varied beta2.
for b1 in (0.1,0.5,0.9,0.99):
    c=2.0*b1/(1.0+b1)
    for b2 in (0.0,0.5,0.9,0.99,0.999):
        G=2.3
        rows=replay(b1,b2,G,200000 if b2>=0.999 else 20000)
        s=rows[-1][-1]
        assert abs(math.sqrt(s)/(abs(G))-c) < 3e-7

# Matched uncentered state and gain ratio.
for b1 in (0.1,0.2,0.5,0.9):
    c=2.0*b1/(1.0+b1)
    for eps in (0.0,1e-8,0.01,1.0):
        G=3.0
        Uac=G/(c*G+eps)
        Uunc=G/(G+eps)
        ratio=Uac/Uunc
        closed=(G+eps)/(c*G+eps)
        assert abs(ratio-closed) < 1e-14
        if eps==0.0:
            assert abs(ratio-(1.0+b1)/(2.0*b1)) < 1e-14

# Stated high-signal examples.
assert abs((1.0+0.9)/(2.0*0.9)-19.0/18.0) < 1e-15
assert abs((1.0+0.5)/(2.0*0.5)-1.5) < 1e-15
assert abs((1.0+0.1)/(2.0*0.1)-5.5) < 1e-15

# Direct long-run update ratio with positive damping.
b1=0.5
b2=0.999
G=4.0
eps=1e-3
rows=replay(b1,b2,G,200000)
s_old=rows[-1][4]
Uac=G/(math.sqrt(s_old)+eps)
v=G*G*(1.0-b2**199999)
Uunc=G/(math.sqrt(v)+eps)
expected=(G+eps)/(2.0*b1/(1.0+b1)*G+eps)
assert abs(Uac/Uunc-expected) < 2e-6

print("verification passed")
