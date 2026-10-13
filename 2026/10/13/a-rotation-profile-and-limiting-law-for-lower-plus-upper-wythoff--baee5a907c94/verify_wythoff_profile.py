from decimal import Decimal, getcontext, ROUND_FLOOR
import math
getcontext().prec = 80
sqrt5 = Decimal(5).sqrt()
phi = (Decimal(1) + sqrt5) / Decimal(2)
alpha = Decimal(1) / phi
beta = Decimal(1) / (phi * phi)
N = 5000
def fl(x): return int(x.to_integral_value(rounding=ROUND_FLOOR))
lower=[]; h=1
while True:
    a=fl(Decimal(h)*phi)
    if a>N: break
    lower.append(a); h+=1
upper=[]; k=1
while True:
    b=fl(Decimal(k)*phi*phi)
    if b>N: break
    upper.append(b); k+=1
r=[0]*(N+1)
for a in lower:
    for b in upper:
        s=a+b
        if s>N: break
        r[s]+=1
oeis77=[0,0,1,0,1,2,0,3,1,2,4,0,4,4,1,6,2,4,7,0,8,4,4,9,1,8,8,2,11,4,7,12,0,12,9,4,14,4,10,14,1,16,8,8,17,2,15,14,4,19,7,12,20,0,21,12,9,22,4,18,19,4,24,10,14,25,1,24,18,8,27,8,19,26,2,29,15]
assert r[1:78]==oeis77
def frac(x): return x-Decimal(fl(x))
def lam(t):
    if t<beta: return beta-t
    if t<2*beta: return t-beta
    return beta
max_abs=Decimal(0); max_scaled=Decimal(0); argmax=None
mean=Decimal(0); summ=0
for n in range(2,N+1):
    model=Decimal(n)*lam(frac(Decimal(n)*alpha))
    err=abs(Decimal(r[n])-model)
    if err>max_abs: max_abs=err; argmax=n
    sc=err/Decimal(str(math.log(n+2)))
    if sc>max_scaled: max_scaled=sc
    mean += Decimal(r[n])/Decimal(n)
    summ += r[n]
mean /= Decimal(N-1)
target_mean=Decimal(1)/(phi**3)
summ_norm=Decimal(summ)/Decimal(N*N)
target_summ=target_mean/Decimal(2)
print("VERIFY_OK oeis_prefix=77 n_max=%d" % N)
print("max_abs_profile_error=%s argmax=%s max_error_over_log=%s" % (format(max_abs,".12f"),argmax,format(max_scaled,".12f")))
print("mean_r_over_n=%s target=%s" % (format(mean,".12f"),format(target_mean,".12f")))
print("summatory_over_n2=%s target=%s" % (format(summ_norm,".12f"),format(target_summ,".12f")))
