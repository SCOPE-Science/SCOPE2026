import math

def replay(m,t0,beta,gamma,eta,omega,r0,n=200000):
    q=(2*(t0-1)+m)/(2*t0+m)
    assert (1+beta)*gamma/2 <= q + 1e-15
    t=t0; r=r0
    for k in range(n):
        tn=(m+math.sqrt(m*m+4*t*t))/2
        A=(tn-m)/(tn-1)
        B=2*(tn-1)/((1+beta)*gamma*tn)
        C=(1-omega)/(2/B+1/(beta*gamma*(1-eta)*A))
        r=min(A*r,B*r,C)
        t=tn
    cinf=(1-omega)/((1+beta)*gamma+1/(beta*gamma*(1-eta)))
    return r,cinf,q

cases=[
    (0.8,1.0,1.0,0.15,0.0,0.0,1.0),
    (0.5,2.0,0.8,0.3,0.2,0.1,3.0),
    (0.9,5.0,2.0,0.2,0.0,0.3,1.0),
    (0.2,1.0,1.0,0.05,0.0,0.0,1e-6),
]
for c in cases:
    r,cinf,q=replay(*c)
    assert abs(r-cinf) < 3e-5, (r,cinf,q)
    assert cinf < 0.5

# Grid check of transformed-parameter envelope.
for q in (0.2,0.4,0.5,0.7,0.9):
    best=0.0
    for i in range(1,1000):
        x=2*q*i/1000
        for j in range(i+1,1001,20):
            y=2*q*j/1000
            if x<y<=2*q:
                best=max(best,1/(y+1/x))
    env=2*q/(1+4*q*q) if q<=0.5 else 0.5
    assert best < env + 1e-12
    assert env-best < 0.02

# t0=1 uniform envelope tends to 6/13 from below as m -> 1.
for m in (0.2,0.5,0.9,0.999):
    q=m/(2+m)
    env=2*q/(1+4*q*q)
    assert env < 6/13
assert abs((2*(1/3))/(1+4/9)-6/13) < 1e-15
print('VERIFY_OK')
