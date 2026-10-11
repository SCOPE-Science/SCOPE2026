from fractions import Fraction
import random, math

def bound(N):
    return Fraction(N-2,1)+Fraction(1,N-1)

def witness_ratio(N):
    vals=[N-1]+[-1]*(N-1)
    s2=sum(v*v for v in vals)
    s4=sum(v**4 for v in vals)
    return Fraction(N*s4, s2*s2)

for N in range(4,101):
    assert witness_ratio(N)==bound(N)
    q=Fraction(N*N-3*N+3, N*(N-1))
    assert N*q==bound(N)

rng=random.Random(43146)
random_checks=0
for N in range(4,21):
    B=float(bound(N))
    for _ in range(500):
        z=[complex(rng.uniform(-1,1),rng.uniform(-1,1)) for _ in range(N-1)]
        z.append(-sum(z))
        s2=sum(abs(w)**2 for w in z)
        if s2==0: continue
        ratio=N*sum(abs(w)**4 for w in z)/(s2*s2)
        assert ratio <= B+2e-12
        random_checks+=1

def q_boundary(y):
    return (1+sum(t**4 for t in y))/(1+sum(t*t for t in y))**2

smooth_checks=0
for k in range(3,10):
    for _ in range(500):
        y=[rng.random() for _ in range(k)]
        s=sum(y); y=[t/s for t in y]
        i,j=rng.sample(range(k),2)
        q0=q_boundary(y)
        a=(y[i]+y[j])/2
        z=y[:]; z[i]=a; z[j]=a
        q1=q_boundary(z)
        assert q1+2e-14>=q0
        smooth_checks+=1
print(f'VERIFY_OK exact_orders=97 random_vectors={random_checks} smoothing_checks={smooth_checks}')
