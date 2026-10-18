from mpmath import mp, iv
mp.dps=170; iv.dps=145
lam=iv.mpf(7)/6
alpha=iv.log(iv.mpf(3)/2)/iv.log(lam)
E=mp.mpf('1e-115')
N=1000

def F(z): return z*(7-z*z)/6
def g_mp(t):
    z=t*mp.mpf(6)/7
    for j in range(12): z-= (z*(7-z*z)/6-t)/((7-3*z*z)/6)
    return z

def bounds(q):
    W=1-iv.mpf(q); L=iv.mpf(1)
    for i in range(N):
        L*=1+W/2
        W=W*(4+3*W-W**2)/6
    # Centered iteration has contraction derivative near W=0 and avoids interval dependency cancellation.
    assert W.b<iv.mpf('1e-40')
    L_lo=L.a
    L_hi=L.b*iv.exp(iv.mpf(5)*W.b)
    Z=iv.mpf(q); B=iv.mpf(1)
    for i in range(N):
        M=(mp.mpf(Z._mpi_[0])+mp.mpf(Z._mpi_[1]))/2
        z=g_mp(M)
        xlo=iv.mpf(str(z-E)); xhi=iv.mpf(str(z+E))
        # Certified monotonic inverse bounds; min F'>=2/3 on [0,1].
        assert xlo>0 and xhi<1
        assert F(xlo).b<Z.a and F(xhi).a>Z.b, (i,'inverse bracket failed')
        Z=iv.mpf([str(z-E),str(z+E)])
        B*=1-Z/3
    assert Z.b<iv.mpf('1e-40')
    # Conservative estimates using g^k(q)<=0.9^k q, and q<1/2.
    B_lo=B.a*(1-3*Z.b)
    B_hi=B.b
    H=lam**N*Z
    H_lo=H.a
    H_hi=H.b*iv.exp(Z.b**2)
    lo=L_lo*B_lo*iv.exp(alpha*iv.log(H_lo))
    hi=L_hi*B_hi*iv.exp(alpha*iv.log(H_hi))
    return lo.a,hi.b,Z.b

q1=bounds('0.45');q2=bounds('0.5')
assert q2[0]-q1[1] > iv.mpf('1.2e-24')
print('A(9/20):',q1[0],q1[1])
print('A(1/2):',q2[0],q2[1])
print('Certified lower gap:', q2[0]-q1[1])
print('VERIFY_OK')
