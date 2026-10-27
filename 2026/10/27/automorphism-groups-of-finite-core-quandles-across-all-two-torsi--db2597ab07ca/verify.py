"""Independent finite enumerations for automorphisms of Takasaki quandles.
No third-party packages are required. Run: python verify.py
"""
import itertools, math

def group(m,n):
    X=list(itertools.product(range(m), range(n)))
    idx={x:i for i,x in enumerate(X)}
    op=lambda a,b:((2*b[0]-a[0])%m,(2*b[1]-a[1])%n)
    table=[[idx[op(a,b)] for b in X] for a in X]
    return X,table

def count_direct(m,n):
    X,table=group(m,n)
    N=len(X)
    cnt=0
    for p in itertools.permutations(range(N)):
        if all(p[table[x][y]]==table[p[x]][p[y]] for x in range(N) for y in range(N)):
            cnt+=1
    return cnt

def aut_cyclic_twofactor(m,n):
    X,_=group(m,n)
    cnt=0
    for aa in itertools.product(X,repeat=2):
        def f(x):return ((aa[0][0]*x[0]+aa[1][0]*x[1])%m,(aa[0][1]*x[0]+aa[1][1]*x[1])%n)
        if m*aa[0][1]%n or n*aa[1][0]%m:continue
        if len(set(map(f,X)))==len(X):cnt+=1
    return cnt

def formula(m,n):
    X,_=group(m,n)
    H=sorted({((2*a)%m,(2*b)%n) for a,b in X})
    hset=set(H)
    # H is abstract isomorphic to Z_{m/gcd(2,m)} x Z_{n/gcd(2,n)}
    hm=m//math.gcd(m,2);hn=n//math.gcd(n,2)
    autH=aut_cyclic_twofactor(hm,hn)
    t=len({h for h in H if ((2*h[0])%m,(2*h[1])%n)==(0,0)})
    q=len(X)//len(H)
    assert q%t==0
    u=q//t
    order=len(X)*autH*math.factorial(u-1)*(math.factorial(u)**(t-1))*(t**(q-1))
    return order,dict(group_order=len(X),H_order=len(H),AutH=autH,u=u,t=t)

def check_direct():
    for m,n in [(1,1),(1,3),(2,2),(2,3),(2,4),(4,2),(1,8),(1,6),(2,1),(3,1)]:
        if m*n>8:continue
        direct=count_direct(m,n)
        value,meta=formula(m,n)
        assert direct==value,(m,n,direct,value,meta)
        print('direct',m,n,direct,meta)

def check_constructive(m,n):
    X,table=group(m,n)
    N=len(X);idx={x:i for i,x in enumerate(X)}
    H=set(((2*a)%m,(2*b)%n) for a,b in X)
    # select base representives of quotient by H
    rem=set(X); reps=[]
    while rem:
        a=min(rem);reps.append(a)
        rem-={((a[0]+h[0])%m,(a[1]+h[1])%n) for h in H}
    zero=(0,0)
    if zero in reps:reps.remove(zero);reps.insert(0,zero)
    def add(a,b):return ((a[0]+b[0])%m,(a[1]+b[1])%n)
    def dbl(a):return add(a,a)
    def neg(a):return ((-a[0])%m,(-a[1])%n)
    def sub(a,b):return add(a,neg(b))
    # Derive actual Aut(H) by counting homomorphisms (without assuming it comes from G)
    hm=m//math.gcd(m,2);hn=n//math.gcd(n,2)
    # group H may have redundant represented labels, enumerate maps H->H
    Hs=sorted(H); Hidx={x:i for i,x in enumerate(Hs)}
    maps=[]
    for p in itertools.permutations(Hs):
        F=dict(zip(Hs,p))
        if F[zero]!=zero:continue
        if all(F[add(x,y)]==add(F[x],F[y]) for x in Hs for y in Hs): maps.append(F)
    for L in maps:
        base=[]
        for a in reps:
            base.append([b for b in X if dbl(b)==L[dbl(a)]])
        # choice constraints, first rep b0=0, other reps any, all must map to distinct quotient cosets
        num=0
        for vals in itertools.product(*base[1:]):
            bs=[zero]+list(vals)
            cs=[frozenset(add(b,h) for h in H) for b in bs]
            if len(set(cs))<len(cs):continue
            f={}
            for a,b in zip(reps,bs):
                for h in H:
                    f[add(a,h)]=add(b,L[h])
            assert len(f)==N and len(set(f.values()))==N
            assert all(f[X[table[i][j]]]==X[table[idx[f[X[i]]]][idx[f[X[j]]]]] for i in range(N) for j in range(N))
            num+=1
        q=N//len(H)
        t=len([x for x in H if dbl(x)==zero]);u=q//t
        expected=math.factorial(u-1)*math.factorial(u)**(t-1)*t**(q-1)
        assert num==expected,(m,n,num,expected)
    assert len(maps)==aut_cyclic_twofactor(hm,hn)
    assert N*len(maps)*expected==formula(m,n)[0]
    print('construct',m,n,formula(m,n)[0],'stabilizer',len(maps)*expected)

if __name__=='__main__':
    check_direct()
    for m,n in [(2,4),(4,2),(4,4),(2,6),(4,6)]:
        if m*n<=16:check_constructive(m,n)
        else:print('formula',m,n,formula(m,n))
    print('VERIFY_OK')
