"""Reproduce rank identities for binary neighbor-parity on finite projective-plane incidence graphs.

Run with Python 3.10+ and no third-party packages: python verify.py
"""
from itertools import product


def field(q):
    if q in (2, 3, 5, 7):
        return (lambda a,b: (a+b)%q,
                lambda a,b: (a*b)%q,
                lambda a: pow(a, q-2, q))
    if q in (4, 8):
        pol = {4: 0b111, 8: 0b1011}[q]
        def add(a,b): return a^b
        def mul(a,b):
            out=0
            while b:
                if b&1: out^=a
                b>>=1
                a<<=1
                if a&q: a^=pol
            return out
        def pw(a,e):
            out=1
            while e:
                if e&1: out=mul(out,a)
                a=mul(a,a); e>>=1
            return out
        return add,mul,lambda a: pw(a,q-2)
    if q==9:
        # GF(9) = F_3[t]/(t^2+1), encoding a+3b*t.
        def add(a,b):return ((a%3+b%3)%3)+3*((a//3+b//3)%3)
        def mul(a,b):
            x,y=a%3,a//3
            u,v=b%3,b//3
            return (x*u-y*v)%3 + 3*((x*v+y*u)%3)
        def pw(a,e):
            out=1
            while e:
                if e&1:out=mul(out,a)
                a=mul(a,a);e>>=1
            return out
        return add,mul,lambda a:pw(a,7)
    raise ValueError(q)


def projective_incidence(q):
    add,mul,inv=field(q)
    reps=[]; seen=set()
    for triple in product(range(q),repeat=3):
        if triple==(0,0,0):continue
        k=next(x for x in triple if x)
        normal=tuple(mul(x,inv(k)) for x in triple)
        if normal not in seen:
            seen.add(normal);reps.append(normal)
    v=q*q+q+1
    assert len(reps)==v
    rows=[]
    for p in reps:
        mask=0
        for j,l in enumerate(reps):
            z=0
            for x,y in zip(p,l):z=add(z,mul(x,y))
            if z==0:mask|=1<<j
        assert mask.bit_count()==q+1
        rows.append(mask)
    return rows


def rank(rows):
    pivots={}
    for vec in rows:
        while vec:
            b=vec.bit_length()-1
            if b not in pivots:
                pivots[b]=vec
                break
            vec ^= pivots[b]
    return len(pivots)


def mul_mats(rows1,rows2):
    out=[]
    for vec in rows1:
        z=0
        while vec:
            low=vec&-vec
            i=low.bit_length()-1
            z^=rows2[i]
            vec^=low
        out.append(z)
    return out


def apply(rows,x):
    return sum(((mask & x).bit_count()&1)<<i for i,mask in enumerate(rows))


def test_q(q):
    B=projective_incidence(q)
    v=q*q+q+1
    cols=[sum(((B[i]>>j)&1)<<i for i in range(v)) for j in range(v)]
    A=[m<<v for m in B]+cols
    m=2*v
    eye=[1<<i for i in range(m)]
    square=mul_mats(A,A)
    cube=mul_mats(square,A)
    fourth=mul_mats(square,square)
    rho=rank(B)
    if q%2:
        assert rho==v-1
        assert rank(A)==2*(v-1)
        assert rank(square)==2*(v-1)
        assert cube==A
        expected=[((1<<m)-1)^(1<<i) for i in range(v)]
        # Matrix identity A^2 = diag(I+J,I+J)
        jm=(1<<v)-1
        assert square==[((jm^(1<<i))) for i in range(v)]+[((jm^(1<<i))<<v) for i in range(v)]
        recurrent_dim=2*(v-1)
        fixed_dim=v-1
        deadline=1
        first_entry_counts=[1<<recurrent_dim,(1<<m)-(1<<recurrent_dim)]
    else:
        assert rank(A)==2*rho
        assert rank(square)==2
        jm=(1<<v)-1
        assert square==[jm for _ in range(v)]+[jm<<v for _ in range(v)]
        assert rho <= (v+1)//2
        recurrent_dim=2
        fixed_dim=1
        deadline=2
        first_entry_counts=[4,(1<<(m-2*rho+2))-4,(1<<m)-(1<<(m-2*rho+2))]
        if q in (2,4,8):
            assert rho==3**({2:1,4:2,8:3}[q])+1
    assert fourth==square
    assert m-rank([A[i]^eye[i] for i in range(m)])==fixed_dim
    assert m-rank([square[i]^eye[i] for i in range(m)])==recurrent_dim
    assert sum(first_entry_counts)==1<<m
    if q==2:
        counts=[0,0,0]
        for s in range(1<<m):
            x=s
            for t in range(3):
                y=apply(square,x)
                if y==x:
                    counts[t]+=1
                    break
                x=apply(A,x)
            else: raise AssertionError('non-periodic at t=2')
        assert counts==first_entry_counts
        print('exhaustive labelled states q=2:',sum(counts))
    # Each state reaches a periodic orbit by the asserted deadline.
    for seed in range(129):
        x=((seed+1)*0x9e3779b97f4a7c15 +seed*seed*0x10001)&((1<<m)-1)
        for _ in range(deadline):x=apply(A,x)
        assert apply(square,x)==x
    print(f'q={q}, points={v}, binary incidence rank={rho}, adjacency ranks=({rank(A)},{rank(square)}), '
          f'periodic states=2^{recurrent_dim}, fixed states=2^{fixed_dim}, '
          f'exact entry-counts={first_entry_counts}')


if __name__=='__main__':
    for q in (2,3,4,5,7,8,9):test_q(q)
    print('PROJECTIVE_PLANE_PARITY_VERIFY_OK')
