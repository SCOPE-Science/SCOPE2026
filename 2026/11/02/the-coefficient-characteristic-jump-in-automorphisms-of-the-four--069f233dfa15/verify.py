"""Finite-field brute-force check of the R4 quandle-algebra automorphism classification.

Usage: python verify.py. Exhaustive for F2 and F3 in the block form forced
by the intrinsic right annihilator; independently tests all 16 basis products.
"""
from itertools import product

def matmul(X,Y,p):
    return [[sum(X[i][k]*Y[k][j] for k in range(len(Y)))%p for j in range(len(Y[0]))] for i in range(len(X))]

def matvec(X,u,p):return [sum(X[i][j]*u[j] for j in range(len(u)))%p for i in range(len(X))]

def invertible2(A,p):return (A[0][0]*A[1][1]-A[0][1]*A[1][0])%p!=0

def cols(M):return list(map(list,zip(*M)))

def product_original(u,v,p):
    # Basis e0,e1,e2,e3; e_i * e_j = e_(2j-i mod 4).
    w=[0]*4
    for i in range(4):
        for j in range(4):w[(2*j-i)%4]=(w[(2*j-i)%4]+u[i]*v[j])%p
    return w

def count(p):
    if p==2:
        basis=[[1,0,0,0],[0,1,0,0],[1,0,1,0],[0,1,0,1]]
    else:
        basis=[[1,0,1,0],[0,1,0,1],[1,0,-1,0],[0,1,0,-1]]
    B=cols(basis)
    # Independently calculate product table in original basis, convert via
    # B inverse by searching representation (small q). Avoid symbolic formulas.
    lookup={tuple(matvec(B,list(v),p)):tuple(v) for v in product(range(p), repeat=4)}
    mul=lambda a,b: lookup[tuple(product_original(matvec(B,a,p),matvec(B,b,p),p))]
    basis4=[tuple(int(i==k) for i in range(4)) for k in range(4)]
    table=[[mul(x,y) for y in basis4] for x in basis4]
    GL=[]
    for t in product(range(p),repeat=4):
        A=((t[0],t[1]),(t[2],t[3]))
        if invertible2(A,p):GL.append(A)
    accepted=[]
    total=0
    for A in GL:
      for D in GL:
        for entries in product(range(p),repeat=4):
          C=((entries[0],entries[1]),(entries[2],entries[3]))
          # Matrix block [A 0; C D], basis 0,1 quotient and 2,3 right annihilator
          F=[list(A[0])+[0,0],list(A[1])+[0,0],list(C[0])+list(D[0]),list(C[1])+list(D[1])]
          ft=[tuple(row) for row in cols(F)]
          def multiply_coordinates(x,y):
            return tuple(sum(x[i]*y[j]*table[i][j][k] for i in range(4) for j in range(4))%p for k in range(4))
          good=True
          for i in range(4):
            for j in range(4):
              if tuple(matvec(F,table[i][j],p))!=multiply_coordinates(ft[i],ft[j]):
                good=False;break
            if not good:break
          total+=1
          if good:accepted.append((A,C,D))
    expected=(2*(p-1)**2 if p%2 else 2*p**4)
    assert len(accepted)==expected,(p,len(accepted),expected)
    if p%2:
       for A,C,D in accepted:
          assert C==((0,0),(0,0))
          assert (A==((1,0),(0,1)) and D[0][1]==D[1][0]==0) or (A==((0,1),(1,0)) and D[0][0]==D[1][1]==0)
    else:
       for A,C,D in accepted:
          assert A==D and A in [((1,0),(0,1)),((0,1),(1,0))]
    print(f'F_{p}: {total} annihilator-preserving invertible matrices checked, {len(accepted)} automorphisms; expected {expected}: PASS')

if __name__=='__main__':
  count(2);count(3);print('VERIFY_OK')
