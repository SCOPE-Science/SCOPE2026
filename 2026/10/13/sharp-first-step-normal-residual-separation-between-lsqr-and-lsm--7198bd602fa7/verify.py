from fractions import Fraction as F

def dot(x,y):
    return sum(a*b for a,b in zip(x,y))

def normal_step(k):
    # A=diag(1,k), b=(k,1/k), hence g=(k,1), B=diag(1,k^2).
    g=[k,F(1)]
    Bg=[k,k*k]
    B2g=[k,k**4]
    s0=dot(g,g)
    s1=dot(g,Bg)
    s2=dot(g,B2g)
    tq=s0/s1
    tm=s1/s2
    qQ=[g[i]-tq*Bg[i] for i in range(2)]
    qM=[g[i]-tm*Bg[i] for i in range(2)]
    qQ2=dot(qQ,qQ)
    qM2=dot(qM,qM)
    assert qM2>0
    # Exact instance-wise ratio squared.
    assert qQ2/qM2 == s0*s2/(s1*s1)
    # Equality-family sharp factor squared.
    K2=((k*k+1)/(2*k))**2
    assert qQ2/qM2 == K2
    # Relative-to-initial normal residual formulas.
    assert qQ2/s0 == ((k*k-1)/(2*k))**2
    assert qM2/s0 == ((k*k-1)/(k*k+1))**2
    return tq,tm,qQ2/s0,qM2/s0,qQ2/qM2

for k in map(F,[2,3,4,7]):
    normal_step(k)

tq,tm,rq2,rm2,cross2=normal_step(F(3))
assert tq==F(5,9)
assert tm==F(1,5)
assert rq2==F(16,9)
assert rm2==F(16,25)
assert cross2==F(25,9)

print('VERIFY_OK')
print('kappa3_t_lsqr',tq)
print('kappa3_t_lsmr',tm)
print('kappa3_lsqr_normal_ratio_sq',rq2)
print('kappa3_lsmr_normal_ratio_sq',rm2)
print('kappa3_cross_ratio_sq',cross2)
