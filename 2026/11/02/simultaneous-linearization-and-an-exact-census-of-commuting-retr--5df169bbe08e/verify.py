"""Independent finite-field checks for commuting algebra retractions of a truncated free tensor algebra.
Run: python verify.py
"""
from itertools import product
from collections import Counter
from math import prod

# Algebra basis x,y,xx,xy,yx,yy; multiplication in length <= 2.
N=6

def matmul(u,v,q):
    w=[0]*N
    a,b=u[:2]; c,d=v[:2]
    w[2]=(a*c)%q; w[3]=(a*d)%q;w[4]=(b*c)%q;w[5]=(b*d)%q
    return tuple(w)

def vec_encode(v,q):
    z=0
    for a in reversed(v): z=z*q+a
    return z

def vec_decode(z,q):
    v=[]
    for _ in range(N): v.append(z%q);z//=q
    return tuple(v)

def eval_elem(e,z,q):
    # e is a pair of generator images, z is a 6-coordinate vector
    x,y=e
    imgs=(x,y,matmul(x,x,q),matmul(x,y,q),matmul(y,x,q),matmul(y,y,q))
    return tuple(sum(z[j]*imgs[j][i] for j in range(N))%q for i in range(N))

def all_idempotents(q):
    elements=[vec_decode(i,q) for i in range(q**N)]
    idems=[]
    for x in elements:
        xx=matmul(x,x,q)
        for y in elements:
            yy=matmul(y,y,q); xy=matmul(x,y,q); yx=matmul(y,x,q)
            imgs=(x,y,xx,xy,yx,yy)
            def apply(z):
                return tuple(sum(z[j]*imgs[j][i] for j in range(N))%q for i in range(N))
            if apply(x)==x and apply(y)==y:
                idems.append((x,y))
    return idems

def r2matrix(e,q):
    return ((e[0][0],e[1][0]),(e[0][1],e[1][1]))

def rank_matrix(A,q):
    a=[list(row) for row in A]; n=len(a);m=len(a[0]); r=0
    for j in range(m):
        pivot=next((i for i in range(r,n) if a[i][j]),None)
        if pivot is None:continue
        a[r],a[pivot]=a[pivot],a[r]
        inv=pow(a[r][j],-1,q)
        a[r]=[(v*inv)%q for v in a[r]]
        for i in range(n):
            if i!=r and a[i][j]:
                v=a[i][j];a[i]=[(aa-v*bb)%q for aa,bb in zip(a[i],a[r])]
        r+=1
    return r

def multiply2(A,B,q):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%q for j in range(2)) for i in range(2))

def dimension_vector(tup,q):
    matrices=[r2matrix(e,q) for e in tup]
    I=((1,0),(0,1))
    result=[]
    for weight in product((0,1),repeat=len(tup)):
        accum=I
        for P,bit in zip(matrices,weight):
            B=P if bit else tuple(tuple((I[i][j]-P[i][j])%q for j in range(2))for i in range(2))
            accum=multiply2(accum,B,q)
        result.append(rank_matrix(accum,q))
    return tuple(result)

def formula(n,m,L,q):
    weights=list(product((0,1),repeat=m))
    S=sum(n**d for d in range(2,L+1))
    def gl(t):
        return prod(q**t-q**j for j in range(t))
    out={}
    def composition(v,k):
        if k==1:
            yield (v,)
        else:
            for i in range(v+1):
                for t in composition(v-i,k-1):yield (i,)+t
    for counts in composition(n,len(weights)):
        H=0
        for d in range(2,L+1):
            for ix in product(range(len(weights)), repeat=d):
                w=tuple(int(all(weights[j][i] for j in ix))for i in range(m))
                target=weights.index(w)
                H+=counts[target]*prod(counts[j] for j in ix)
        out[counts]=gl(n)//prod(gl(k) for k in counts)*q**(n*S-H)
    return out

if __name__=='__main__':
    for q in (2,3):
        e=all_idempotents(q)
        hist=Counter(rank_matrix(r2matrix(x,q),q) for x in e)
        expected=Counter()
        for sizes,ct in formula(2,1,2,q).items(): expected[sizes[1]]+=ct
        assert hist==expected,('single',q,hist,expected)
        print(f'F_{q}: all {q**12} endomorphisms inspected; idempotent rank histogram {dict(sorted(hist.items()))}')
        if q in (2,3):
            actual=Counter()
            for x in e:
                for y in e:
                    if eval_elem(x,y[0],q)==eval_elem(y,x[0],q) and eval_elem(x,y[1],q)==eval_elem(y,x[1],q):
                        actual[dimension_vector((x,y),q)]+=1
            predicted=formula(2,2,2,q)
            assert actual==predicted,('pairs',actual,predicted)
            print(f'F_{q}: all {len(e)**2} idempotent pairs inspected; commuting={sum(actual.values())}, joint-weight strata={len(actual)}')
            print(f'F_{q} joint-weight counts:',sorted(actual.items()))
            if q==2:
                adjacency=[[False]*len(e) for _ in e]
                for i,x in enumerate(e):
                    for j,y in enumerate(e):
                        adjacency[i][j]=(eval_elem(x,y[0],q)==eval_elem(y,x[0],q) and eval_elem(x,y[1],q)==eval_elem(y,x[1],q))
                hist3=Counter()
                for i,x in enumerate(e):
                    for j,y in enumerate(e):
                        if adjacency[i][j]:
                            for k,z in enumerate(e):
                                if adjacency[i][k] and adjacency[j][k]:
                                    hist3[dimension_vector((x,y,z),q)]+=1
                assert hist3==formula(2,3,2,q)
                print(f'F_2: all {len(e)**3} idempotent triples tested; commuting={sum(hist3.values())}, strata={len(hist3)}')
    print('TRUNCATED_FREE_RETRACTIONS_CHECKS_OK')
