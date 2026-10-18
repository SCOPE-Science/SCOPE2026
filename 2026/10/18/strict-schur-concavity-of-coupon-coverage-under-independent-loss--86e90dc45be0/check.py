"""Exact arithmetic checks for coupon coverage optimization theorem.
Run: python check.py. Standard library only.
"""
from fractions import Fraction as F
from itertools import product, combinations
from math import comb

checks=0

def assert_equal(a,b):
    global checks
    assert a==b,(a,b)
    checks+=1

def after_one(dist,weight,q):
    n=len(weight)
    nd={}
    for state,mass in dist.items():
        for i,w in enumerate(weight):
            pre=state|(1<<i)
            active=[j for j in range(n) if pre>>j&1]
            for mask in range(1<<len(active)):
                new=sum((1<<j) for k,j in enumerate(active) if mask>>k&1)
                v=mass*w*(q**mask.bit_count())*((1-q)**(len(active)-mask.bit_count()))
                nd[new]=nd.get(new,F(0))+v
    return nd

def direct(n,weight,qs,A):
    total=F(0)
    for word in product(range(n), repeat=len(qs)):
        mass=F(1)
        for j in word:mass*=weight[j]
        for i in A:
            inds=[s for s,z in enumerate(word) if z==i]
            if not inds:
                mass=F(0);break
            s=inds[-1]
            for r in range(s,len(qs)): mass*=qs[r]
        total+=mass
    return total

def markov(n,weight,qs,A):
    dist={0:F(1)}
    for q in qs: dist=after_one(dist,weight,q)
    return sum(v for state,v in dist.items() if all(state>>j&1 for j in A))

weights=[(F(1,2),F(1,3),F(1,6)),(F(2,5),F(1,5),F(2,5)),(F(1,3),)*3,
         (F(1,2),F(1,6),F(1,6),F(1,6))]
qs_list=[(F(1,2),F(2,3),F(3,4),F(4,5)),(F(2,3),)*4,(F(1),)*4]
for w in weights:
    n=len(w)
    for qs0 in qs_list:
        for t in range(0,5):
            qs=qs0[:t]
            for r in range(1,n+1):
                for A in combinations(range(n),r):
                    assert_equal(direct(n,w,qs,A),markov(n,w,qs,A))
                    if t>=r:
                        for i,j in combinations(A,2):
                            new=list(w);new[i]=new[j]=(w[i]+w[j])/2
                            before=direct(n,w,qs,A)
                            after=direct(n,new,qs,A)
                            assert after>=before,(n,t,A,w,new,after,before)
                            checks+=1
                            if w[i]!=w[j] and all(q>0 for q in qs):
                                assert after>before,(n,t,A,w,new,after,before)
                                checks+=1

# Last-run survival tail: P(K >= k)=a^k+b^k for every k=1,...,m.
for a in [F(1,7),F(2,5),F(1,2),F(5,6)]:
    b=1-a
    for m in range(2,8):
        for k in range(1,m+1):
            got=F(0)
            for z in product([0,1],repeat=m):
                p=a**z.count(0)*b**z.count(1)
                if all(z[m-1-j]==z[-1] for j in range(k)):
                    got+=p
            assert_equal(got,a**k+b**k)

# Independent stationary formula via subset recursion and 2^n x 2^n full-state matrix.
def stationary_moments(w,q):
    n=len(w);moment={0:F(1)}
    for r in range(1,n+1):
        for C in combinations(range(n),r):
            S=sum(1<<i for i in C)
            W=sum(w[i] for i in C)
            numer=q**r *sum(w[i]*moment[S^(1<<i)] for i in C)
            moment[S]=numer/(1-q**r*(1-W))
    return moment

def solve_linear(M,b):
    M=[row[:]+[right] for row,right in zip(M,b)];n=len(b)
    for j in range(n):
        pivot=next(i for i in range(j,n) if M[i][j]);M[j],M[pivot]=M[pivot],M[j]
        v=M[j][j];M[j]=[x/v for x in M[j]]
        for i in range(n):
            if i==j:continue
            d=M[i][j]
            if d:M[i]=[x-d*y for x,y in zip(M[i],M[j])]
    return [row[-1] for row in M]

def stationary_direct(w,q):
    n=len(w);states=1<<n
    P=[[F(0) for _ in range(states)] for _ in range(states)]
    for old in range(states):
        d=after_one({old:F(1)},w,q)
        for new,mass in d.items():P[old][new]=mass
    matrix=[[P[old][new] - (F(1) if old==new else F(0)) for old in range(states)] for new in range(states)]
    matrix[-1]=[F(1)]*states
    b=[F(0)]*states;b[-1]=F(1)
    return solve_linear(matrix,b)

for w in weights[:3]:
    for q in [F(1,3),F(2,3),F(4,5)]:
        n=len(w);stat=stationary_direct(w,q);mom=stationary_moments(w,q)
        for A in range(1<<n):
            assert_equal(sum(stat[S] for S in range(1<<n) if S&A==A),mom[A])
        for i,j in combinations(range(n),2):
            new=list(w);new[i]=new[j]=(w[i]+w[j])/2
            a=stationary_moments(new,q)[(1<<n)-1]
            b=moment_all=mom[(1<<n)-1]
            assert a>=b,(w,new,q,a,b)
            checks+=1
            if w[i]!=w[j]: assert a>b,(w,new,q,a,b);checks+=1

print(f'PASS {checks} exact assertions')
