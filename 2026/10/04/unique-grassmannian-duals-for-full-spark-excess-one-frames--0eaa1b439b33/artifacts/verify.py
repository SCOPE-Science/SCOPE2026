from fractions import Fraction as Q

def mm(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

def tr(A):
    return [list(x) for x in zip(*A)]

def eye(n):
    return [[Q(int(i==j)) for j in range(n)] for i in range(n)]

F=[[Q(3),Q(0),Q(-1)],[Q(0),Q(3),Q(-2)]]
H=[[Q(13,45),Q(-4,45),Q(-2,15)],[Q(-2,45),Q(11,45),Q(-2,15)]]
Hc=[[Q(13,42),Q(-1,21),Q(-1,14)],[Q(-1,21),Q(5,21),Q(-1,7)]]
G=mm(tr(F),H)
Gc=mm(tr(F),Hc)
assert mm(F,tr(H))==eye(2)
assert mm(F,tr(Hc))==eye(2)
assert mm(G,G)==G
assert mm(Gc,Gc)==Gc
mu=max(abs(G[i][j]) for i in range(3) for j in range(3) if i!=j)
muc=max(abs(Gc[i][j]) for i in range(3) for j in range(3) if i!=j)
assert mu==Q(2,5)
assert muc==Q(3,7)
assert mu<muc
expected=[[Q(13,15),Q(-4,15),Q(-2,5)],[Q(-2,15),Q(11,15),Q(-2,5)],[Q(-1,5),Q(-2,5),Q(2,5)]]
assert G==expected
print('VERIFY_OK mu_star=2/5 mu_canonical=3/7 dual_identity=True')
