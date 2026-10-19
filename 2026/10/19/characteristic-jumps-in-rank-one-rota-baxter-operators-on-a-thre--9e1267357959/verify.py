"""Independent finite-field checks for rank-one weight-zero Rota--Baxter operators on the three-generator exterior algebra.

Requires only the Python standard library. Run `python verify_exterior_rankone.py`.
"""
from itertools import product

DIM = 8


def mul_basis(a,b,p):
    if a & b:
        return None,0
    inversions = sum(1 for i in range(3) for j in range(i) if (a >> i)&1 and (b >> j)&1)
    return a | b, (-1 if inversions%2 else 1)%p


def mul(x,y,p):
    out=[0]*DIM
    for i,a in enumerate(x):
        if not a: continue
        for j,b in enumerate(y):
            if not b: continue
            k,s=mul_basis(i,j,p)
            if k is not None:out[k]=(out[k]+a*b*s)%p
    return tuple(out)


def span_rank(columns,p):
    A=[list(c) for c in columns]
    pivots=[]
    for v in A:
        for j,r in pivots:
            if v[j]:
                s=v[j]
                v=[(a-s*b)%p for a,b in zip(v,r)]
        if any(v):
            j=next(i for i,z in enumerate(v) if z)
            s=pow(v[j],-1,p)
            v=[(z*s)%p for z in v]
            # Keep pivots sorted to preserve reduction invariant.
            pivots.append((j,v));pivots.sort(key=lambda x:x[0])
    return len(pivots)


def normalized_lines(p):
    for first in range(DIM):
        for tail in product(range(p),repeat=DIM-first-1):
            yield (0,)*first+(1,)+tail


def theoretical(p):
    t=p*p+p+1
    high=(p**4 if p==2 else p**3)*t
    middle=p*t
    low=1
    return {(4,1):high,(2,2):middle,(1,3):low}


def check(p):
    # p prime (the theorem itself also holds over prime-power fields).
    bs=[tuple(int(i==j) for i in range(DIM)) for j in range(DIM)]
    counts={}
    bad=[]
    for u in normalized_lines(p):
        if any(mul(u,u,p)):
            continue
        ideal=[mul(u,b,p) for b in bs]+[mul(b,u,p) for b in bs]
        r=span_rank(ideal,p)
        # Bit-count of a basis-mask equals exterior degree.
        order=min(i.bit_count() for i,c in enumerate(u) if c and i)
        counts[(r,order)]=counts.get((r,order),0)+1
        if (r,order) not in {(4,1),(2,2),(1,3)}:bad.append((u,r,order))
    expected=theoretical(p)
    assert not bad,bad[:3]
    assert counts==expected,(p,counts,expected)
    total=sum(num*(p**(DIM-r)-1) for (r,d),num in counts.items())
    predicted=sum(num*(p**(DIM-r)-1) for (r,d),num in expected.items())
    assert total==predicted
    return counts,total


if __name__=='__main__':
    for p in [2,3,5]:
        counts,total=check(p)
        print('p=',p,'projective square-zero lines by (ideal-rank, lowest exterior-degree)=',counts,'rank-one RB operators=',total)
    print('PASS: all tested square-zero images exhaust the three predicted strata; counts agree exactly.')


def direct_count_binary():
    """Independently test the complete identity on basis pairs for EVERY binary rank-one map."""
    p=2
    bs=[tuple(int(i==j) for i in range(DIM)) for j in range(DIM)]
    forms=list(product(range(p),repeat=DIM))[1:]
    number=0
    for u in normalized_lines(p):
        ux=[mul(u,b,p) for b in bs]
        xu=[mul(b,u,p) for b in bs]
        uu=mul(u,u,p)
        for f in forms:
            def dot(v): return sum(a*b for a,b in zip(f,v))%p
            left=[dot(v) for v in ux]
            right=[dot(v) for v in xu]
            good=True
            for i in range(DIM):
                if not good:break
                for j in range(DIM):
                    coefficient=(f[i]*left[j]+f[j]*right[i])%p
                    # This is the original Rota--Baxter identity on basis elements,
                    # without imposing the square-zero/annihilator characterization.
                    if any((f[i]*f[j]*uu[k]-coefficient*u[k])%p for k in range(DIM)):
                        good=False
                        break
            if good:number+=1
    assert number==2689,number
    return number

if __name__ == '__main__':
    print('Exhaustive independent binary identity count:',direct_count_binary())

# Separate extension-field check, using F_4 = F_2[z]/(z^2+z+1).
def gf4_mul(a,b):
    t=((a&1)*(b&1)) ^ ((((a>>1)&1)*((b>>1)&1))<<0)
    t ^= (((a&1)*((b>>1)&1)) ^ (((a>>1)&1)*(b&1)) ^ (((a>>1)&1)*((b>>1)&1)))<<1
    return t


def gf4_rank(columns):
    pivots={}
    for col in columns:
        v=list(col)
        for k in sorted(pivots):
            if v[k]:
                t=v[k]
                v=[a ^ gf4_mul(t,b) for a,b in zip(v,pivots[k])]
        for k in range(DIM):
            if v[k]:
                inv=next(x for x in (1,2,3) if gf4_mul(v[k],x)==1)
                pivots[k]=[gf4_mul(x,inv) for x in v]
                break
    return len(pivots)


def gf4_mult(x,y):
    out=[0]*DIM
    for i,a in enumerate(x):
        if not a:continue
        for j,b in enumerate(y):
            if a and b and not i&j:
                out[i|j] ^= gf4_mul(a,b)
    return out


def gf4_check():
    q=4
    b=[[int(i==j) for i in range(DIM)] for j in range(DIM)]
    counts={}
    for u in normalized_lines(q):
        if any(gf4_mult(u,u)):
            continue
        I=[gf4_mult(u,e) for e in b]+[gf4_mult(e,u) for e in b]
        r=gf4_rank(I)
        d=min(i.bit_count() for i,x in enumerate(u) if x and i)
        counts[(r,d)]=counts.get((r,d),0)+1
    expected={(4,1):q**4*(q*q+q+1),(2,2):q*(q*q+q+1),(1,3):1}
    assert counts==expected,(counts,expected)
    total=sum(n*(q**(DIM-r)-1) for (r,d),n in counts.items())
    print('F4: projective strata=',counts,'rank-one RB operators=',total)

if __name__ == '__main__':
    gf4_check()
