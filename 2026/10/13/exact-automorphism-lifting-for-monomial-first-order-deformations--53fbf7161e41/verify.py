from itertools import product
from math import gcd,ceil

# Direct exact multiplication in F_p[epsilon,x]/(epsilon^2,x^n-epsilon*x^r).
def mul(A,B,p,n,r):
    a,b=A; c,d=B
    base=[0]*n; eps=[0]*n
    for i,ai in enumerate(a):
        if ai:
            for j,cj in enumerate(c):
                if cj:
                    k=i+j
                    if k<n:base[k]=(base[k]+ai*cj)%p
                    elif k-n+r<n:eps[k-n+r]=(eps[k-n+r]+ai*cj)%p
            for j,dj in enumerate(d):
                if dj and i+j<n:eps[i+j]=(eps[i+j]+ai*dj)%p
    for i,bi in enumerate(b):
        if bi:
            for j,cj in enumerate(c):
                if cj and i+j<n:eps[i+j]=(eps[i+j]+bi*cj)%p
    return base,eps

def power(A,j,p,n,r):
    y=([1]+[0]*(n-1),[0]*n)
    for _ in range(j): y=mul(y,A,p,n,r)
    return y

def count(p,n,r):
    options=range(p)
    count_liftable=0; num_lifts=0; num_nonempty=0
    for coeffs in product(options,repeat=n-1):
        if coeffs[0]==0:continue
        base=[0]+list(coeffs)
        qualifies=0
        for v in options:
            eps=[v]+[0]*(n-1)
            F=(base,eps)
            L=power(F,n,p,n,r)
            Rbase,_=power(F,r,p,n,r)
            R=([0]*n,Rbase)
            if L==R:qualifies+=1
        if qualifies:count_liftable+=1;num_lifts+=qualifies
        if qualifies not in (0,1,p):raise AssertionError(('bad',p,n,r,qualifies))
        if qualifies not in (0,p if n%p==0 else 1): raise AssertionError(('multiplicity',p,n,r,qualifies))
    return count_liftable,num_lifts

def predicted(p,q,n,r):
    m=n-r; v=0; t=m
    while t%p==0:v+=1;t//=p
    if n%p!=0 and m==1:return (q-1)*q**(n-2),None
    threshold=m if n%p==0 else m-1
    small=(threshold+p**v-1)//(p**v)
    d=gcd(m,q-1)
    return d*q**(n-1-small),small

checks=0
for p in (2,3,5):
    for n in range(2,7 if p==2 else 6 if p==3 else 5):
        for r in range(n):
            actual,lifts=count(p,n,r)
            want,small=predicted(p,p,n,r)
            assert actual==want,(p,n,r,actual,want,small)
            assert lifts==actual*(p if n%p==0 else 1),(p,n,r,lifts,actual)
            checks+=1
print('EXHAUSTIVE_PARAMETER_CASES=',checks, 'VERIFY_OK')

# Independent characteristic-two extension field check, F_4=F_2[a]/(a*a+a+1).
def gf4mul(a,b):
    z=0
    for i in range(2):
        for j in range(2):
            if ((a>>i)&1) and ((b>>j)&1):z^=(1<<(i+j))
    if z&8:z^=0b1110 # unreachable for two degree-one factors
    if z&4:z^=0b111
    return z

def mul4(A,B,n,r):
    a,b=A;c,d=B;regular=[0]*n;inf=[0]*n
    for i,ai in enumerate(a):
        for j,cj in enumerate(c):
            k=i+j
            if k<n:regular[k]^=gf4mul(ai,cj)
            elif k-n+r<n:inf[k-n+r]^=gf4mul(ai,cj)
        for j,dj in enumerate(d):
            if i+j<n:inf[i+j]^=gf4mul(ai,dj)
    for i,bi in enumerate(b):
        for j,cj in enumerate(c):
            if i+j<n:inf[i+j]^=gf4mul(bi,cj)
    return regular,inf

def pow4(A,k,n,r):
    z=([1]+[0]*(n-1),[0]*n)
    for _ in range(k):z=mul4(z,A,n,r)
    return z

for n in range(2,5):
    for r in range(n):
        found=0
        for coeff in product(range(4),repeat=n-1):
            if coeff[0]==0:continue
            base=[0]+list(coeff)
            if any(pow4((base,[v]+[0]*(n-1)),n,n,r)==([0]*n,pow4((base,[v]+[0]*(n-1)),r,n,r)[0]) for v in range(4)):
                found+=1
        predicted_count,_=predicted(2,4,n,r)
        assert found==predicted_count,(n,r,found,predicted_count)
        checks+=1
print('INCLUDING_EXTENSION_FIELD_CASES=',checks,'VERIFY_OK')
