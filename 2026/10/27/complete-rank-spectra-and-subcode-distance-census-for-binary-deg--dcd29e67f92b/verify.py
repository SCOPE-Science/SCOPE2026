"""Independent finite-field checks for binary degree-two Gabidulin hyperplanes.

Uses bit-polynomial arithmetic, constructs every linearized-map matrix directly,
and enumerates every coefficient hyperplane. Standard-library Python only.
"""
from collections import Counter
from itertools import combinations

POLY={2:0b111,3:0b1011,4:0b10011,5:0b100101}

def mul(a,b,m):
    modulus=POLY[m]
    out=0
    while b:
        if b&1:out^=a
        b>>=1
        a<<=1
        if a & (1<<m): a ^= modulus
    return out

def rank(rows,m):
    basis=[0]*m
    r=0
    for row in rows:
        v=row
        for bit in range(m-1,-1,-1):
            if not ((v>>bit)&1): continue
            if basis[bit]:v^=basis[bit]
            else:
                basis[bit]=v;r+=1;break
    return r

def map_rank(a,b,m):
    rows=[]
    for i in range(m):
        x=1<<i
        ax=mul(a,x,m)
        bx2=mul(b,mul(x,x,m),m)
        rows.append(ax^bx2)
    return rank(rows,m)

def is_in_hyperplane(a,b,s,t):
    return ((s&a).bit_count()+(t&b).bit_count())%2==0

def verify_subspaces(m, rank_by_code):
    d=2*m;count=0;full=[]
    for pivots in combinations(range(d),m):
        freedom=[(i,c) for i,p in enumerate(pivots)
                 for c in range(p+1,d) if c not in pivots]
        for choice in range(1<<len(freedom)):
            rows=[1<<p for p in pivots]
            for j,(i,c) in enumerate(freedom):
                if choice>>j&1: rows[i] |=1<<c
            if all(rank_by_code[__import__('functools').reduce(int.__xor__,(rows[i] for i in range(m) if mask>>i&1),0)]==m for mask in range(1,1<<m)):
                count+=1;full.append(tuple(rows))
    assert count==2,(m,count,full)
    print(f'm={m} full_rank_dimension_m_subspaces={count} verified')



def gaussian(n,k):
    if k<0 or k>n:return 0
    numerator=1;denominator=1
    for i in range(k):
        numerator*=2**(n-i)-1
        denominator*=2**(k-i)-1
    assert numerator%denominator==0
    return numerator//denominator

def gl_count(t):
    result=1
    for i in range(t):result*=2**t-2**i
    return result

def predicted_subcode_census(m,d):
    result=Counter()
    for r in range(m+1):
        for s in range(m+1):
            t=d-r-s
            if not 0<=t<=min(m-r,m-s):continue
            count=gaussian(m,r)*gaussian(m,s)*gaussian(m-r,t)*gaussian(m-s,t)*gl_count(t)
            if count:result[(r,s)]=count
    assert sum(result.values())==gaussian(2*m,d)
    return result

def all_rref_subspaces(dimension,degree):
    for pivots in combinations(range(dimension),degree):
        freedom=[(i,c) for i,p in enumerate(pivots)
                 for c in range(p+1,dimension) if c not in pivots]
        for choice in range(1<<len(freedom)):
            rows=[1<<p for p in pivots]
            for j,(i,c) in enumerate(freedom):
                if choice>>j&1:rows[i]|=1<<c
            yield rows

def verify_census(m,rank_by_code):
    Q=1<<m
    total=0
    for d in range(2*m+1):
        observed=Counter()
        for rows in all_rref_subspaces(2*m,d):
            r=d-rank([row>>m for row in rows],m)
            s=d-rank([row&(Q-1) for row in rows],m)
            observed[(r,s)]+=1
            if m<=3:
                full=0
                for selection in range(1,1<<d):
                    vector=0
                    for i,row in enumerate(rows):
                        if selection>>i&1:vector^=row
                    if rank_by_code[vector]==m:full+=1
                assert full==2**r+2**s-2,(m,d,r,s,rows,full)
        assert observed==predicted_subcode_census(m,d),(m,d,observed,predicted_subcode_census(m,d))
        total+=sum(observed.values())
        print(f'm={m} subcode_dim={d} count={sum(observed.values())} profiles={len(observed)} verified')
    print(f'm={m} all_subcodes={total} CENSUS_OK')

for m,modulus in POLY.items():
    Q=1<<m
    rank_by_code=[]
    for b in range(Q):
        for a in range(Q):
            got=map_rank(a,b,m)
            expected=0 if a==b==0 else (m if a==0 or b==0 else m-1)
            assert got==expected,(m,a,b,got,expected)
            rank_by_code.append(got)
    observations=Counter()
    for t in range(Q):
        for s in range(Q):
            if s==t==0:continue
            count=Counter()
            for b in range(Q):
                for a in range(Q):
                    if is_in_hyperplane(a,b,s,t):
                        count[rank_by_code[b*Q+a]]+=1
            assert count[0]==1 and sum(count.values())==Q*Q//2
            predicted_full=3*Q//2-2 if (s==0 or t==0) else Q-2
            assert count[m]==predicted_full,(m,s,t,count,predicted_full)
            assert count[m-1]==Q*Q//2-1-predicted_full
            observations[(s==0 or t==0,count[m],count[m-1])]+=1
    assert observations[(True,3*Q//2-2,Q*Q//2-3*Q//2+1)]==2*(Q-1)
    assert observations[(False,Q-2,Q*Q//2-Q+1)]==(Q-1)**2
    assert sum(observations.values())==Q*Q-1
    print(f'm={m} matrices={Q*Q} hyperplanes={Q*Q-1} coordinate={2*(Q-1)} coupled={(Q-1)**2} rank_m_counts=({3*Q//2-2},{Q-2}) verified')
    if m<=3:verify_subspaces(m,rank_by_code)
    if m<=4:verify_census(m,rank_by_code)
print('VERIFY_OK')
