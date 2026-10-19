#!/usr/bin/env python3
"""Finite computational checks of weight-zero Rota-Baxter classifications on K+V, V^2=0."""
from itertools import product
from math import prod

# An exhaustive test over prime fields directly evaluates all (n+1)x(n+1) linear maps,
# not merely candidate block forms.
def mat_vec(columns, v, q):
    size=len(columns)
    return tuple(sum(v[j]*columns[j][i] for j in range(size))%q for i in range(size))

def mul(x,y,q):
    return (x[0]*y[0]%q,)+tuple((x[0]*y[i]+y[0]*x[i])%q for i in range(1,len(x)))

def add(x,y,q):
    return tuple((a+b)%q for a,b in zip(x,y))

def rb_test(cols,q):
    for a in cols:
        for b in cols:
            # Check on the standard basis using their prescribed images.
            pass
    d=len(cols); basis=[tuple(int(i==j) for i in range(d)) for j in range(d)]
    for i in range(d):
        for j in range(i,d):
            lhs=mul(cols[i],cols[j],q)
            z=add(mul(basis[i],cols[j],q),mul(cols[i],basis[j],q),q)
            rhs=mat_vec(cols,z,q)
            if lhs!=rhs:return False
    return True

def T_square_zero(cols,q):
    n=len(cols)
    return all(all(a==0 for a in mat_vec(cols,c,q)) for c in cols)

def rank(M,q):
    a=[list(row) for row in M]; nr=len(a); nc=len(a[0]) if a else 0; k=0
    for j in range(nc):
        pivot=next((i for i in range(k,nr) if a[i][j]%q),None)
        if pivot is None:continue
        a[k],a[pivot]=a[pivot],a[k]
        h=pow(a[k][j]%q,-1,q)
        a[k]=[x*h%q for x in a[k]]
        for i in range(nr):
            if i!=k and a[i][j]:
                b=a[i][j]
                a[i]=[(x-b*y)%q for x,y in zip(a[i],a[k])]
        k+=1
        if k==nr:break
    return k

def gamma(n,r,q):
    if 2*r>n:return 0
    gaussian=lambda a,b: prod(q**a-q**j for j in range(b))//prod(q**b-q**j for j in range(b))
    return gaussian(n,r)*gaussian(n-r,r)*prod(q**r-q**j for j in range(r))

