from math import gcd

def mul(a,b,p):
    u,v=a; x,y=b
    return ((u*x-v*y)%p,(u*y+v*x-3*v*y)%p)
def ord_mu(p):
    z=(1,0)
    for i in range(1,2*p+2):
        z=mul(z,(0,1),p)
        if z==(1,0):return i
    raise ValueError(p)
def prime_factors(n):
    z=[]; d=2
    while d*d<=n:
        if n%d==0:
            z.append(d)
            while n%d==0:n//=d
        d+=1
    if n>1:z.append(n)
    return z
F=[0,1]
for i in range(800):F.append(F[-1]+F[-2])
for k in range(1,401):
    arr=[sum(F[i+j]**4 for j in range(k)) for i in range(9)]
    g=0
    for v in arr[:5]:g=gcd(g,v)
    for v in arr[5:]:assert v%g==0
    for p in prime_factors(k):
        if p<7:continue
        o=ord_mu(p)
        expected=0
        if k%o==0:
            t=k
            while t%p==0:expected+=1;t//=p
        actual=0
        t=g
        while t%p==0:actual+=1;t//=p
        assert actual==expected, (k,p,o,g,actual,expected)
    for p in prime_factors(g):
        if p>=7:
            assert k%p==0,(k,p,g)
    
print('PASS quartic prime-primary checks, lengths 1..400')
