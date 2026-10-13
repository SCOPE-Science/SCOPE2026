"""Independent finite-field enumeration for subalgebras of characteristic-two short symplectic local rings."""
import itertools
import math
from collections import Counter, defaultdict

IRRED={2:0b11,4:0b111,8:0b1011}

def gf_mul(a,b,q):
    deg=q.bit_length()-1
    mod=IRRED[q]
    out=0
    while b:
        if b & 1:
            out ^= a
        b >>= 1
        a <<= 1
        if a & q:
            a ^= mod
    return out

def gf_pow(a,k,q):
    r=1
    while k:
        if k&1: r=gf_mul(r,a,q)
        a=gf_mul(a,a,q)
        k>>=1
    return r

def gf_inv(a,q):
    assert a
    return gf_pow(a,q-2,q)

def rref(rows,n,q):
    rows=[list(v) for v in rows]
    pivots=[]
    i=0
    for j in range(n):
        k=next((k for k in range(i,len(rows)) if rows[k][j]),None)
        if k is None: continue
        rows[i],rows[k]=rows[k],rows[i]
        inv=gf_inv(rows[i][j],q)
        rows[i]=[gf_mul(inv,x,q) for x in rows[i]]
        for k in range(len(rows)):
            if k!=i and rows[k][j]:
                a=rows[k][j]
                rows[k]=[x^gf_mul(a,y,q) for x,y in zip(rows[k],rows[i])]
        pivots.append(j)
        i+=1
        if i==len(rows):break
    return tuple(tuple(row) for row in rows[:i])

def all_subspaces(n,q):
    for k in range(n+1):
        for ps in itertools.combinations(range(n),k):
            nonp=[j for j in range(n) if j not in ps]
            pos=[(i,j) for i,p in enumerate(ps) for j in nonp if j>p]
            for vals in itertools.product(range(q),repeat=len(pos)):
                rows=[[0]*n for _ in range(k)]
                for i,p in enumerate(ps):rows[i][p]=1
                for (i,j),val in zip(pos,vals):rows[i][j]=val
                yield tuple(tuple(row) for row in rows)

def B(u,v,m,q):
    out=0
    for i in range(m):
        out ^= gf_mul(u[2*i],v[2*i+1],q) ^ gf_mul(u[2*i+1],v[2*i],q)
    return out

def has_z(rows,n,q):
    z=(0,)*(n-1)+(1,)
    return len(rref(rows+(z,),n,q))==len(rows)

def inv_num(m,d,q):
    if not (0<=d<=m):return 0
    num=den=1
    for i in range(d):
        num *= q**(2*m-i)-q**i
        den *= q**d-q**i
    assert num % den==0
    return num//den

def sp_order(m,q):
    return q**(m*m)*math.prod(q**(2*i)-1 for i in range(1,m+1))

def orbit_size_type1(m,r,s,q):
    N=m-r
    return inv_num(m,r,q)*(sp_order(N,q)//(sp_order(s,q)*sp_order(N-s,q)))

def gauss(n,k,q):
    if k<0 or k>n:return 0
    num=den=1
    for i in range(k):
        num*=q**(n-i)-1
        den*=q**(k-i)-1
    assert num%den==0
    return num//den

def theoretical(m,q):
    types={}
    for r in range(m+1):
        for s in range(m-r+1):
            types[('Z',r+2*s,r)]=orbit_size_type1(m,r,s,q)
    for d in range(m+1):
        types[('F',d)]=q**d*inv_num(m,d,q)
    total=sum(types.values())
    assert total==sum(gauss(2*m,d,q) for d in range(2*m+1))+sum(q**d*inv_num(m,d,q) for d in range(m+1))
    assert len(types)==(m+1)*(m+4)//2
    return types

def enumerate_algebra(m,q):
    n=2*m+1
    count=Counter()
    subspaces=[]
    for U in all_subspaces(n,q):
        if has_z(U,n,q):
            L=rref(tuple(u[:-1] for u in U),n-1,q)
            d=len(L)
            rank=len(rref(tuple(tuple(B(u,v,m,q) for v in L) for u in L),d,q)) if d else 0
            assert rank%2==0
            typ=('Z',d,d-rank)
        else:
            if any(B(u,v,m,q) for u in U for v in U):continue
            typ=('F',len(U))
        count[typ]+=1
        subspaces.append(U)
    predicted=theoretical(m,q)
    assert dict(count)==predicted,(m,q,count,predicted)
    return subspaces,predicted

def transform(U,m,q,kind,v,scale=1):
    n=2*m+1
    out=[]
    for u in U:
        x=list(u)
        if kind=='t':
            # symplectic transvection w -> w + scale * B(w,v) v
            c=gf_mul(scale,B(u,v,m,q),q)
            for i in range(2*m):x[i]^=gf_mul(c,v[i],q)
        elif kind=='l':
            # central shear w -> w + v(w)*z
            c=0
            for i in range(2*m):c ^=gf_mul(u[i],v[i],q)
            x[-1]^=c
        else:raise ValueError
        out.append(tuple(x))
    return rref(tuple(out),n,q)

def orbit_check(m,q,subspaces):
    # Small cases: use transvections in each nonzero direction and all linear central shears.
    n=2*m+1
    gens=[]
    for v in itertools.product(range(q),repeat=2*m):
        if not any(v):continue
        for a in range(1,q):gens.append(('t',v,a))
    for j in range(2*m):
        v=[0]*(2*m);v[j]=1
        gens.append(('l',tuple(v),1))
    todo=set(subspaces)
    sizes=[]
    while todo:
        a=next(iter(todo)); todo.remove(a)
        queue=[a]
        for cur in queue:
            for kind,v,sc in gens:
                w=transform(cur,m,q,kind,v,sc)
                if w in todo:
                    todo.remove(w);queue.append(w)
        sizes.append(len(queue))
    expected=Counter(theoretical(m,q).values())
    assert Counter(sizes)==expected,(m,q,sorted(sizes),expected)
    return sorted(sizes)

if __name__=='__main__':
    for m,q in [(1,2),(1,4),(1,8),(2,2),(2,4),(3,2)]:
        subs,classes=enumerate_algebra(m,q)
        if (m,q) in [(1,2),(1,4),(2,2),(3,2)]:orbits=orbit_check(m,q,subs)
        else:orbits='not computed'
        print(f'm={m} q={q}: subalgebras={len(subs)} class-count={len(classes)}, orbit-sizes={orbits}',flush=True)
    print('VERIFY_OK')
