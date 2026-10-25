"""Independent enumeration for distinct scattered abelian squares with two marked letters."""
from collections import Counter
from itertools import product

def closed_spectrum(a,b,c):
    s=a+b+c
    def choose2(r):return r*(r-1)//2 if r>=2 else 0
    def H(A,C,t):
        return choose2(t+2)-choose2(t-A+1)-choose2(t-C+1)+choose2(t-A-C)
    D={}
    for h in range(1,(s+2)//2+1):
        A=min(a,h-1);C=min(c,h-1)
        M=2*h-2-b
        val=int(2*h<=s)+(A+1)*(C+1)-H(A,C,M-1)
        if val:D[2*h]=val
    return D

def independent_spectrum(a,b,c):
    w='0'*a+'1'+'0'*b+'1'+'0'*c
    S={''}
    for t in w:S|={x+t for x in S}
    ctr=Counter()
    for x in S:
        m=len(x)
        if m>0 and m%2==0 and x[:m//2].count('1')==x[m//2:].count('1'):
            ctr[m]+=1
    return dict(ctr)

k=0
for a,b,c in product(range(7),repeat=3):
    x=closed_spectrum(a,b,c)
    y=independent_spectrum(a,b,c)
    assert x==y,(a,b,c,x,y)
    k+=1
print('SPECTRUM_CHECK',k)

# Different method for counting the two-one forms: 1D difference bands.
def difference_count(a,b,c):
    s=a+b+c
    val=s//2
    for d in range(-min(c,b),min(a,b)+1):
        i_low=max(0,d)
        i_high=min(a,c+d)
        if i_low<=i_high:
            val+=(i_high-i_low+1)*(1+(b-abs(d))//2)
    return val
for a,b,c in product(range(17),repeat=3):
    assert sum(closed_spectrum(a,b,c).values())==difference_count(a,b,c)
print('DIFFERENCE_RECONCILIATION',17**3)

# Shape under scaling; the coefficient and optimizing ratio are approximate and theorem is analytic.
for k in (1,2,3,5,10,20):
    a,b,c=2*k,3*k,2*k
    n=a+b+c+2
    f=difference_count(a,b,c)
    print('WITNESS',k,n,f,round(f/(n**3),9))
print('VERIFY_OK')
