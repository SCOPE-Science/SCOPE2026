"""Exact rational verification of affine least-squares kernels on metric stars."""
from fractions import Fraction as Q
from itertools import product


def inverse_rational(A):
    n=len(A)
    U=[list(row)+[Q(int(i==j)) for j in range(n)] for i,row in enumerate(A)]
    for k in range(n):
        p=next(i for i in range(k,n) if U[i][k])
        U[k],U[p]=U[p],U[k]
        h=U[k][k]
        U[k]=[z/h for z in U[k]]
        for i in range(n):
            if i!=k:
                h=U[i][k]
                U[i]=[a-h*b for a,b in zip(U[i],U[k])]
    return [row[n:] for row in U]


def abs_affine_integral(a,b):
    if a*b>=0:
        return (abs(a)+abs(b))/2
    return (a*a+b*b)/(2*(abs(a)+abs(b)))


def gram(m):
    W=sum(m)
    n=len(m)
    A=[[Q(0) for _ in range(n+1)] for _ in range(n+1)]
    A[0][0]=W/3
    for i,x in enumerate(m,1):
        A[0][i]=A[i][0]=x/6
        A[i][i]=x/3
    return A


def kernel_from_inverse(m, i, t, j, s, inv=None):
    inv=inverse_rational(gram(m)) if inv is None else inv
    n=len(m)
    row=[Q(1)-t]+[t if k==i else Q(0) for k in range(n)]
    col=[Q(1)-s]+[s if k==j else Q(0) for k in range(n)]
    return sum(row[a]*inv[a][b]*col[b] for a in range(n+1) for b in range(n+1))


def row_norm(m,i,t,inv):
    return sum(m[j]*abs_affine_integral(kernel_from_inverse(m,i,t,j,Q(0),inv),
                                          kernel_from_inverse(m,i,t,j,Q(1),inv))
               for j in range(len(m)))


def predicted_leaf(m,i):
    q=m[i]/sum(m)
    return (7+3*q)/(3*(1+q))


checks=0
sequences=[]
for n in range(1,8):
    sequences += [tuple(Q(a) for a in arr) for arr in product(range(1,5),repeat=n) if n<=4]
for n in range(5,12):
    sequences.extend([tuple(Q(((j*17+i*29)%13)+1,((i*j+3)%5)+1) for i in range(n)) for j in range(6)])
sequences = sequences[:2500]
for masses in sequences:
    n=len(masses); W=sum(masses)
    inv=inverse_rational(gram(masses))
    # Exact independently inverted Gram matrix.
    G=gram(masses)
    for a in range(n+1):
        for b in range(n+1):
            assert sum(G[a][k]*inv[k][b] for k in range(n+1))==Q(int(a==b))
            checks+=1
    observed=[]
    for i in range(n):
        center=row_norm(masses,i,Q(0),inv)
        leaf=row_norm(masses,i,Q(1),inv)
        assert center==Q(5,3)
        assert leaf==predicted_leaf(masses,i)
        checks+=2
        observed.append(leaf)
        for t in (Q(1,11),Q(1,3),Q(2,3),Q(10,11)):
            rr=row_norm(masses,i,t,inv)
            assert rr<(Q(1)-t)*center+t*leaf or rr==(Q(1)-t)*center+t*leaf
            assert rr<max(Q(5,3),leaf)
            checks+=2
    sharp=(7+3*min(masses)/W)/(3*(1+min(masses)/W))
    assert max([Q(5,3)]+observed)==sharp
    checks+=1
print(f'PASS: {checks} exact-rational assertions over {len(sequences)} weighted metric stars')
print('equilateral d=1..7:',[str((7*Q(d)+3)/(3*(Q(d)+1))) for d in range(1,8)])
