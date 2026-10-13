import math

def u_constant_norm(diag, N, k):
    q=2**k
    return (sum(abs(z)**q for z in diag)/N)**(1.0/q)

def check(N,k,eps):
    q=2**k
    b=eps/2.0
    a=(1.0-b**q)**(1.0/q)
    scale=N**(1.0/q)
    ap=[scale*a, scale*b]+[0.0]*(N-2)
    am=[scale*a,-scale*b]+[0.0]*(N-2)
    assert abs(u_constant_norm(ap,N,k)-1.0)<1e-12
    assert abs(u_constant_norm(am,N,k)-1.0)<1e-12
    diff=[x-y for x,y in zip(ap,am)]
    mid=[(x+y)/2.0 for x,y in zip(ap,am)]
    assert abs(u_constant_norm(diff,N,k)-eps)<1e-12
    assert abs(u_constant_norm(mid,N,k)-a)<1e-12
    delta=1.0-a
    rhs=1.0-(1.0-(eps/2.0)**q)**(1.0/q)
    assert abs(delta-rhs)<1e-14

for k in range(2,7):
    # Repeated constant derivatives produce exponent 2^(k-1) on AA*.
    exp=1
    for _ in range(1,k):
        exp*=2
    assert exp==2**(k-1)
    for N in (2,3,5,8):
        for eps in (0.125,0.5,1.0,1.75,2.0):
            check(N,k,eps)
print('VERIFY_OK')
