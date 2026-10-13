from mpmath import mp
mp.dps = 60

def a(r,n):
    x = r/(n+r+1)
    return mp.betainc(r,n+1,0,x,regularized=True)

def P(r,N):
    return mp.gamma(N+r+1)/(mp.gamma(r)*mp.gamma(N+1))*r**r*N**N/(N+r)**(N+r+1)

def H(r,N):
    f=lambda t:(1+t/N)**N/(1+t/(N+r))**(N+r+1)
    return 1-mp.quad(f,[0,1])

shapes=[mp.mpf('0.01'),mp.mpf('0.2'),mp.mpf('1'),mp.mpf('2.5'),mp.mpf('10'),mp.mpf('100')]
for r in shapes:
    last=None
    for N in range(1,41):
        d=a(r,N)-a(r,N-1)
        fac=P(r,N)*H(r,N)
        assert abs(d-fac) < mp.mpf('1e-45') + mp.mpf('1e-38')*abs(d)
        assert d > 0
        if last is not None:
            assert d < last
        last=d
print('VERIFY_OK shapes=6 increments_per_shape=40 factorization=matched concavity=strict')
