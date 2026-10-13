"""Independent finite-field multiplication fiber tests for the strictly upper-triangular 4x4 algebra.

No external packages; run: python verify_product_u4.py
"""
from collections import Counter
from itertools import product


def operations(q):
    if q in (2, 3, 5):
        add = lambda a, b: (a+b) % q
        mul = lambda a, b: (a*b) % q
    elif q == 4:
        # GF(4)=GF(2)[t]/(t*t+t+1), binary polynomial encoding
        add = lambda a,b: a ^ b
        def mul(a,b):
            z = 0
            for k in range(2):
                if (b >> k) & 1:
                    z ^= a << k
            if z & 8:
                z ^= 0b1110
            if z & 4:
                z ^= 0b111
            return z
    else:
        raise ValueError('unsupported field')
    return add, mul


def fibers(q):
    add,mul=operations(q)
    # X = (x12,x13,x14,x23,x24,x34)
    # Y = (y12,y13,y14,y23,y24,y34)
    # Each X,Y has three coordinates not used in XY. Account by q**6.
    base=Counter()
    for a,b,c in product(range(q),repeat=3):
        for d,e,f in product(range(q),repeat=3):
            # Note c=x23, d=y23, f=y34
            target=(mul(a,d),mul(c,f),add(mul(a,e),mul(b,f)))
            base[target]+=1
    return {z:q**6*n for z,n in base.items()}


def predicted(q,u,v,w):
    return q**6 * (q*(q-1)**2+q**2*(q-1)*((u==0)+(v==0))+q**4*(u==v==w==0))


def verify_direct(q):
    # Exhaustively multiply full 4x4 matrices (not reduced equations).
    add,mul=operations(q)
    coordinates=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)]
    words=list(product(range(q),repeat=6))
    mats=[]
    for v in words:
        mat=[[0]*4 for _ in range(4)]
        for (i,j),val in zip(coordinates,v): mat[i][j]=val
        mats.append(mat)
    histogram=Counter()
    for x in mats:
        for y in mats:
            m=[[0]*4 for _ in range(4)]
            for i in range(4):
                for k in range(i+1,4):
                    if x[i][k]:
                        for j in range(k+1,4):
                            m[i][j]=add(m[i][j],mul(x[i][k],y[k][j]))
            histogram[(m[0][2],m[1][3],m[0][3])]+=1
    expected=fibers(q)
    assert histogram==expected, (q,histogram,expected)
    print('direct-matrix-exhaustive',q,'pairs',q**12)


def check(q):
    allfib=fibers(q)
    assert len(allfib)==q**3
    assert sum(allfib.values())==q**12
    counts=Counter()
    for u,v,w in product(range(q),repeat=3):
        got=allfib[(u,v,w)]
        exp=predicted(q,u,v,w)
        assert got==exp,(q,u,v,w,got,exp)
        counts[got]+=1
    assert len(counts)==4 if q>1 else True
    print('q=',q,'targets=',q**3,'strata=',sorted(counts.items()),'total=',sum(allfib.values()))


if __name__=='__main__':
    for order in (2,3,4,5):
        check(order)
    for order in (2,3):
        verify_direct(order)
    print('VERIFY_OK_PRODUCT_U4')
