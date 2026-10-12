from itertools import product

def r(alpha,q):
    return (1+sum(alpha))%q

def op(x,y,q):
    t,a=x; s,b=y
    ra=r(a,q)
    return ((t+s)%q,tuple((a[i]+ra*b[i])%q for i in range(len(a))))

def inv(x,q):
    t,a=x
    z=pow(r(a,q),-1,q)
    return ((-t)%q,tuple((-z*v)%q for v in a))

def group(q,n):
    G=[]
    for t in range(q):
        for a in product(range(q),repeat=n):
            if r(a,q): G.append((t,a))
    return G

def comm(x,y,q):
    return op(op(op(x,y,q),inv(x,q),q),inv(y,q),q)

for q,n in [(2,3),(2,4),(3,3),(5,3)]:
    G=group(q,n); S=set(G); e=(0,(0,)*n)
    assert len(G)==q**n*(q-1)
    for x in G:
        assert op(x,inv(x,q),q)==e==op(inv(x,q),x,q)
    for x in G:
        for y in G:
            assert op(x,y,q) in S
    # exhaustive associativity in smaller cases, sampled-by-all-z for q=2,3 n=3
    if len(G)<=60:
        for x in G:
            for y in G:
                for z in G:
                    assert op(op(x,y,q),z,q)==op(x,op(y,z,q),q)
    center=[x for x in G if all(op(x,y,q)==op(y,x,q) for y in G)]
    derived={e}
    for x in G:
        for y in G:
            derived.add(comm(x,y,q))
    # generated subgroup is already translation hyperplane for q>2; close directly
    changed=True
    while changed:
        changed=False
        cur=list(derived)
        for x in cur:
            for y in cur:
                z=op(x,y,q)
                if z not in derived:
                    derived.add(z); changed=True
    if q==2:
        assert len(center)==len(G)==2**n
        assert len(derived)==1
    else:
        assert len(center)==q
        assert len(derived)==q**(n-1)
    print({'q':q,'n':n,'order':len(G),'center':len(center),'derived':len(derived)})

# Matrix helpers for the Hom-Jacobi check on T_3.
def madd(A,B,q): return tuple(tuple((A[i][j]+B[i][j])%q for j in range(3)) for i in range(3))
def msub(A,B,q): return tuple(tuple((A[i][j]-B[i][j])%q for j in range(3)) for i in range(3))
def mmul(A,B,q): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3))%q for j in range(3)) for i in range(3))
def smul(s,A,q): return tuple(tuple(s*A[i][j]%q for j in range(3)) for i in range(3))
def bracket(A,B,q): return msub(mmul(A,B,q),mmul(B,A,q),q)
def add3(A,B,C,q): return madd(madd(A,B,q),C,q)
I=((1,0,0),(0,1,0),(0,0,1)); E=((0,0,1),(0,0,0),(0,0,0))
basis=[]
for i in range(3):
    for j in range(i,3):
        M=[[0]*3 for _ in range(3)]; M[i][j]=1; basis.append(tuple(tuple(x) for x in M))

def phi(X,t,a,q):
    P=madd(I,smul(t,E,q),q); Pinv=msub(I,smul(t,E,q),q)
    Y=mmul(mmul(P,X,q),Pinv,q)
    ell=sum(a[i]*X[i][i] for i in range(3))%q
    return madd(Y,smul(ell,I,q),q)

for q in (2,3):
    for t in range(q):
        for a in product(range(q),repeat=3):
            if not r(a,q): continue
            # Hom-Jacobi on basis triples.
            for X in basis:
                PX=phi(X,t,a,q)
                for Y in basis:
                    for Z in basis:
                        h=add3(bracket(PX,bracket(Y,Z,q),q),
                               bracket(phi(Y,t,a,q),bracket(Z,X,q),q),
                               bracket(phi(Z,t,a,q),bracket(X,Y,q),q),q)
                        assert all(v%q==0 for row in h for v in row)
    print({'q':q,'T3_hom_jacobi':'OK'})
print('VERIFY_OK')
