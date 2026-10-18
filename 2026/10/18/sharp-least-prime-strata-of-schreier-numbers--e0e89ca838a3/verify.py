"""Independent finite checks for least-prime Schreier layers (standard Python only)."""
import math

LIMIT = 250000
spf = list(range(LIMIT+1))
spf[1] = 1
for k in range(2,math.isqrt(LIMIT)+1):
    if spf[k]==k:
        for j in range(k*k,LIMIT+1,k):
            if spf[j]==j: spf[j]=k

def factor(n):
    z=[]
    while n>1:
        p=spf[n]
        a=0
        while n%p==0:
            n//=p;a+=1
        z.append((p,a))
    return z

def is_schreier_direct(n):
    ds=[d for d in range(2,math.isqrt(n)+1) if n%d==0]
    return not ds or min(ds)>=len(ds)

def is_schreier_divisor_count(n,fs):
    if not fs: return True
    p=fs[0][0]
    tau=math.prod(a+1 for _,a in fs)
    return tau<=2*p+(1 if math.isqrt(n)**2==n else 2)

primes=(2,3,5,7,11,13,17,23)
observed={p:0 for p in primes}
main={p:0 for p in primes}
for n in range(2,LIMIT+1):
    fs=factor(n)
    direct=is_schreier_direct(n)
    divisor=is_schreier_divisor_count(n,fs)
    assert direct==divisor,(n,fs,direct,divisor)
    p=fs[0][0]
    if p not in observed: continue
    if direct: observed[p]+=1
    u=(p+1).bit_length()-1
    E=(p+1)//(1<<(u-1))-1
    primary= (len(fs)==u+1 and 1<=fs[0][1]<=E and all(a==1 for _,a in fs[1:]))
    if primary:
        assert direct,(n,fs,'not actually Schreier')
        main[p]+=1
for p in primes:
    u=(p+1).bit_length()-1
    E=(p+1)//(1<<(u-1))-1
    K=sum(1/p**e for e in range(1,E+1))
    asym=K*LIMIT*math.log(math.log(LIMIT))**(u-1)/(math.factorial(u-1)*math.log(LIMIT))
    print(f'p={p:2} u={u} E={E} K={K:.10f} exact={observed[p]:6} principal={main[p]:6} predicted={asym:9.1f} ratio={observed[p]/asym:.5f}')
print('OK: exhaustive independent small-divisor and tau checks n=2..',LIMIT)
