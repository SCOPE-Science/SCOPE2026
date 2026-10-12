from itertools import combinations, product
from math import comb

P = 3
G = [
    [1]*33,
    [2,1,1,2,0,1,0,2,2,1,0,2,1,1,1,0,1,0,1,2,1,2,1,2,0,2,0,1,1,1,0,1,0],
    [1,0,2,1,0,2,1,1,2,2,2,0,1,2,2,1,1,2,2,0,0,2,1,2,1,0,0,2,2,0,0,2,2],
    [1,1,1,1,1,1,0,1,2,1,1,2,2,0,2,2,0,2,2,1,2,1,1,0,1,0,1,0,0,0,1,2,0],
    [2,2,1,0,0,2,1,1,2,0,2,0,1,0,0,0,0,2,1,2,1,2,2,2,2,1,1,2,1,0,2,2,2],
]

def rank_mod(M, p):
    A=[row[:] for row in M]
    r=0
    for c in range(len(A[0])):
        pivot=next((i for i in range(r,len(A)) if A[i][c]%p),None)
        if pivot is None: continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=pow(A[r][c],-1,p)
        A[r]=[(inv*x)%p for x in A[r]]
        for i in range(len(A)):
            if i!=r and A[i][c]%p:
                f=A[i][c]%p
                A[i]=[(x-f*y)%p for x,y in zip(A[i],A[r])]
        r+=1
        if r==len(A): break
    return r

assert rank_mod(G,P)==5
cols=[tuple(G[r][j] for r in range(5)) for j in range(33)]
assert all(any(x for x in v) for v in cols)
assert len(set(cols))==33
# Since the first coordinate is 1 in every column, two columns can be
# proportional only if the scalar is 1, hence only if the columns coincide.
for i,j in combinations(range(33),2):
    assert cols[i]!=cols[j]

triples=[]
for ijk in combinations(range(33),3):
    vs=[cols[i] for i in ijk]
    hit=False
    # Normalize the first nonzero coefficient to 1; weight-three requires all
    # coefficients nonzero.
    for a,b in product((1,2), repeat=2):
        if all((vs[0][r]+a*vs[1][r]+b*vs[2][r])%P==0 for r in range(5)):
            hit=True
            break
    if hit: triples.append(ijk)
assert triples

# Primary source Table III: 1+32 z^18+96 z^21+112 z^24+2 z^33.
A={0:1,18:32,21:96,24:112,33:2}
n=33;k=5;q=3
assert sum(A.values())==q**k

def kraw(j,w):
    lo=max(0,j-(n-w)); hi=min(j,w)
    return sum(((-1)**i)*(q-1)**(j-i)*comb(w,i)*comb(n-w,j-i)
               for i in range(lo,hi+1))

dual={j:sum(cnt*kraw(j,w) for w,cnt in A.items())//(q**k) for j in range(4)}
assert dual=={0:1,1:0,2:0,3:160}, dual
print('rank',rank_mod(G,P))
print('dependent_triple_count',len(triples))
print('dual_low_weights',dual)
print('VERIFY_OK')
