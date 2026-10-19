"""Finite-field counts of involutive automorphisms of the 5-dimensional free class-three Lie algebra."""
from itertools import product

def mul(X,Y,q):
    n=len(X)
    return [[sum(X[i][k]*Y[k][j] for k in range(n))%q for j in range(n)] for i in range(n)]

def matrix(a,b,c,d,e,f,g,h,i,j,q):
    delta=(a*g-b*f)%q
    return [[a, f, 0, 0, 0],
            [b, g, 0, 0, 0],
            [c, h, delta, 0, 0],
            [d, i, (a*h-c*f)%q,(delta*a)%q,(delta*f)%q],
            [e, j, (b*h-c*g)%q,(delta*b)%q,(delta*g)%q]]

def test(q):
    counts={}
    for a,b,f,g in product(range(q),repeat=4):
        delta=(a*g-b*f)%q
        if not delta: continue
        cts=0
        for c,h,d,e,i,j in product(range(q),repeat=6):
            T=matrix(a,b,c,d,e,f,g,h,i,j,q)
            TT=mul(T,T,q)
            if TT==[[int(i==j) for j in range(5)] for i in range(5)]:
                cts+=1
        counts[(a,b,f,g)]=cts
    total=sum(counts.values())
    expected=q**5+q**4-q**3 if q%2==0 else 1+q**2+q**4*(q+1)
    print('q',q,'total',total,'expected',expected,'distinct fibers',sorted(set(counts.values())))
    assert total==expected
    return total

if __name__=='__main__':
    for q in (2,3): test(q)

def gf4_add(x,y): return x^y

def gf4_mul(x,y):
    z=0
    for i in range(2):
        for j in range(2):
            if ((x>>i)&1) and ((y>>j)&1): z ^= (1<<(i+j))
    if z&8: z^=(8|2)  # x^3=x(x+1) in F_4
    if z&4: z^=(4|2|1) # x^2=x+1
    return z

def gf4_square(T):
    return [[gf4_sum(gf4_mul(T[i][k],T[k][j]) for k in range(5)) for j in range(5)] for i in range(5)]

def gf4_sum(it):
    ans=0
    for x in it: ans^=x
    return ans

def gf4_matrix(a,b,c,d,e,f,g,h,i,j):
    delta=gf4_add(gf4_mul(a,g),gf4_mul(b,f))
    return [[a,f,0,0,0],
        [b,g,0,0,0],
        [c,h,delta,0,0],
        [d,i,gf4_add(gf4_mul(a,h),gf4_mul(c,f)),gf4_mul(delta,a),gf4_mul(delta,f)],
        [e,j,gf4_add(gf4_mul(b,h),gf4_mul(c,g)),gf4_mul(delta,b),gf4_mul(delta,g)]]

def test4():
    total=0
    cts={}
    for a,b,f,g in product(range(4),repeat=4):
        delta=gf4_add(gf4_mul(a,g),gf4_mul(b,f))
        if not delta: continue
        if (gf4_add(gf4_mul(a,a),gf4_mul(f,b))!=1 or
            gf4_add(gf4_mul(a,f),gf4_mul(f,g))!=0 or
            gf4_add(gf4_mul(b,a),gf4_mul(g,b))!=0 or
            gf4_add(gf4_mul(b,f),gf4_mul(g,g))!=1):
            continue
        cnt=0
        for c,h,d,e,i,j in product(range(4),repeat=6):
            T=gf4_matrix(a,b,c,d,e,f,g,h,i,j)
            if gf4_square(T)==[[int(i==j) for j in range(5)] for i in range(5)]:
                cnt+=1
        cts[(a,b,f,g)]=cnt
        total+=cnt
    print('q 4','total',total,'expected',4**5+4**4-4**3,'distinct fibers',sorted(set(cts.values())))
    assert total==1216

if __name__=='__main__': test4()
