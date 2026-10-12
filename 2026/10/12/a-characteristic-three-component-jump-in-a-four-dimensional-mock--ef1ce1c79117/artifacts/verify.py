"""Reconstruction of skew mock-Lie YBE for a four-dimensional 2-step algebra.

Requires SymPy; finite enumeration is a check, not the arbitrary-field proof.
"""
import itertools
import sympy as sp

n=4
a,b,c,d,e,f=sp.symbols('a b c d e f')
vars_=(a,b,c,d,e,f)
R=sp.Matrix([[0,a,b,c],[-a,0,d,e],[-b,-d,0,f],[-c,-e,-f,0]])
unit=sp.eye(n)

def mul(x,y):
    return sp.Matrix([0,x[0]*y[0],0,x[0]*y[2]+x[2]*y[0]])

def left(x):
    return sp.Matrix.hstack(*(mul(x,unit[:,j]) for j in range(n)))

# Reconstruct the original commutative Jacobi algebra, in every characteristic.
for i,j,k in itertools.product(range(n),repeat=3):
    x,y,z=unit[:,i],unit[:,j],unit[:,k]
    assert mul(x,y)==mul(y,x)
    assert mul(mul(x,y),z)==sp.zeros(4,1)
    assert mul(x,mul(y,z))+mul(y,mul(z,x))+mul(z,mul(x,y))==sp.zeros(4,1)

# Definition (4.9): [r,r]=r12*r13 + r13*r23 - r12*r23.
T={}
for i,j,k in itertools.product(range(n),repeat=3):
    value=sp.Integer(0)
    for u,v in itertools.product(range(n),repeat=2):
        base=mul(unit[:,u],unit[:,v])
        value+=base[i]*R[u,j]*R[v,k]
        value+=R[i,u]*R[j,v]*base[k]
        value-=R[i,u]*base[j]*R[v,k]
    T[i,j,k]=sp.expand(value)

# Independent reconstruction via Proposition 5.1, the coadjoint O-operator identity.
for j,k in itertools.product(range(n),repeat=2):
    rj,rk=R[:,j],R[:,k]
    defect=sp.expand(mul(rj,rk)-R*(left(rj).T*unit[:,k]+left(rk).T*unit[:,j]))
    for i in range(n):
        assert sp.expand(defect[i]-T[i,j,k])==0

# Exact field-point equations in any characteristic unequal to two.
# By b^2=0, b=0 at every field-valued solution.
# Remaining equations: 3a^2=0, a(c-d)=0,
# 2af+c^2-2cd=0, and 3cf=0.
short=[b,3*a*a,a*(c-d),2*a*f+c*c-2*c*d,3*c*f]
full=[value for value in T.values()]

# A direct symbolic check of both parameterized branches for char != 2,3.
for subs in ({a:0,b:0,c:0},{a:0,b:0,c:2*d,f:0}):
    assert all(sp.expand(p.subs(subs,simultaneous=True))==0 for p in full)

# Characteristic-three polynomial consequences checked coefficientwise.
for p in full:
    # Replace b=0 and reduce coefficients modulo 3. The surviving polynomial
    # vanishes whenever a(c-d)=0 and af=c(c+d).
    t=sp.Poly(sp.expand(p.subs({b:0})),a,c,d,e,f,modulus=3)
    g=sp.groebner([a*(c-d),a*f-c*(c+d)],a,c,d,e,f,modulus=3)
    assert g.reduce(t.as_expr())[1]==0

# Also prove all the displayed equations occur in the full tensor ideal.
Gfull=sp.groebner(full,vars_)
for x in (b*b,3*a*a,2*a*(c-d),2*a*f+c*c-2*c*d,6*c*f):
    assert sp.expand(Gfull.reduce(x)[1])==0

# Formula for the source coboundary: Delta(x)=(L_x x id-id x L_x)r.
delta=[]
for k in range(n):
    M=sp.zeros(n,n)
    for i,j in itertools.product(range(n),repeat=2):
        M+=R[i,j]*(mul(unit[:,k],unit[:,i])*unit[:,j].T-unit[:,i]*mul(unit[:,k],unit[:,j]).T)
    delta.append(sp.expand(M))
