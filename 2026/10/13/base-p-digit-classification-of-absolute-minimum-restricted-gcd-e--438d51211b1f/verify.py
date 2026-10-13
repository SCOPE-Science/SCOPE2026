from math import prod

def digits(n,p,r=None):
    ds=[]
    while n:
        ds.append(n%p); n//=p
    if not ds: ds=[0]
    if r is not None: ds += [0]*(r-len(ds))
    return ds

def carry_count_double(m,p):
    ds=digits(m,p)
    c=0; carry=0
    for d in ds:
        s=2*d+carry
        carry=1 if s>=p else 0
        c+=carry
    return c

def criterion(m,p):
    ds=digits(m,p)
    if 2*ds[0] < p: return False
    return all(2*d+1>=p for d in ds[1:])

def rlen(m,p):
    r=1; q=p
    while not m<q:
        r+=1; q*=p
    return r

primes=[2,3,5,7,11,13]
checks=0
for p in primes:
    for r in range(1,6):
        lo=1 if r==1 else p**(r-1)
        hi=p**r
        good=0
        for m in range(max(2,lo),hi):
            if m%p==0: continue
            assert rlen(m,p)==r
            lhs=(carry_count_double(m,p)==r)
            rhs=criterion(m,p)
            assert lhs==rhs, (p,r,m,carry_count_double(m,p),digits(m,p))
            if rhs: good+=1
            checks+=1
        if p==2:
            expected=1 if (2**r-1)>=2 else 0
        else:
            expected=((p-1)//2)*(((p+1)//2)**(r-1))
        assert good==expected,(p,r,good,expected)
for p in primes:
    for a in range(1,6):
        m=p**a-1
        if m>=2:
            r=rlen(m,p)
            assert carry_count_double(m,p)==r
            assert criterion(m,p)
print(f"VERIFY_OK primes={len(primes)} r_max=5 parameters={checks} exact_counts=yes repunit_complements=yes")
