from fractions import Fraction as F

def add(a,b): return (a[0]+b[0], a[1]+b[1])
def sub(a,b): return (a[0]-b[0], a[1]-b[1])
def mul(s,a): return (s*a[0], s*a[1])
def det(a,b): return a[0]*b[1]-a[1]*b[0]

def coeff(dm, du):
    if du[0] != 0:
        q = dm[0] / du[0]
    else:
        q = dm[1] / du[1]
    assert dm == mul(q,du)
    return q

def involute(M,U,n):
    alpha=[]
    V=[]
    for i in range(2*n):
        du=sub(U[(i+1)%(2*n)],U[i])
        dm=sub(M[(i+1)%(2*n)],M[i])
        alpha.append(coeff(dm,du))
        a=det(U[i],U[(i+1)%(2*n)])
        V.append(mul(F(1,a),du))
    beta=[]
    for i in range(2*n):
        s=F(0)
        for k in range(n):
            j=(i+k)%(2*n)
            s += alpha[j]*det(U[j],U[(j+1)%(2*n)])
        beta.append(s/2)
    N=[add(M[i],mul(beta[i],V[i])) for i in range(2*n)]
    return N,V

def double_involute(M,U,n):
    N,V=involute(M,U,n)
    S,W=involute(N,V,n)
    # W_i = -U_{i+1}; relabel back to U-indexing.
    for i in range(2*n):
        assert W[i] == mul(F(-1),U[(i+1)%(2*n)])
    return [S[(j-1)%(2*n)] for j in range(2*n)]

def build_from_alpha(U,n,alpha,anchor=(F(0),F(0))):
    M=[None]*(2*n)
    M[0]=anchor
    for i in range(n-1):
        M[i+1]=add(M[i],mul(alpha[i],sub(U[i+1],U[i])))
    closure=add(M[n-1],mul(alpha[n-1],sub(U[n],U[n-1])))
    assert closure == anchor
    for i in range(n,2*n):
        M[i]=M[i-n]
    return M

def edge_alpha(M,U,n):
    return [coeff(sub(M[(i+1)%n],M[i]),sub(U[i+1],U[i])) for i in range(n)]

# A rational centrally symmetric octagon.
n=4
U=[(F(3),F(0)),(F(2),F(2)),(F(0),F(3)),(F(-2),F(2))]
U += [mul(F(-1),u) for u in U]

# A basis of E_U found from the two closure equations.
e1=[F(4,3),F(-5,3),F(1),F(0)]
e2=[F(5,3),F(-4,3),F(0),F(1)]

def apply_shape(alpha):
    M=build_from_alpha(U,n,alpha)
    Mp=double_involute(M,U,n)
    return edge_alpha(Mp,U,n), Mp[0]

# Determine A and B on the chosen basis.
ae1,b1=apply_shape(e1)
ae2,b2=apply_shape(e2)
assert ae1 == [x/F(6) for x in e1]
assert ae2 == [x/F(6) for x in e2]
# Thus A=(1/6)I in this example. B columns are b1,b2.
A=F(1,6)

# Nontrivial shape r=2 e1+3 e2, with translated anchor.
r=[2*e1[i]+3*e2[i] for i in range(n)]
anchor=(F(1),F(2))
M=build_from_alpha(U,n,r,anchor)
Mp=double_involute(M,U,n)
rp=edge_alpha(Mp,U,n)

# Coordinates of r in the selected basis are q=(2,3).
q1,q2=F(2),F(3)
# Solve (I-A)y=q exactly.
y1=q1/(1-A); y2=q2/(1-A)
shift=add(mul(y1,b1),mul(y2,b2))
O=add(anchor,shift)

# After one step, coordinates are A*q and anchor is Mp[0].
yp1=(A*q1)/(1-A); yp2=(A*q2)/(1-A)
Op=add(Mp[0],add(mul(yp1,b1),mul(yp2,b2)))
assert O == Op
assert rp == [A*x for x in r]

print("VERIFY_OK")
print("A_scalar =", A)
print("B_e1 =", b1)
print("B_e2 =", b2)
print("central_point =", O)