assert delta[1]==sp.zeros(n,n) and delta[3]==sp.zeros(n,n)
S24=unit[:,1]*unit[:,3].T+unit[:,3]*unit[:,1].T
assert sp.expand((delta[0]-(2*a*unit[:,1]*unit[:,1].T-b*(unit[:,0]*unit[:,3].T+unit[:,3]*unit[:,0].T)+b*(unit[:,1]*unit[:,2].T+unit[:,2]*unit[:,1].T)+(c-d)*S24+2*f*unit[:,3]*unit[:,3].T)))==sp.zeros(n,n)
assert sp.expand(delta[2]-(a*S24+b*(unit[:,2]*unit[:,3].T+unit[:,3]*unit[:,2].T)+2*c*unit[:,3]*unit[:,3].T))==sp.zeros(n,n)

# Exact Pfaffian, determining ranks 0, 2 and 4 over odd fields.
pf=sp.expand(R.det()-(a*f-b*e+c*d)**2)
assert pf==0

# Exhaustively compare the defining 64 tensor coordinates against the closed
# field-specific equations for all six skew coefficients over F3,F5,F7.
def tensor_zero_mod_prime(u,q):
    A,B,C,D,E,F=u
    rr=((0,A,B,C),(-A,0,D,E),(-B,-D,0,F),(-C,-E,-F,0))
    for i,j,k in itertools.product(range(4),repeat=3):
        t=0
        if i==1:t+=rr[0][j]*rr[0][k]
        if i==3:t+=rr[0][j]*rr[2][k]+rr[2][j]*rr[0][k]
        if k==1:t+=rr[i][0]*rr[j][0]
        if k==3:t+=rr[i][0]*rr[j][2]+rr[i][2]*rr[j][0]
        if j==1:t-=rr[i][0]*rr[0][k]
        if j==3:t-=rr[i][0]*rr[2][k]+rr[i][2]*rr[0][k]
        if t%q:return False
    return True

def closed_zero(u,q):
    A,B,C,D,E,F=u
    return (B==0 and (3*A*A)%q==0 and A*(C-D)%q==0
            and (2*A*F+C*C-2*C*D)%q==0 and (3*C*F)%q==0)

for q in (3,5,7):
    N=0
    rank4=0
    deltas=set()
    for u in itertools.product(range(q),repeat=6):
        direct=tensor_zero_mod_prime(u,q)
        closed=closed_zero(u,q)
        assert direct==closed,(q,u)
        if not direct:continue
        N+=1
        A,B,C,D,E,F=u
        if (A*F-B*E+C*D)%q:rank4+=1
        deltas.add((A%q,C%q,D%q,F%q))
    if q==3:
        expected=3*q**3-2*q**2
        expected_full=q*q*(q-1)
        expected_delta=3*q*q-2*q
    else:
        expected=q**3+q*q-q
        expected_full=q*(q-1)
        expected_delta=q*q+q-1
    assert (N,rank4,len(deltas))==(expected,expected_full,expected_delta)
    print(f'F_{q}: r={N} rank4={rank4} distinct_coboundaries={len(deltas)}')

# A separate prime-power check on F9, represented as F3[t]/(t^2+1).
# A field element A+Bt is encoded by A+3B.
add=[[((x%3+y%3)%3+3*((x//3+y//3)%3)) for y in range(9)] for x in range(9)]
neg=[(((-x)%3)+3*((-(x//3))%3)) for x in range(9)]
mul9=[[((x%3*y%3+2*(x//3)*(y//3))%3+3*((x%3*(y//3)+(x//3)*(y%3))%3)) for y in range(9)] for x in range(9)]
assert all(mul9[x][y]==mul9[y][x] for x in range(9) for y in range(9))
assert all(mul9[x][y]!=0 for x in range(1,9) for y in range(1,9))
solutions9=0
fullrank9=0
for A,C,D,F,E in itertools.product(range(9),repeat=5):
    # b=0 is necessary over any field; e is genuinely a free gauge parameter.
    acd=add[C][neg[D]]
    fterm=add[mul9[2][mul9[A][F]]][add[mul9[C][C]][neg[mul9[2][mul9[C][D]]]]]
    if mul9[A][acd] or fterm:continue
    solutions9+=1
    pf9=add[mul9[A][F]][mul9[C][D]]
    if pf9:fullrank9+=1
assert solutions9==3*9**3-2*9**2
assert fullrank9==9**2*(9-1)
print(f'F_9: r={solutions9} rank4={fullrank9} (GF9 arithmetic)')
print('VERIFY_OK')
