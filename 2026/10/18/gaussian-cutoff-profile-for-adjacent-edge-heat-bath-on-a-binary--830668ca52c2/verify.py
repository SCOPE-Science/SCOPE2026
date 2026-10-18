from fractions import Fraction
from math import comb, exp, log, sqrt

def count(n,k,r):
    if not(1 <= r <= min(k,n-k)): return 0
    return n*comb(k-1,r-1)*comb(n-k-1,r-1)//r

def boundary_size(n,mask):
    return sum(bool(mask & (1<<i)) or bool(mask & (1<<((i+1)%n))) for i in range(n))

def clusters(n,mask):
    return sum(bool(mask & (1<<i)) and not bool(mask & (1<<((i-1)%n))) for i in range(n))

def check_counts(n):
    for k in range(1,n):
        for r in range(1,min(k,n-k)+1):
            got=sum(1 for m in range(1,(1<<n)-1) if m.bit_count()==k and clusters(n,m)==r)
            assert got==count(n,k,r),(n,k,r,got,count(n,k,r))

def check_direct(n,t):
    size=1<<n
    p=[Fraction(0) for _ in range(size)];p[0]=Fraction(1)
    for _ in range(t):
        q=[Fraction(0) for _ in range(size)]
        for x,pv in enumerate(p):
            if pv==0: continue
            for i in range(n):
                j=(i+1)%n
                base=x & ~(1<<i) & ~(1<<j)
                for a in (0,1):
                    for b in (0,1):
                        q[base | (a<<i) | (b<<j)] += pv/Fraction(4*n)
        p=q
    # all Walsh coefficients obtained from true distribution
    for mask in range(size):
        got=sum(p[x]*(1 if (x & mask).bit_count()%2==0 else -1) for x in range(size))
        exact=Fraction(n-boundary_size(n,mask),n)**t if t>0 else Fraction(1)
        assert got==exact,(n,t,mask,got,exact)

def chi_square(n,t):
    ans=0.
    for k in range(1,n):
        for r in range(1,min(k,n-k)+1):
            lam=1-(k+r)/n
            if lam>0: ans+=count(n,k,r)*lam**(2*t)
    return ans

def product_l2_distance_sq(n,t):
    b=(1-2/n)**t
    ans=b**(2*n)
    for k in range(1,n):
        for r in range(1,min(k,n-k)+1):
            lam=1-(k+r)/n
            a=lam**t if lam>0 else 0
            ans+=count(n,k,r)*(a-b**k)**2
    return ans

if __name__=='__main__':
    tests=0
    for n in range(3,9):
        check_counts(n);tests+=sum(min(k,n-k) for k in range(1,n))
        for t in range(1,5):
            check_direct(n,t);tests+=(1<<n)
            assert abs(chi_square(n,t)-sum((1-boundary_size(n,m)/n)**(2*t) for m in range(1,1<<n))) < 1e-9
            tests+=1
    for n in (50,100,200,500):
        t=round(n*log(n)/4)
        L2=product_l2_distance_sq(n,t)
        chisq=chi_square(n,t)
        print('n',n,'time',t,'L2distance',sqrt(L2),'chi-square',chisq,'target',exp(1)-1)
        assert L2>=0 and L2<5 and chisq>0
        tests+=2
    print('VERIFY_OK',tests)
