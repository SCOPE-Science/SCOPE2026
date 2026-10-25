from itertools import permutations
from collections import Counter
from math import factorial

def sweep(n,pi):
    rows=[1<<i for i in range(n)]
    for i in pi:
        rows[i]=rows[(i-1)%n]^rows[(i+1)%n]
    return rows

def cp_direct(rows):
    n=len(rows); dp=[0]*(1<<n);dp[0]=1
    for mask in range(1,1<<n):
        i=mask.bit_count()-1
        s=0
        for j in range(n):
            if mask&(1<<j) and rows[i]>>j&1: s^=dp[mask^(1<<j)]
            if mask&(1<<j) and i==j:s^=dp[mask^(1<<j)]<<1
        dp[mask]=s
    return dp[-1]

def H(n):
    a,b=2,4 # H1=t; H2=t2
    if n==1:return a
    if n==2:return b
    for _ in range(3,n+1):a,b=b,((a^b)<<1)
    return b

def cyc_asc(n,pi):
    pos=[0]*n
    for k,i in enumerate(pi):pos[i]=k
    return sum(pos[i]<pos[(i+1)%n] for i in range(n))

def mul(A,B):
    C=[]
    for v in A:
        s=0
        while v:
            p=(v&-v).bit_length()-1
            s^=B[p];v&=v-1
        C.append(s)
    return C

def nilpotent(A):
    n=len(A)
    X=[1<<i for i in range(n)]
    for _ in range(n):X=mul(A,X)
    return all(x==0 for x in X)

def eulerian(m,k):
    a=[1]
    for n in range(2,m+1):
        b=[0]*n
        for j in range(n):
            b[j]=(j+1)*(a[j] if j<len(a) else 0)+(n-j)*(a[j-1] if j else 0)
        a=b
    return a[k]

total=0; fullnil=0
for n in range(3,8):
    stats=Counter();ct=0;polys=set();nin=0
    for pi in permutations(range(n)):
        a=cyc_asc(n,pi)
        A=sweep(n,pi)
        cp=cp_direct(A)
        expected=H(n)^(1<<a)^(1<<(n-a))
        assert cp==expected,(n,pi,hex(cp),hex(expected))
        stats[a]+=1;polys.add(cp);ct+=1
        if n<=6 or n==7:
            is_nil=nilpotent(A)
            expected_nil=(n&(n-1)==0 and a==n//2)
            assert is_nil==expected_nil,(n,pi,a,is_nil)
            nin+=is_nil
        total+=1
    assert len(polys)==n//2,(n,len(polys))
    assert all(stats[a]==n*eulerian(n-1,a-1) for a in range(1,n))
    print('n',n,'schedules',ct,'polynomials',len(polys),'nil',nin,'freq',sorted(stats.items()))
    fullnil+=nin
for n,reps in [(8,200),(9,100),(10,35),(11,7),(12,2),(16,30),(20,25)]:
    import random
    rng=random.Random(n)
    for rep in range(reps):
        pi=list(range(n)); rng.shuffle(pi)
        a=cyc_asc(n,pi);A=sweep(n,pi)
        if n<=12:
            assert cp_direct(A)==H(n)^(1<<a)^(1<<(n-a))
        assert nilpotent(A)==(n&(n-1)==0 and a==n//2)
        total+=1
assert sum(cyc_asc(8,pi)==4 for pi in permutations(range(8)))==19328
print('VERIFY_OK', 'tested_schedules',total,'nilpotent_exhaustive_through_7',fullnil,'n8_balanced',19328,'additional_samples',399)
