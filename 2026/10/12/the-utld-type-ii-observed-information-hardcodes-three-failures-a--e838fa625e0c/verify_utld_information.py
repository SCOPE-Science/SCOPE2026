import mpmath as mp

mp.mp.dps = 80

def ell(alpha, n, r, xr, linear=mp.mpf("0.37")):
    z = xr*(2-xr)
    return r*mp.log(alpha) + (n-r)*mp.log(1-z**alpha) + linear*alpha

def hessian_correct(alpha, n, r, xr):
    z = xr*(2-xr)
    q = z**alpha
    L = mp.log(z)
    return -r/alpha**2 - (n-r)*q*L**2/(1-q)**2

def hessian_source(alpha, n, xr):
    z = xr*(2-xr)
    q = z**alpha
    L = mp.log(z)
    return (q*(6-alpha**2*(n-3)*L**2)-3*(q**2+1))/(q-1)**2

# Replay against numerical differentiation of the actual likelihood.
tests = [
    (mp.mpf("0.3"), 12, 4, mp.mpf("0.2")),
    (mp.mpf("0.5"), 10, 3, mp.mpf("0.5")),
    (mp.mpf("0.8"), 20, 17, mp.mpf("0.9")),
]
for a,n,r,x in tests:
    num = mp.diff(lambda aa: ell(aa,n,r,x), a, 2)
    clo = hessian_correct(a,n,r,x)
    assert abs(num-clo) < mp.mpf("1e-60")
    assert clo < 0

# Exact structural relationship on the accidental r=3 slice.
for a,n,x in [
    (mp.mpf("0.2"), 8, mp.mpf("0.25")),
    (mp.mpf("0.5"), 10, mp.mpf("0.5")),
    (mp.mpf("0.9"), 30, mp.mpf("0.8")),
]:
    src = hessian_source(a,n,x)
    cor = hessian_correct(a,n,3,x)
    assert abs(src-a*a*cor) < mp.mpf("1e-60")

# Source expression is independent of r; true Hessian is not.
a=mp.mpf("0.5"); n=10; x=mp.mpf("0.5")
src = hessian_source(a,n,x)
h3 = hessian_correct(a,n,3,x)
h5 = hessian_correct(a,n,5,x)
assert abs(h3-h5) > mp.mpf("1e-3")
assert abs(src-a*a*h3) < mp.mpf("1e-60")
assert abs(src-a*a*h5) > mp.mpf("1e-3")

# Concrete variance discrepancy.
true_var = -1/h3
source_var = -1/src
assert abs(true_var-mp.mpf("0.025030178468734978317")) < mp.mpf("1e-20")
assert abs(source_var-mp.mpf("0.10012071387493991327")) < mp.mpf("1e-20")
assert abs(source_var/true_var-4) < mp.mpf("1e-60")

print("VERIFY_OK")
print("correct_hessian_example", mp.nstr(h3, 40))
print("source_hessian_example", mp.nstr(src, 40))
print("correct_inverse_information", mp.nstr(true_var, 40))
print("source_inverse_information", mp.nstr(source_var, 40))
print("variance_factor", mp.nstr(source_var/true_var, 20))
