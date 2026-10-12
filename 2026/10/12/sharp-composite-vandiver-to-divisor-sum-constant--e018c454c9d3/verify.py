from math import prod, isqrt

LIMIT = 100000

def spf_sieve(n):
    spf=list(range(n+1))
    if n>=1: spf[1]=1
    for i in range(2,isqrt(n)+1):
        if spf[i]==i:
            for j in range(i*i,n+1,i):
                if spf[j]==j: spf[j]=i
    return spf

def factor(n,spf):
    f=[]
    while n>1:
        p=spf[n]; a=0
        while n%p==0:
            n//=p; a+=1
        f.append((p,a))
    return f

def invariants(n,spf):
    fs=factor(n,spf)
    tau=1; sigma=1
    divisors=[1]
    for p,a in fs:
        tau*=a+1
        sigma*= (p**(a+1)-1)//(p-1)
        old=divisors[:]
        divisors=[]
        q=1
        for e in range(a+1):
            divisors.extend(d*q for d in old)
            q*=p
    V=1
    for d in divisors:
        V*=d+1
    T=pow(n,tau//2) if tau%2==0 else pow(n,(tau-1)//2)*isqrt(n)
    # odd tau iff n square, so isqrt(n) exact
    return tau,sigma,V,T

spf=spf_sieve(LIMIT)
composites=0
minimum=None
minimizers=[]
aux_eq=[]
thm7_eq=[]
for n in range(4,LIMIT+1):
    fs=factor(n,spf)
    if len(fs)==1 and fs[0][1]==1:
        continue
    composites+=1
    tau,sigma,V,T=invariants(n,spf)
    assert 7*T >= 8*sigma, (n,tau,sigma,T)
    assert V >= 2*(sigma+T), (n,V,sigma,T)
    assert 7*V >= 30*sigma, (n,V,sigma)
    if 7*T == 8*sigma: aux_eq.append(n)
    if V == 2*(sigma+T): thm7_eq.append(n)
    # compare V/sigma exactly
    if minimum is None or V*minimum[1] < minimum[0]*sigma:
        minimum=(V,sigma); minimizers=[n]
    elif V*minimum[1] == minimum[0]*sigma:
        minimizers.append(n)
assert minimum == (30,7), minimum
assert minimizers == [4], minimizers
assert aux_eq == [4], aux_eq
# theorem7 equality exactly prime squares in range
for n in thm7_eq:
    r=isqrt(n); assert r*r==n and r>=2 and spf[r]==r
print('VERIFY_OK')
print(f'limit={LIMIT}')
print(f'composite_cases={composites}')
print('minimum_ratio=30/7')
print('unique_minimizer=4')
print(f'auxiliary_equality={aux_eq}')
print(f'theorem7_equality_cases={len(thm7_eq)}')
