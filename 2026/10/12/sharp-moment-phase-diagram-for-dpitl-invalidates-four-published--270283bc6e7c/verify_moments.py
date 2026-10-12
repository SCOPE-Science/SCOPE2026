import math

def survival(n, kappa, eta):
    if n == 0:
        return 1.0
    x = float(n) ** eta
    return ((1.0 + 2.0*x) / ((1.0+x)**2)) ** kappa

def pmf(n, kappa, eta):
    return survival(n,kappa,eta) - survival(n+1,kappa,eta)

# Exact asymptotic constants at a large n. The eta=0.5 case converges slowly.
for kappa, eta in [(1.5,0.5),(1.5,1.5),(2.5,0.5),(2.5,1.5)]:
    a = kappa*eta
    n = 1_000_000
    rs = (n**a)*survival(n,kappa,eta)
    rp = (n**(a+1))*pmf(n,kappa,eta)
    target_s = 2.0**kappa
    target_p = (2.0**kappa)*a
    assert abs(rs/target_s - 1.0) < 0.005, (kappa,eta,rs,target_s)
    assert abs(rp/target_p - 1.0) < 0.03, (kappa,eta,rp,target_p)

# Partial moments: a row with a=0.75 has a growing first-moment tail,
# whereas a=4.5 has rapidly shrinking first-fourth-moment tails.
def block_moment(kappa,eta,r,N0,N1):
    return sum((n**r)*pmf(n,kappa,eta) for n in range(N0,N1))

bad1 = block_moment(1.5,0.5,1,20_000,40_000)
bad2 = block_moment(1.5,0.5,1,40_000,80_000)
assert bad2 > 0.8*bad1  # blocks do not die at a summable geometric rate

good1 = block_moment(1.5,3.0,4,2_000,4_000)
good2 = block_moment(1.5,3.0,4,4_000,8_000)
assert good2 < good1

# Positive-MGF summands eventually increase on log scale.
kappa,eta,t = 2.5,3.0,0.01
def log_pmf_asym(n):
    a=kappa*eta
    return math.log((2.0**kappa)*a) -(a+1.0)*math.log(n)
assert t*100000 + log_pmf_asym(100000) > t*50000 + log_pmf_asym(50000)

print("VERIFY_OK")
