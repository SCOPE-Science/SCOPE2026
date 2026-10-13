LIMIT=2_000_000

def sieve_spf(n):
    spf=list(range(n+1))
    if n>=1: spf[1]=1
    for i in range(2,int(n**0.5)+1):
        if spf[i]==i:
            for j in range(i*i,n+1,i):
                if spf[j]==j: spf[j]=i
    return spf

def factor(n, spf):
    out=[]
    while n>1:
        p=spf[n]; e=0
        while n%p==0:
            n//=p; e+=1
        out.append((p,e))
    return out

def beta_pp(p,a):
    return (p**(a+1)+(-1)**a)//(p+1)

def beta_from_factor(f):
    z=1
    for p,a in f: z*=beta_pp(p,a)
    return z

spf=sieve_spf(LIMIT)
hits=[]; tested=0
for n in range(4,LIMIT+1):
    f=factor(n,spf)
    if len(f)<=2 and not (len(f)==1 and f[0][1]==1):
        tested += 1
        b=beta_from_factor(f)
        if (n-1)%b==0:
            hits.append(n)
assert hits==[4], hits[:20]

# Directly stress the prime-power inequalities and parity facts used in proof.
primes=[p for p in range(2,5000) if spf[p]==p]
lemma_checks=0
for p in primes:
    for a in range(1,13):
        b=beta_pp(p,a)
        assert 0 < b < p**a
        assert b >= p**(a-1)*(p-1)
        assert (b == p**(a-1)*(p-1)) == (a==1)
        if p==2: assert b%2==1
        if p%2==1: assert (b%2==1) == (a%2==0)
        lemma_checks += 1

print('VERIFY_OK', f'limit={LIMIT}', f'tested_low_support_composites={tested}', f'hits={hits}', f'lemma_checks={lemma_checks}')
