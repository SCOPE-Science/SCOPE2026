import mpmath as mp

mp.mp.dps = 80

def moment_integral(alpha, beta, p, r):
    alpha=mp.mpf(alpha); beta=mp.mpf(beta); p=mp.mpf(p); r=mp.mpf(r)
    def integrand(y):
        e = mp.e**(-alpha*y**beta)
        return (1-p)*alpha*beta*y**(beta-1)*mp.e**(-r*y)*e/(1-p+p*e)**2
    return mp.quad(integrand, [0,1,mp.inf])

def moment_beta1(alpha,p,r):
    alpha=mp.mpf(alpha); p=mp.mpf(p); r=mp.mpf(r)
    a = 1+r/alpha
    return mp.hyp2f1(2,a,a+1,-p/(1-p))/((1-p)*a)

def printed_59_alpha_beta_1(p, N):
    p=mp.mpf(p)
    # At alpha=beta=r=1, the inner finite sum is H_{i+1}/(i+1).
    return (1-p)*mp.fsum((p**i)*mp.harmonic(i+1) for i in range(N))

p=mp.mpf("0.5")
exact = moment_integral(1,1,p,1)
elementary = 2*mp.log(2)-1
assert abs(exact-elementary) < mp.mpf("1e-60")

printed = printed_59_alpha_beta_1(p, 500)
printed_exact = 2*mp.log(2)
assert abs(printed-printed_exact) < mp.mpf("1e-60")
assert printed > 1
assert abs(printed-exact-1) < mp.mpf("1e-60")

for alpha,pv,r in [
    ("0.8","0.2","0.7"),
    ("2.0","0.5","1.0"),
    ("3.5","0.8","2.3"),
]:
    direct=moment_integral(alpha,1,pv,r)
    closed=moment_beta1(alpha,pv,r)
    assert abs(direct-closed) < mp.mpf("1e-55")

table_case = moment_beta1(2,mp.mpf("0.5"),1)
assert abs(table_case-(mp.pi/2-1)) < mp.mpf("1e-60")
assert abs(table_case-mp.mpf("0.5708")) < mp.mpf("0.00001")

print("VERIFY_OK")
print("exact_counterexample_mean", mp.nstr(exact,30))
print("printed_eq_5_9_value", mp.nstr(printed,30))
print("table_case_exact", mp.nstr(table_case,30))
