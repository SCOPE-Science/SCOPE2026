#!/usr/bin/env python3
# Exact witness for the two-qubit random-unitary pair-product rank theorem.
P=1009
root=469
assert (root*root+1)%P==0
inv2=pow(2,P-2,P)
# Each entry represents 2 H_r. Tuples (a,b) denote a+b*i.
Hs=[
[[-4,(3,4),(-1,3),(-2,2)],[(3,-4),-2,(-3,-3),(0,-2)],[(-1,-3),(-3,3),-2,(2,1)],[(-2,-2),(0,2),(2,-1),-2]],
[[0,4,2,(-3,-2)],[4,2,(-2,-4),(0,-1)],[2,(-2,4),-2,-4],[(-3,2),(0,1),-4,0]],
[[0,(-2,-4),(-2,-3),4],[(-2,4),2,(1,3),(-2,3)],[(-2,3),(1,-3),0,(2,-2)],[4,(-2,-3),(2,2),0]],
[[-2,(2,4),(0,-1),(0,2)],[(2,-4),-4,-3,(-1,2)],[(0,1),-3,0,(-2,-1)],[(0,-2),(-1,-2),(-2,1),0]]
]
def cv(z):
    if isinstance(z,tuple): a,b=z
    else: a,b=z,0
    return ((a%P)+(b%P)*root)%P*inv2%P
def eye(n): return [[1 if i==j else 0 for j in range(n)] for i in range(n)]
def add(A,B): return [[(A[i][j]+B[i][j])%P for j in range(len(A[0]))] for i in range(len(A))]
def sub(A,B): return [[(A[i][j]-B[i][j])%P for j in range(len(A[0]))] for i in range(len(A))]
def sc(c,A): return [[c*x%P for x in row] for row in A]
def mm(A,B): return [[sum(A[i][k]*B[k][j] for k in range(len(B)))%P for j in range(len(B[0]))] for i in range(len(A))]
def inv(A):
    n=len(A); E=eye(n); M=[A[i][:]+E[i] for i in range(n)]; row=0
    for col in range(n):
        piv=next((r for r in range(row,n) if M[r][col]),None)
        if piv is None: raise AssertionError('singular denominator in Cayley witness')
        M[row],M[piv]=M[piv],M[row]
        q=pow(M[row][col],P-2,P); M[row]=[(q*x)%P for x in M[row]]
        for r in range(n):
            if r!=row and M[r][col]:
                q=M[r][col]; M[r]=[(M[r][c]-q*M[row][c])%P for c in range(2*n)]
        row+=1
    return [x[n:] for x in M]
def rank(rows):
    A=[r[:] for r in rows]; row=0
    if not A:return 0
    for col in range(len(A[0])):
        piv=next((r for r in range(row,len(A)) if A[r][col]),None)
        if piv is None: continue
        A[row],A[piv]=A[piv],A[row]
        q=pow(A[row][col],P-2,P); A[row]=[(q*x)%P for x in A[row]]
        for r in range(len(A)):
            if r!=row and A[r][col]:
                q=A[r][col]; A[r]=[(A[r][c]-q*A[row][c])%P for c in range(len(A[0]))]
        row+=1
        if row==len(A): break
    return row
def flat(A): return [x for row in A for x in row]
def kron(A,B):
    return [[A[i//len(B)][j//len(B[0])]*B[i%len(B)][j%len(B[0])]%P for j in range(len(A[0])*len(B[0]))] for i in range(len(A)*len(B))]
I4=eye(4); U=[I4]
for G in Hs:
    H=[[cv(z) for z in row] for row in G]
    U.append(mm(sub(I4,sc(root,H)),inv(add(I4,sc(root,H)))))
E=[]
for a in range(2):
    for b in range(2):
        X=[[0,0],[0,0]]; X[a][b]=1; E.append(X)
LA=[flat(kron(X,eye(2))) for X in E]
LB=[flat(kron(eye(2),X)) for X in E]
expected={2:(3,6,6),3:(7,10,10),4:(13,16,16),5:(16,16,16)}
rows_out=[]
for m in range(2,6):
    Ui=U[:m]; invs=[inv(X) for X in Ui]
    products=[flat(mm(invs[i],Ui[j])) for i in range(m) for j in range(m)]
    got=(rank(products),rank(products+LA),rank(products+LB))
    assert got==expected[m],(m,got,expected[m])
    rows_out.append((m,)+got)
print('VERIFY_OK')
print('prime =',P)
print('sqrt_minus_one =',root)
for row in rows_out: print('m=%d pair_rank=%d alice_sum_rank=%d bob_sum_rank=%d'%row)
