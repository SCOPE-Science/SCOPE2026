from collections import defaultdict, Counter

def field(q):
    if q in (2,3,5,7):
        p=q
        def add(a,b):return (a+b)%q
        def mul(a,b):return a*b%q
        def inv(a):return pow(a,q-2,q)
        primitive=next(a for a in range(1,q) if {pow(a,i,q) for i in range(q-1)}==set(range(1,q)))
        return add,mul,inv,primitive,[1]
    if q in (4,8):
        mod=(0b111 if q==4 else 0b1011);n=q.bit_length()-1
        def add(a,b):return a^b
        def mul(a,b):
            z=0
            for i in range(n):
                if b>>i&1:z^=a<<i
            for i in range(2*n-2,n-1,-1):
                if z>>i&1:z^=mod<<(i-n)
            return z
        def power(a,t):
            z=1
            while t:
                if t&1:z=mul(z,a)
                a=mul(a,a);t//=2
            return z
        def inv(a):return power(a,q-2)
        primitive=next(a for a in range(1,q) if {power(a,i) for i in range(q-1)}==set(range(1,q)))
        return add,mul,inv,primitive,[1<<i for i in range(n)]
    raise ValueError(q)

def subalgebras(q):
    ad,mu,iv,prim,basis=field(q)
    z=(0,)*5
    def V(*pairs):
        v=[0]*5
        for i,c in pairs:v[i-1]=c
        return tuple(v)
    out={}
    def put(rows):
        rows=tuple(rows);assert rows not in out
        out[rows]=None
    put([])
    put([V((1,1)),V((2,1)),V((3,1)),V((4,1)),V((5,1))])
    put([V((2,1)),V((3,1)),V((4,1)),V((5,1))])
    put([V((3,1)),V((4,1)),V((5,1))])
    put([V((4,1)),V((5,1))]);put([V((5,1))])
    for u in range(q):
        for v in range(q):
            put([V((2,1),(3,u),(5,v)),V((4,1),(5,ad(u,u)))])
            put([V((3,1),(4,u),(5,v))])
            put([V((3,1),(5,u)),V((4,1),(5,v))])
        put([V((2,1),(3,u)),V((4,1)),V((5,1))])
        put([V((3,1),(4,u)),V((5,1))])
        put([V((4,1),(5,u))])
    assert len(out)==3*q*q+3*q+6,(len(out),q)
    return set(out)

def rref(rows,q):
    ad,mu,iv,pr,ba=field(q)
    v=[list(w) for w in rows]
    k=0
    for j in range(5):
        pivot=next((i for i in range(k,len(v)) if v[i][j]),None)
        if pivot is None:continue
        v[k],v[pivot]=v[pivot],v[k]
        inv=iv(v[k][j]);v[k]=[mu(a,inv) for a in v[k]]
        for i in range(len(v)):
            if i!=k and v[i][j]:
                factor=v[i][j]
                v[i]=[ad(x,mu((-factor)%q if q in (2,3,5,7) else factor,y)) for x,y in zip(v[i],v[k])]
        k+=1
        if k==len(v):break
    return tuple(tuple(row) for row in v[:k])

def orbit_census(q):
    ad,mu,iv,pr,ba=field(q)
    S=subalgebras(q)
    gs=[(pr,0,0,0,0)]
    for i in range(1,5):
        for z in ba:
            w=[0]*5;w[0]=1;w[i]=z;gs.append(tuple(w))
    def multiply(x,y):
        z=[0]*6
        for i,a in enumerate(x):
            for j,b in enumerate(y):
                if i+j<=5:z[i+j]=ad(z[i+j],mu(a,b))
        return z
    def transform(rows,g):
        pow_g=[[1]+[0]*5]
        for i in range(1,6):pow_g.append(multiply(pow_g[-1],(0,)+g))
        transformed=[]
        for row in rows:
            t=[0]*5
            for i,c in enumerate(row):
                for j in range(1,6):t[j-1]=ad(t[j-1],mu(c,pow_g[i+1][j]))
            transformed.append(t)
        return rref(transformed,q)
    for g in gs:
        for rows in S:
            im=transform(rows,g)
            assert im in S,('bad-image',q,rows,g,im)
    out={};bytype=defaultdict(list)
    while S:
        start=next(iter(S));orb={start};queue=[start]
        for x in queue:
            for g in gs:
                y=transform(x,g)
                if y not in orb:orb.add(y);queue.append(y)
        assert orb<=S
        S-=orb
        piv=tuple(next(i+1 for i,x in enumerate(row) if x) for row in start)
        bytype[piv].append(len(orb))
    for x in bytype:bytype[x].sort()
    expected={():[1],(1,2,3,4,5):[1],(2,3,4,5):[1],(3,4,5):[1],(4,5):[1],(5,):[1]}
    if q%2==0:
        g=__import__('math').gcd(3,q-1)
        expected.update({(2,4):sorted([1]+[(q-1)//g]*g+[q*(q-1)]),(2,4,5):sorted([1,q-1]),(3,):[q*q],(3,4):sorted([q,q*(q-1)]),(3,5):[q],(4,):sorted([1,q-1])})
        target=16+g
    elif q==3:
        expected.update({(2,4):[q*q],(2,4,5):[q],(3,):sorted([1,(q-1)//2,(q-1)//2,q*(q-1)]),(3,4):sorted([q,q*(q-1)//2,q*(q-1)//2]),(3,5):sorted([1,q-1]),(4,):[q]})
        target=18
    else:
        expected.update({(2,4):[q*q],(2,4,5):[q],(3,):[q*q],(3,4):[q*q],(3,5):[q],(4,):[q]})
        target=12
    assert dict(bytype)==expected,('spectrum-mismatch',q,dict(bytype),expected)
    assert sum(map(len,bytype.values()))==target
    assert sum(sum(z) for z in bytype.values())==6+3*q+3*q*q
    print('q',q,'orbits',target,'sum',6+3*q+3*q*q,'distribution',dict(sorted(bytype.items())),flush=True)

if __name__=='__main__':
  for q in (2,3,4,5,7,8):orbit_census(q)
  print('VERIFY_OK')

# The finite examples below are independent checks, not a proof over all fields.