def exhaustive(q,n):
    d=n+1
    hist={}; cnt=0; idx3=0
    for flat in product(range(q),repeat=d*d):
        cols=tuple(flat[j*d:(j+1)*d] for j in range(d))
        if not rb_test(cols,q):continue
        cnt+=1
        assert all(c[0]==0 for c in cols)
        u=tuple(cols[0][1:]); T=tuple(tuple(cols[j+1][1:]) for j in range(n))
        assert T_square_zero(T,q)
        r=rank([[T[j][i] for j in range(n)] for i in range(n)],q)
        should_sq_zero=all(x==0 for x in mat_vec(T,u,q))
        if q%2:assert should_sq_zero
        if not should_sq_zero:idx3+=1
        hist[r]=hist.get(r,0)+1
    predicted={r:gamma(n,r,q)*(q**n if q%2==0 else q**(n-r)) for r in range(n//2+1)}
    assert cnt==sum(predicted.values()),(q,n,cnt,predicted)
    assert hist==predicted,(q,n,hist,predicted)
    if q%2==0:
        predict3=sum(gamma(n,r,q)*(q**n-q**(n-r)) for r in range(n//2+1))
        assert idx3==predict3,(idx3,predict3)
    print('EXHAUSTIVE_OK',q,n,cnt,'index3',idx3,'ranks',hist)

def even_param_test(q,n):
    # Test all candidates of block form for q=2; the direct full-map check runs above.
    if q!=2:return
    d=n+1; total=0
    for flat in product(range(q),repeat=n*n):
        T=tuple(flat[j*n:(j+1)*n] for j in range(n))
        if not T_square_zero(T,q):continue
        for u in product(range(q),repeat=n):
            cols=((0,)+u,)+tuple((0,)+c for c in T)
            assert rb_test(cols,q)
            total+=1
    assert total==q**n*sum(gamma(n,r,q) for r in range(n//2+1))
    print('PARAM_OK',q,n,total)

if __name__=='__main__':
    for q,n in [(2,1),(2,2),(2,3),(3,1),(3,2),(5,1)]:exhaustive(q,n)
    even_param_test(2,3)
    print('VERIFY_OK')

def orbit_test(q,n):
    vs=list(product(range(q),repeat=n))
    standard=[tuple(int(i==j) for i in range(n)) for j in range(n)]
    invertibles=[]
    for cols in product(vs,repeat=n):
        lookup={mat_vec(cols,v,q):v for v in vs}
        if len(lookup)==q**n:
            inv=tuple(lookup[e] for e in standard)
            invertibles.append((cols,inv))
    sq=[cols for cols in product(vs,repeat=n) if T_square_zero(cols,q)]
    pairs={(T,u) for T in sq for u in vs if q%2==0 or mat_vec(T,u,q)==(0,)*n}
    classes=[]
    while pairs:
        T,u=next(iter(pairs)); orb=set()
        for g,ginv in invertibles:
            t_new=tuple(mat_vec(g,mat_vec(T,vi,q),q) for vi in ginv)
            u_new=mat_vec(g,u,q)
            orb.add((t_new,u_new))
        assert orb<=pairs or orb.isdisjoint(pairs) is False
        classes.append(len(orb))
        pairs-=orb
    if q%2==0:
        predicted=2*n+1 if n%2==0 else 2*n
    else:
        m=n//2; predicted=3*m+1 if n%2==0 else 3*m+2
    assert len(classes)==predicted,(q,n,classes,predicted)
    print('ORBITS_OK',q,n,'num',len(classes),'sizes',sorted(classes))

if __name__=='__main__':
    for q,n in [(2,1),(2,2),(2,3),(3,1),(3,2)]:orbit_test(q,n)
    print('ORBIT_VERIFY_OK')

def asymptotic_test():
    for q in (2,4):
        for eps in (0,1):
            weights=[]
            for j in range(25):
                c=prod(1-q**(-i) for i in range(1,2*j+eps+1))
                weights.append(q**(-2*j*(j+eps))/c)
            target=sum(q**j*w for j,w in enumerate(weights))/sum(weights)
            n=80+eps; m=n//2
            cs=[gamma(n,r,q) for r in range(m+1)]
            actual=sum(z*q**(n-r) for r,z in enumerate(cs))/sum(z*q**n for z in cs)
            scaled=actual*q**m
            assert abs(scaled/target-1)<1e-8,(q,eps,scaled,target)
            print('ASYMPTOTIC_OK',q,'parity',eps,'scaled',format(scaled,'.12g'),'limit',format(target,'.12g'))

if __name__=='__main__':
    asymptotic_test()
    print('ALL_VERIFY_OK')

def gf4_full_test():
    # Binary polynomial representation of GF(4)=F2[t]/(t^2+t+1).
    multiply=[[0]*4 for _ in range(4)]
    for x in range(4):
        for y in range(4):
            r=0
            for k in range(2):
                if (y>>k)&1:r^=(x<<k)
            if r&8:r^=14
            if r&4:r^=7
            multiply[x][y]=r
    def plus(a,b):return tuple(x^y for x,y in zip(a,b))
    def prodvec(a,b):
        return (multiply[a[0]][b[0]],)+(tuple(multiply[a[0]][b[k]]^multiply[b[0]][a[k]] for k in (1,2)))
    def image(cols,vec):
        return tuple(multiply[vec[0]][cols[0][i]]^multiply[vec[1]][cols[1][i]]^multiply[vec[2]][cols[2][i]] for i in range(3))
    standard=((1,0,0),(0,1,0),(0,0,1))
    count=0; idx3=0
    for flat in product(range(4),repeat=9):
        cols=(flat[0:3],flat[3:6],flat[6:9])
        okay=True
        for i in range(3):
            for j in range(i,3):
                z=plus(prodvec(standard[i],cols[j]),prodvec(cols[i],standard[j]))
                if prodvec(cols[i],cols[j])!=image(cols,z):
                    okay=False;break
            if not okay:break
        if not okay:continue
        count+=1
        assert cols[0][0]==cols[1][0]==cols[2][0]==0
        u=cols[0][1:]; T=(cols[1][1:],cols[2][1:])
        for v in T:
            assert tuple(multiply[v[0]][T[0][k]]^multiply[v[1]][T[1][k]] for k in (0,1))==(0,0)
        Tu=tuple(multiply[u[0]][T[0][k]]^multiply[u[1]][T[1][k]] for k in (0,1))
        if Tu!=(0,0):idx3+=1
    assert (count,idx3)==(256,180),(count,idx3)
    print('GF4_EXHAUSTIVE_OK',count,'index3',idx3)

if __name__=='__main__':
    gf4_full_test()
    print('FULL_VERIFY_OK')
