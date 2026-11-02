"""Independent finite-field enumeration for M_2 anticommutator operators.
No mathematical assertion about infinite fields is inferred from these tests.
"""
from itertools import product
from collections import Counter

def add(a,b): return a^b

def mul(a,b,q):
    z=0
    while b:
        if b&1: z^=a
        b>>=1;a<<=1
        if a&q: a^=(q|3) if q==4 else (q|3) # F2 x+1, F4 x^2+x+1
    return z

def mm(A,B,q):
    a,b,c,d=A;e,f,g,h=B
    return (add(mul(a,e,q),mul(c,h,q)),add(mul(b,f,q),mul(d,g,q)),add(mul(a,g,q),mul(c,f,q)),add(mul(d,e,q),mul(b,h,q)))

def adj(A,q):
    basis=((1,0,0,0),(0,1,0,0),(0,0,1,0),(0,0,0,1))
    columns=[]
    for X in basis:
        U,V=mm(A,X,q),mm(X,A,q)
        columns.append(tuple(add(u,v) for u,v in zip(U,V)))
    return tuple(tuple(columns[j][i] for j in range(4)) for i in range(4))

def comp(X,Y,q):
    return tuple(tuple(add(add(mul(X[i][0],Y[0][j],q),mul(X[i][1],Y[1][j],q)),add(mul(X[i][2],Y[2][j],q),mul(X[i][3],Y[3][j],q))) for j in range(4)) for i in range(4))

def rank(A,q):
    M=[list(row) for row in A];r=0
    for c in range(4):
        ii=next((i for i in range(r,4) if M[i][c]),None)
        if ii is None:continue
        M[r],M[ii]=M[ii],M[r]; inv=next(t for t in range(1,q) if mul(t,M[r][c],q)==1)
        M[r]=[mul(v,inv,q) for v in M[r]]
        for i in range(4):
            if i!=r and M[i][c]:
                v=M[i][c];M[i]=[add(M[i][j],mul(v,M[r][j],q)) for j in range(4)]
        r+=1
    return r

def verify(q):
    I=tuple(tuple(int(i==j) for j in range(4)) for i in range(4))
    generators={adj(A,q) for A in product(range(q),repeat=4)}
    pairs={comp(A,B,q) for A in generators for B in generators}
    S={I}|generators|pairs
    expected=(q-1)*q**4+2*q**3+q*q-q
    expected_ranks={0:1,1:2*q**3-q-1,2:(q-1)*q**4+q*q-1,4:1}
    assert len(generators)==q**3,(q,'single',len(generators))
    assert len(pairs)==(q-1)*q**4+2*q**3-q,(q,'pairs',len(pairs))
    assert len(S)==expected,(q,'total',len(S),expected)
    by_rank=dict(Counter(rank(x,q) for x in S))
    assert by_rank==expected_ranks,(q,by_rank,expected_ranks)
    # Closure: all products of up to length three suffice and no new operators occur.
    assert all(comp(P,L,q) in S for P in pairs for L in generators)
    print(f'GF({q}): generators={len(generators)}, twofold={len(pairs)}, monoid={len(S)}, ranks={by_rank}; VERIFY_OK')

if __name__=='__main__':
    for q in (2,4):verify(q)
