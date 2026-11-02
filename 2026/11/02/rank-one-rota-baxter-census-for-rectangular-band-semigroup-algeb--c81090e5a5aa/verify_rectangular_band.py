"""Direct finite-field checks of rank-one Rota--Baxter operators on rectangular bands.
Reproducible with Python 3 standard library. The multiplication is implemented from
(i,j)(k,l)=(i,l), independently of the census proof's row/column classification.
"""
from itertools import product


def field(q):
    assert q in (2,3,4)
    if q != 4:
        add = [[(a+b)%q for b in range(q)] for a in range(q)]
        mul = [[(a*b)%q for b in range(q)] for a in range(q)]
    else:
        add = [[a^b for b in range(4)] for a in range(4)]
        mul = [[0]*4 for _ in range(4)]
        for a in range(4):
            for b in range(4):
                p=0
                for i in range(2):
                    for j in range(2):
                        if (a>>i)&1 and (b>>j)&1:
                            p ^= 1 << (i+j)
                if p & 4: p ^= 7   # t^2 = t+1
                mul[a][b]=p
    return add,mul


def count(m,n,q):
    add,mul=field(q)
    N=m*n
    rows=list(product(range(q),repeat=N))
    zero=(0,)*N
    # unique representatives for each image line
    def normalize(a):
        scalar=next(x for x in a if x)
        inv=next(x for x in range(1,q) if mul[scalar][x] == 1)
        return tuple(mul[inv][x] for x in a)
    reps = [a for a in rows if a != zero and normalize(a)==a]
    # Directly construct semigroup algebra's product of arbitrary vectors.
    prodidx = [[(i//n)*n+(j%n) for j in range(N)] for i in range(N)]
    def prod(a,b):
        z=[0]*N
        for i, ai in enumerate(a):
            if not ai: continue
            for j, bj in enumerate(b):
                if bj:
                    k=prodidx[i][j]
                    z[k]=add[z[k]][mul[ai][bj]]
        return tuple(z)
    basis=[tuple(int(i==j) for i in range(N)) for j in range(N)]
    total=0; classcounts={'zero_product':0,'scaled_idempotent':0,'other':0}
    for a in reps:
        aa=prod(a,a)
        category = ('zero_product' if aa==zero else
                    'scaled_idempotent' if any(aa==tuple(mul[c][x] for x in a) for c in range(1,q)) else
                    'other')
        ae=[prod(a,e) for e in basis]
        ea=[prod(e,a) for e in basis]
        for f in rows:
            if f==zero: continue
            ae_eval=[0]*N; ea_eval=[0]*N
            for j in range(N):
                for k in range(N):
                    ae_eval[j]=add[ae_eval[j]][mul[f[k]][ae[j][k]]]
                    ea_eval[j]=add[ea_eval[j]][mul[f[k]][ea[j][k]]]
            good=True
            for i in range(N):
                if not good: break
                for j in range(N):
                    lhs_coeff=mul[f[i]][f[j]]
                    rhs_coeff=add[mul[f[i]][ae_eval[j]]][mul[f[j]][ea_eval[i]]]
                    for k in range(N):
                        if mul[lhs_coeff][aa[k]] != mul[rhs_coeff][a[k]]:
                            good=False; break
                    if not good: break
            if good:
                total+=1;classcounts[category]+=1
    d=(m-1)*(n-1)
    numerator = ((q**d-1)*(q**N-1)
       + q**d*(q**(n-1)-1)*(q**(N-m)-1)
       + q**d*(q**(m-1)-1)*(q**(N-n)-1))
    assert numerator%(q-1)==0
    expected_zero=numerator//(q-1)
    expected_quasi=q**(m+n-2)*(q**(n-1)+q**(m-1)-2)
    assert classcounts['other']==0
    assert classcounts['zero_product']==expected_zero, (m,n,q,'zero',classcounts,expected_zero)
    assert classcounts['scaled_idempotent']==expected_quasi, (m,n,q,'quasi',classcounts,expected_quasi)
    assert total == expected_zero+expected_quasi
    print(f'm={m}, n={n}, q={q}: direct={total}, zero_product={expected_zero}, quasi_idempotent={expected_quasi} PASS')


if __name__=='__main__':
    for m,n,q in [(1,1,2),(1,2,3),(1,3,2),(2,2,2),(2,2,3),(2,2,4),(2,3,2)]:
        count(m,n,q)
    print('RECTANGULAR_BAND_RANK_ONE_RB_OK')
