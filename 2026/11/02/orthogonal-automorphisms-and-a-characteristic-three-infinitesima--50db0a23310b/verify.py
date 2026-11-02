"""Independent modular checks for automorphisms and derivations of complete-bipartite graph evolution algebras. Python 3, stdlib only."""
from itertools import product

def det2(a,q): return (a[0]*a[3]-a[1]*a[2])%q

def mats2(q):
    for x in product(range(q),repeat=4):
        if det2(x,q): yield x

def trans_mul(a,b,q):
    # column-major 2 by 2 matrices
    return tuple(sum(a[k*2+i]*b[j*2+k] for k in range(2))%q for j in range(2) for i in range(2))

def gram(a,q):
    return tuple(sum(a[i*2+k]*a[j*2+k] for k in range(2))%q for j in range(2) for i in range(2))

def vec_sum(a,q): return ((a[0]+a[2])%q,(a[1]+a[3])%q)

def count_side(q):
    G=[x for x in mats2(q)]
    # A(u0)=alpha*u0 and A^t A=beta I; independently group all allowable pairs
    aa=[]; bb=[]
    for A in G:
        au=vec_sum(A,q); gg=gram(A,q)
        if au[0]==au[1] and au[0] and gg[1]==gg[2]==0 and gg[0]==gg[3] and gg[0]:
            aa.append((au[0],gg[0]))
            bb.append((au[0],gg[0]))
    by={}
    for al,be in aa:by[al,be]=by.get((al,be),0)+1
    total=sum(x*y for (a,b),x in by.items() for (c,d),y in by.items() if c==b and d==a)
    expect=4*__import__('math').gcd(3,q-1)
    assert total==expect,(q,total,expect)
    # Each ordered choice has a disjoint swapped counterpart in Aut(K_{2,2}).
    assert 2*total==8*__import__('math').gcd(3,q-1)
    return (len(G),total,2*total)

def rank_mod(M,p):
    if not M:return 0
    a=[list(map(lambda x:x%p,row)) for row in M];nr=len(a);nc=len(a[0]);i=0
    for j in range(nc):
        pivot=next((r for r in range(i,nr) if a[r][j]),None)
        if pivot is None: continue
        a[i],a[pivot]=a[pivot],a[i]
        inv=pow(a[i][j],-1,p);a[i]=[(v*inv)%p for v in a[i]]
        for r in range(nr):
            if r!=i and a[r][j]:
                v=a[r][j];a[r]=[(b-v*c)%p for b,c in zip(a[r],a[i])]
        i+=1
        if i==nr:break
    return i

def derivation_dimension(r,s,p):
    n=r+s
    # e_i^2 = sum of all opposite-side basis vectors
    square=[[1 if (i<r and j>=r) or (i>=r and j<r) else 0 for j in range(n)] for i in range(n)]
    # Unknown entries D_{out,in}; impose Leibniz on basis products.
    matrix=[]
    for i in range(n):
        for j in range(i,n):
            for out in range(n):
                coeff=[0]*(n*n)
                if i==j:
                    for k in range(n):coeff[out*n+k]+=square[i][k]
                    coeff[i*n+i]-=2*square[i][out]
                else:
                    coeff[j*n+i]-=square[j][out]
                    coeff[i*n+j]-=square[i][out]
                matrix.append(coeff)
    return n*n-rank_mod(matrix,p)

for q in (3,5,7):
    gl,ps,all_count=count_side(q)
    print('K22 GF',q,'GL2',gl,'part_preserving',ps,'full',all_count)
for p,r,s in [(3,2,2),(3,2,4),(5,2,2),(5,3,3),(7,2,2),(7,3,3),(7,4,4)]:
    d=derivation_dimension(r,s,p)
    predicted=(r-1)*(r-2)//2+(s-1)*(s-2)//2+(1 if p==3 else 0)
    assert d==predicted,(p,r,s,d,predicted)
    print('Der_k for K_%d_%d characteristic %d dimension %d (predicted %d)'%(r,s,p,d,predicted))
print('VERIFY_OK')
