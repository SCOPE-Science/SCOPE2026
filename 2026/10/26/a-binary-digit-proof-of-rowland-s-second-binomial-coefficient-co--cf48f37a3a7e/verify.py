from math import comb

def primes_to(N):
    sieve=bytearray(b'\x01')*(N+1)
    sieve[:2]=b'\x00\x00'
    for d in range(2,int(N**.5)+1):
        if sieve[d]:sieve[d*d::d]=b'\x00'*len(sieve[d*d::d])
    return [i for i in range(N+1) if sieve[i]]

def original(m):
    L=m.bit_length(); z=L-m.bit_count(); val=set()
    for j in range(1<<z):
        s=0
        for i in range(1,L):
            if (m>>i)&1:
                pref=m % (1<<(i+1))
                w=(pref.bit_length()-pref.bit_count())-int(i==1)
                s+=(j>>w)<<i
        val.add((m+s)%(1<<L))
    return val

def mask(m):
    L=m.bit_length(); Q=1<<L
    return {n for n in range(Q) if (((n-1)&(m-1))==m-1)}

c1=0;c2=0;c3=0
for p in primes_to(3000):
    if p==2:continue
    m=2*p; a=original(m);b=mask(m)
    assert a==b,('original vs mask',p,a^b)
    assert len(a)==1<<(m.bit_length()-m.bit_count())
    c1+=1
    if p>197:continue
    for n in range(1,(1<<m.bit_length())+1):
        C=comb(n-1,m-1) if n>=m else 0
        n1=n//p%p
        A=(p+1)*(n1-1)*(n%p==0)
        assert (C-A)%p==0,('integer',p,n)
        E=(C-A)//p
        assert (E&1) == ((n-1)&(m-1)==m-1),('parity',p,n)
        assert ((E&1)!=0)==(n% (1<<m.bit_length()) in a)
        c2+=1
    c3+=1
print(f'VERIFY_OK: {c1} odd primes <=3000, all residues of Rowland parametrizations; '+f'{c3} odd primes <=197 and {c2} exact integer-binomial checks')
