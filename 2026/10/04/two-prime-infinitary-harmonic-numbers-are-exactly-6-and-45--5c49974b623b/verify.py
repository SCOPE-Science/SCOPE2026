from fractions import Fraction

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

def factor(n):
    out=[]
    d=2
    while d*d<=n:
        if n%d==0:
            e=0
            while n%d==0:
                n//=d; e+=1
            out.append((d,e))
        d += 1 if d==2 else 2
    if n>1: out.append((n,1))
    return out

def h_inf_from_factorization(f):
    N=1; J=0; den=1
    for p,e in f:
        N*=p**e
        J+=e.bit_count()
        i=0; t=e
        while t:
            if t&1: den*=p**(1<<i)+1
            t>>=1; i+=1
    return Fraction((1<<J)*N,den)

ps=primes_below(100)
hits=[]
for ix,p in enumerate(ps):
    for q in ps[ix+1:]:
        for a in range(1,16):
            for b in range(1,16):
                h=h_inf_from_factorization([(p,a),(q,b)])
                if h.denominator==1:
                    hits.append((p,a,q,b,p**a*q**b,h.numerator))
vals=sorted({x[4] for x in hits})
assert vals==[6,45], vals
assert hits==[(2,1,3,1,6,2),(3,2,5,1,45,3)], hits
print('VERIFY_OK prime_bound=100 exponent_max=15 hits='+repr(hits))
