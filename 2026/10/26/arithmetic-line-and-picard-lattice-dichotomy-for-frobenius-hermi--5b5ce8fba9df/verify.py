#!/usr/bin/env python3
"""Exact verification of arithmetic line and Picard lattices for two ternary diagonal quartics.

Requires Python 3.10+ and SymPy. All finite-field, intersection,
Frobenius, lattice, and integer-kernel computations are recreated here.
"""
from itertools import combinations, product
from math import gcd
from sympy import Matrix, eye, zeros, ZZ
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form

# Encode F_9 = F_3[i], i^2=-1, by a+3*b (a,b in {0,1,2}).
def plus(x, y):
    return ((x % 3 + y % 3) % 3) + 3*((x//3 + y//3) % 3)
def times(x, y):
    a,b=x%3,x//3
    c,d=y%3,y//3
    return (a*c-b*d)%3 + 3*((a*d+b*c)%3)

def power(x, n):
    z=1
    for _ in range(n):
        z=times(z,x)
    return z

def conjugate(x):
    return power(x,3)

def minus(x,y):
    return plus(x, ((-y%3) + 3*((-(y//3))%3)))

def hermitian(u,v):
    val=0
    for a,b in zip(u,v):
        val=plus(val,times(conjugate(a),b))
    return val

def rref(rows):
    rows=[list(row) for row in rows]
    i=0
    pivot=[]
    for j in range(4):
        k=next((k for k in range(i,len(rows)) if rows[k][j]!=0),None)
        if k is None:continue
        rows[i],rows[k]=rows[k],rows[i]
        inv=power(rows[i][j],7)  # Multiplicative group order 8.
        rows[i]=[times(z,inv) for z in rows[i]]
        for k in range(len(rows)):
            if k==i:continue
            factor=rows[k][j]
            if factor:
                rows[k]=[minus(a,times(factor,b)) for a,b in zip(rows[k],rows[i])]
        pivot.append(j)
        i+=1
        if i==len(rows):break
    return tuple(tuple(row) for row in rows),tuple(pivot)

def all_rref_planes():
    for a,b in combinations(range(4),2):
        u=[0]*4;v=[0]*4
        u[a]=1;v[b]=1
        free=[(0,j) for j in range(a+1,4) if j!=b]
        free +=[(1,j) for j in range(b+1,4)]
        for values in product(range(9),repeat=len(free)):
            uu=u[:];vv=v[:]
            for (which,j),z in zip(free,values):
                (uu if which==0 else vv)[j]=z
            yield (tuple(uu),tuple(vv))

def primitive_kernel(A):
    """Find an integral basis of ker(A) via unimodular row operations on A.T."""
    B=A.T.copy()
    m,n=B.shape
    U=eye(m)
    r=0
    for j in range(n):
        k=next((i for i in range(r,m) if B[i,j]),None)
        if k is None:continue
        if k!=r:
            B.row_swap(k,r);U.row_swap(k,r)
        for i in range(r+1,m):
            if not B[i,j]:continue
            a,b=int(B[r,j]),int(B[i,j])
            g=gcd(a,b)
            alpha,beta,d=ZZ.gcdex(ZZ(a),ZZ(b))
            assert d==g
            br,bi=list(B.row(r)),list(B.row(i))
            ur,ui=list(U.row(r)),list(U.row(i))
            B[r,:]=Matrix(1,n,[alpha*x+beta*y for x,y in zip(br,bi)])
            B[i,:]=Matrix(1,n,[(-b//g)*x+(a//g)*y for x,y in zip(br,bi)])
            U[r,:]=Matrix(1,m,[alpha*x+beta*y for x,y in zip(ur,ui)])
            U[i,:]=Matrix(1,m,[(-b//g)*x+(a//g)*y for x,y in zip(ur,ui)])
        r+=1
    assert B[r:,:]==zeros(m-r,n)
    assert U.det() in (-1,1)
    N=U[r:,:].T
    assert A*N==zeros(A.rows,N.cols)
    return N

def rational_points(signs):
    ans=0
    for p in product(range(3),repeat=4):
        if all(a==0 for a in p):continue
        if next(a for a in p if a)!=1:continue
        if sum(s*(a**4) for s,a in zip(signs,p))%3==0:ans+=1
    return ans

def main():
    planes=list(all_rref_planes())
    assert len(planes)==7462 and len(set(planes))==7462
    lines=sorted(p for p in planes
                 if hermitian(p[0],p[0])==hermitian(p[1],p[1])==hermitian(p[0],p[1])==0)
    assert len(lines)==112
    index={p:j for j,p in enumerate(lines)}
    G=zeros(112)
    for i in range(112):
        G[i,i]=-2
        for j in range(i):
            meeting=(len(rref([*lines[i],*lines[j]])[1])<4)
            G[i,j]=G[j,i]=int(meeting)
    basis=list(G.rref()[1]);assert len(basis)==22
    gram=G.extract(basis,basis)
    assert gram.det()==-9
    # Classes of other 90 lines in the 22-line NS basis.
    coords=gram.inv()*G.extract(basis,list(range(112)))
    assert all(x.q==1 for x in coords)
    # First, repeat the two distinct square-class cases, then the second split sign vector.
    expected={0:(8,52,16,16,12,-3072,[1,1]+[2]*9+[6]),
              1:(0,56,10,20,11,6144,[2]*10+[6]),
              2:(8,52,16,16,12,-3072,[1,1]+[2]*9+[6])}
    for m in range(3):
        signs=[-1]*m+[1]*(4-m)
        alpha=[3]*m+[1]*(4-m)  # The quadratic scaling (1+i) has (1+i)^(-2)=i.
        F=[]
        for p in lines:
            p2=rref([[times(conjugate(x),alpha[j]) for j,x in enumerate(row)] for row in p])[0]
            F.append(index[p2])
        assert all(F[F[i]]==i for i in range(112))
        fixed=[i for i,j in enumerate(F) if i==j]
        pairs=[(i,j) for i,j in enumerate(F) if i<j]
        touching=sum(int(G[i,j]) for i,j in pairs)
        point_count=rational_points(signs)
        Fmat=coords.extract(list(range(22)),[F[i] for i in basis])
        assert Fmat*Fmat==eye(22)
        assert Fmat.T*gram*Fmat==gram
        invariant=primitive_kernel(Fmat-eye(22))
        # Every integral invariant class is generated by Galois orbit sums of lines.
        orbit_vectors=[coords[:,i] for i in fixed]
        orbit_vectors += [coords[:,i]+coords[:,j] for i,j in pairs]
        orbit_matrix=Matrix.hstack(*orbit_vectors)
        # Express all orbit sums in a primitive fixed-lattice basis.
        orbit_coords=(invariant.T*invariant).inv()*invariant.T*orbit_matrix
        assert invariant*orbit_coords==orbit_matrix
        assert all(x.q==1 for x in orbit_coords)
        orbit_hnf=hermite_normal_form(orbit_coords.applyfunc(int))
        assert abs(int(orbit_hnf.det()))==1
        fixed_gram=invariant.T*gram*invariant
        normal=smith_normal_form(fixed_gram,domain=ZZ)
        elementary=sorted(abs(int(normal[i,i])) for i in range(normal.rows))
        result=(len(fixed),len(pairs),point_count,touching,invariant.cols,int(fixed_gram.det()),elementary)
        assert result==expected[m],(m,result,expected[m])
        # For all cases the invariant sublattice contains the hyperplane class.
        assert (Fmat-eye(22)).rank()==22-invariant.cols
        print('SIGN_MINUS',m,'FIXED_LINES',len(fixed),'DEGREE2_LINE_PAIRS',len(pairs),
              'F3_POINTS',point_count,'TOUCHING_PAIRS',touching,'PICARD_RANK',invariant.cols,
              'PICARD_DISCRIMINANT',fixed_gram.det(),'DISCR_GROUP_SNF',elementary,'ORBIT_TRACE_INDEX',abs(int(orbit_hnf.det())))
    print('VERIFY_OK: 7462 F9 planes, 112 Hermitian lines, NS discriminant -9, two diagonal twist lattice types')

if __name__=='__main__':
    main()
