import math
def dbin(p,q):
    if p == 1.0:
        return -math.log(q)
    return p*math.log(p/q)+(1-p)*math.log((1-p)/(1-q))
for m in range(2,20):
    s=math.sqrt(m); q0=(1+1/s)/2
    for k in range(1,1000):
        b=1+(s-1)*k/1000
        p=(1+b/s)/2
        assert dbin(p,q0) > (b-1)**2/(2*m)-1e-14
s=math.sqrt(3); q0=(1+1/s)/2
assert abs(-math.log(q0)-0.23740078615161916)<1e-15
assert abs((s-1)**2/6-0.08931639747704088)<1e-15
# Direct three-qubit Pauli multiplication without external packages.
I=((1,0),(0,1)); X=((0,1),(1,0)); Y=((0,-1j),(1j,0)); Z=((1,0),(0,-1))
def kron(A,B):
    return tuple(tuple(a*b for a in rowA for b in rowB) for rowA in A for rowB in B)
def add(A,B):
    return tuple(tuple(A[i][j]+B[i][j] for j in range(len(A[0]))) for i in range(len(A)))
def mm(A,B):
    n=len(A); m=len(B[0]); k=len(B)
    return tuple(tuple(sum(A[i][t]*B[t][j] for t in range(k)) for j in range(m)) for i in range(n))
def scale(c,A):
    return tuple(tuple(c*x for x in row) for row in A)
def eye(n):
    return tuple(tuple(1 if i==j else 0 for j in range(n)) for i in range(n))
def k3(A): return kron(kron(A,A),A)
B=add(add(k3(X),k3(Y)),k3(Z))
D=add(mm(B,B),scale(-3,eye(8)))
assert max(abs(z) for row in D for z in row)<1e-12
print("VERIFY_OK")
