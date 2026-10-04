from math import isqrt

def primes_below(n):
    ps=[]
    for x in range(2,n):
        ok=True
        for p in ps:
            if p*p>x: break
            if x%p==0:
                ok=False; break
        if ok: ps.append(x)
    return ps

def sigma_bi_pp(p,a):
    s=(p**(a+1)-1)//(p-1)
    if a%2==0:
        s-=p**(a//2)
    return s

def tau_bi_pp(a):
    return a+1 if a%2 else a

def is_biunitary_harmonic_two_pp(p,a,q,c):
    num=(p**a)*(q**c)*tau_bi_pp(a)*tau_bi_pp(c)
    den=sigma_bi_pp(p,a)*sigma_bi_pp(q,c)
    return num%den==0

def B(q,b):
    return sum(q**j for j in range(2*b+1) if j!=b)

for p in primes_below(80):
    for q in primes_below(80):
        if p==q: continue
        for t in range(1,5):
            b=2**t
            A=(p+1)*(p*p+1)
            bb=B(q,b)
            assert sigma_bi_pp(p,3)==A
            assert sigma_bi_pp(q,2*b)==bb
            num=(p**3)*(q**(2*b))*4*(2*b)
            den=A*bb
            assert is_biunitary_harmonic_two_pp(p,3,q,2*b)==(num%den==0)

ps=primes_below(2000)
for t in range(1,6):
    b=2**t
    for p in ps:
        for q in ps:
            if p==q: continue
            assert not is_biunitary_harmonic_two_pp(p,3,q,2*b), (p,q,t)

for t in range(1,12):
    b=2**t
    bb=B(5,b)
    assert bb > 5**(2*b)
    assert 5**(2*b) > 216*b
    assert bb > 216*b

print("VERIFY_OK")
