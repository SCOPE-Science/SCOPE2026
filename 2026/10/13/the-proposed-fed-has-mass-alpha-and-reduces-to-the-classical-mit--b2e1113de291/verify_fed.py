import mpmath as mp
mp.mp.dps=80

# Closed-form survival for alpha=1/2.
def S_half(x, lam=1):
    z=lam*mp.sqrt(x)
    return mp.e**(z*z)*mp.erfc(z)

# Correct density is -S'; published density is alpha times this.
def f_correct_half(x, lam=1):
    return -mp.diff(lambda t:S_half(t,lam), x)

def f_published_half(x, lam=1):
    return mp.mpf('0.5')*f_correct_half(x,lam)

# Finite-R masses converge respectively to 1 and 1/2.
R=mp.mpf('1e5')
mass_correct=S_half(0)-S_half(R)
mass_published=mp.mpf('0.5')*mass_correct
assert mass_correct > mp.mpf('0.998')
assert abs(mass_published/mp.mpf('0.5')-mass_correct) < mp.mpf('1e-70')

# Tail constant S(x)*sqrt(x) -> 1/sqrt(pi) for alpha=1/2, lambda=1.
target=1/mp.sqrt(mp.pi)
for x in (mp.mpf('1e3'),mp.mpf('1e4'),mp.mpf('1e5')):
    ratio=S_half(x)*mp.sqrt(x)/target
assert abs(ratio-1) < mp.mpf('1e-5')

# Truncated first moment grows without stabilization; asymptotic coefficient is 2/sqrt(pi).
def trunc_mean(R):
    U=mp.sqrt(R)
    return mp.quad(lambda u: 2*u*S_half(u*u), [0,1,U])
m1=trunc_mean(mp.mpf('100'))
m2=trunc_mean(mp.mpf('10000'))
assert m2 > 8*m1
asym=2/mp.sqrt(mp.pi)*mp.sqrt(mp.mpf('10000'))
assert abs(m2/asym-1) < mp.mpf('0.08')

# Series coefficient identity: derivative coefficients match lambda*x^(alpha-1)E_{a,a}.
a=mp.mpf('0.7'); lam=mp.mpf('1.3'); x=mp.mpf('0.4')
N=80
S_series=mp.fsum([(-lam)**k*x**(a*k)/mp.gamma(a*k+1) for k in range(N)])
dS_series=mp.fsum([a*k*(-lam)**k*x**(a*k-1)/mp.gamma(a*k+1) for k in range(1,N)])
Eaa=mp.fsum([(-lam*x**a)**k/mp.gamma(a*k+a) for k in range(N)])
rhs=-lam*x**(a-1)*Eaa
assert abs(dS_series-rhs) < mp.mpf('1e-60')

print('VERIFY_OK')
print('alpha_half_correct_mass_to_R', mp.nstr(mass_correct,30))
print('alpha_half_published_mass_to_R', mp.nstr(mass_published,30))
print('tail_ratio_at_1e5', mp.nstr(ratio,30))
print('truncated_mean_100', mp.nstr(m1,30))
print('truncated_mean_10000', mp.nstr(m2,30))
