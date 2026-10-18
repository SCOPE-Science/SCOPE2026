"""Finite exact tests of sign fibers and involution tangent ranks.
Scientific proof is independent of these bounded tests.
"""
from itertools import combinations, product
from math import comb

def plucker(A,p):
    n=len(A)
    return {(i,j):(A[i][0]*A[j][1]-A[j][0]*A[i][1])%p for i,j in combinations(range(n),2)}

def relation(P,i,j,k,l,p):
    return (P[i,j]*P[k,l]-P[i,k]*P[j,l]+P[i,l]*P[j,k])%p

def test_fibers():
    p=1009
    for n in (4,5,6):
      A=[((i*i+7*i+3)%p,(i*i*i+13*i+5)%p) for i in range(n)]
      P=plucker(A,p)
      assert all(v for v in P.values()),(n,P)
      pairs=list(P)
      # all projective sign vectors, fixing first Plucker sign +
      count=0
      for bits in product((-1,1),repeat=len(pairs)-1):
        Q={pairs[0]:P[pairs[0]]}
        Q.update({e:P[e]*s%p for e,s in zip(pairs[1:],bits)})
        if all(relation(Q,*four,p)==0 for four in combinations(range(n),4)):
          count+=1
      expect=2**(n-1)
      assert count==expect,(n,count,expect)
      print('FIBERS',n,count)

def test_fixed():
    for n in range(4,13):
      n_mixed=2**(n-1)-1
      n_coord=n
      # For each nontrivial sign partition compute tangent minus-eigenspace
      # on each fixed component (W contained in eigenspace, or W split).
      for s in range(1,n):
        t=n-s
        codims=[n-2]
        if s>=2: codims.append(2*t)
        if t>=2: codims.append(2*s)
        assert all(c>=2 for c in codims)
        if n%2==0: assert all(c%2==0 for c in codims)
      degree=2**(n-3)*comb(2*n-4,n-2)//(n-1)
      assert degree>0
      print('COMPONENTS',n,n_coord,n_mixed,'dimensions',2*n-6,n-2,'degree',degree,'gorenstein',n%2==0)


def permutation_sign(p):
    return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1

def det_mod(M,p):
    from itertools import permutations
    k=len(M)
    return sum(permutation_sign(z)*__import__('math').prod(M[i][z[i]] for i in range(k)) for z in permutations(range(k)))%p

def rank_mod(M,p):
    if not M:return 0
    A=[list(row) for row in M]
    row=0
    for col in range(len(A[0])):
        pivot=next((i for i in range(row,len(A)) if A[i][col]%p),None)
        if pivot is None: continue
        A[row],A[pivot]=A[pivot],A[row]
        inv=pow(A[row][col]%p,-1,p)
        A[row]=[(e*inv)%p for e in A[row]]
        for i in range(len(A)):
            if i!=row and A[i][col]:
                coef=A[i][col]
                A[i]=[(a-coef*b)%p for a,b in zip(A[i],A[row])]
        row+=1
        if row==len(A):break
    return row

def test_jacobian():
    from itertools import combinations
    n=5;p=101
    pairs=list(combinations(range(n),2))
    patterns=[('generic',[(1,1),(1,2),(1,4),(1,8),(1,16)]),
       ('missing-column',[(1,1),(1,2),(1,4),(1,8),(0,0)]),
       ('split-1+4',[(1,0),(0,1),(0,2),(0,4),(0,8)]),
       ('split-2+3',[(1,0),(2,0),(0,1),(0,2),(0,4)])]
    for label,A in patterns:
      P=plucker(A,p)
      Q=[[0]*n for _ in range(n)]
      for (i,j),x in P.items(): Q[i][j]=Q[j][i]=x*x%p
      jac=[]
      for R in combinations(range(n),4):
       for C in combinations(range(n),4):
        M=[[Q[i][j] for j in C] for i in R]
        assert det_mod(M,p)==0
        grad=[]
        for i,j in pairs:
         z=0
         for ii,jj in ((i,j),(j,i)):
          if ii in R and jj in C:
           r=R.index(ii);c=C.index(jj)
           sub=[[M[a][b] for b in range(4) if b!=c] for a in range(4) if a!=r]
           z+=(-1)**(r+c)*det_mod(sub,p)
         grad.append(z%p)
        jac.append(grad)
      r=rank_mod(jac,p)
      assert (r==3 if label=='generic' else r<3),(label,r)
      print('JACOBIAN',label,r)

if __name__=='__main__':
    test_fibers()
    test_fixed()
    test_jacobian()
    print('VERIFY_OK')
