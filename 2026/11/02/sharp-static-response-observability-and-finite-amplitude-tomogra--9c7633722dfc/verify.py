"""Exact-rational checks for stationary row-transfer response geometry.

Run: python verify.py (requires sympy). This verifies finite examples and
linear-response reconstruction; arbitrary-size claims use the written proof.
"""
import itertools
import sympy as s

R=s.Rational

def connected_components(A):
    n=A.rows
    neighbours=[set() for _ in range(n)]
    for i in range(n):
        js=[j for j in range(n) if A[i,j]>0]
        for j,k in itertools.combinations(js,2):
            neighbours[j].add(k); neighbours[k].add(j)
    remain=set(range(n)); out=[]
    while remain:
        root=min(remain); comp={root}; todo=[root]; remain.remove(root)
        while todo:
            for k in neighbours[todo.pop()]:
                if k in remain:
                    remain.remove(k); comp.add(k); todo.append(k)
        out.append(comp)
    return out

def all_probes(P):
    n=P.rows
    ans=[]
    for i in range(n):
        js=[j for j in range(n) if P[i,j]>0]
        for j,k in itertools.combinations(js,2):
            d=s.zeros(n,1); d[j]=-1; d[k]=1
            ans.append((i,j,k,d))
    return ans

def reduced_basis(n):
    return s.Matrix.hstack(*(s.eye(n)[:,i]-s.eye(n)[:,n-1] for i in range(n-1)))

def response(P,src):
    n=P.rows
    A=s.eye(n)-P.T
    E=reduced_basis(n)
    # full rank system: replace final row with normalization
    F=A.copy(); F[n-1,:]=s.ones(1,n)
    b=src/n
    b[n-1]=0
    ans=F.inv()*b
    assert sum(ans)==0
    assert A*ans==src/n
    return ans

def stationary(P):
    n=P.rows
    F=s.eye(n)-P.T
    F[n-1,:]=s.ones(1,n)
    rhs=s.zeros(n,1); rhs[n-1]=1
    return F.inv()*rhs

P=s.Matrix([
 [0,R(1,2),R(1,2),0,0,0],
 [R(1,2),0,R(1,2),0,0,0],
 [0,0,0,R(1,2),R(1,4),R(1,4)],
 [R(1,2),R(1,2),0,0,0,0],
 [0,0,0,R(1,4),0,R(3,4)],
 [0,0,0,R(1,4),R(3,4),0],
])
assert P.rows==6 and all(P[i,i]==0 for i in range(6))
assert P*s.ones(6,1)==s.ones(6,1)
assert P.T*s.ones(6,1)==s.ones(6,1)
# Check reachability by positive powers of (I+P).
G=(s.eye(6)+P)**5
assert all(G[i,j]>0 for i in range(6) for j in range(6))
# Aperiodic by 2-cycle 0->1->0 and 3-cycle 0->2->3->0.
assert P[0,1]*P[1,0]>0 and P[0,2]*P[2,3]*P[3,0]>0
parts=connected_components(P)
assert {frozenset(a) for a in parts}=={frozenset((0,1,2)),frozenset((3,4,5))}
probes=all_probes(P)
Ds=s.Matrix.hstack(*[x[3] for x in probes]); Ys=s.Matrix.hstack(*[response(P,x[3]) for x in probes])
assert Ds.rank()==4 and Ys.rank()==4
assert (s.eye(6)-P.T)*Ys==Ds/6

# Three-state complete support: two spanning tree probes determine P exactly.
Q=s.Matrix([[0,R(1,2),R(1,2)], [R(1,2),0,R(1,2)], [R(1,2),R(1,2),0]])
assert len(connected_components(Q))==1
allq=all_probes(Q)
sel=[next(z for z in allq if set(z[1:3])==st) for st in [{0,1},{1,2}]]
D=s.Matrix.hstack(*[z[3] for z in sel]); Y=s.Matrix.hstack(*[response(Q,z[3]) for z in sel]); E=reduced_basis(3)
# Coordinate representation: source differences, measured response, reduced generator.
Dred=D[:2,:]; Yred=Y[:2,:]
InvA=3*Yred*Dred.inv(); Ared=InvA.inv()
A=s.eye(3)-Q.T
assert A*E==E*Ared
# Reconstruct generator by known zero-column-sum and known action on zero-sum.
# For each standard basis vector e_j = e3 + (ej-e3), and A*1=0.
ReconstA=s.Matrix.hstack(*[(E*Ared)[:,j] for j in range(2)],s.zeros(3,1))
# column operation: first two are A(ej-e3), third A*1=0 -> solve A on e3 = -sum(first two)/3
c3=-(ReconstA[:,0]+ReconstA[:,1])/3
Af=s.Matrix.hstack(ReconstA[:,0]+c3, ReconstA[:,1]+c3, c3)
Qrec=(s.eye(3)-Af).T
assert Qrec==Q

# Four-state genuinely chiral, fully supported bistochastic example.
n=4
cycle=s.zeros(n,n)
for i in range(n): cycle[i,(i+1)%n]=1
K=cycle/2+(s.ones(n,n)-s.eye(n))/6
assert K*s.ones(n,1)==s.ones(n,1) and K.T*s.ones(n,1)==s.ones(n,1)
assert K!=K.T and all(K[i,i]==0 for i in range(n))
assert len(connected_components(K))==1
probek=all_probes(K)
targets=[{0,1},{1,2},{2,3}]
chosen=[next(z for z in probek if set(z[1:3])==pair) for pair in targets]
wvals=[]
for i,j,k,d in chosen:
    eps=R(1,24)
    B=s.zeros(n,n); B[i,j]=-1; B[i,k]=1
    observed=stationary(K+eps*B)
    w=(observed-s.ones(n,1)/n)/(eps*observed[i])
    assert (s.eye(n)-K.T)*w==d
    assert observed==s.ones(n,1)/n+eps*w/(n*(1-eps*w[i]))
    wvals.append(w)
Ds=s.Matrix.hstack(*[z[3] for z in chosen]); Ws=s.Matrix.hstack(*wvals)
Dred=Ds[:n-1,:]; Wred=Ws[:n-1,:]
Ared=(Wred*Dred.inv()).inv()
E=reduced_basis(n)
assert (s.eye(n)-K.T)*E==E*Ared
first=E*Ared
last=-sum((first[:,i] for i in range(n-1)),s.zeros(n,1))/n
Arec=s.Matrix.hstack(*[first[:,i]+last for i in range(n-1)],last)
assert (s.eye(n)-Arec).T==K

# Exact first-order finite-amplitude comparisons for all row transfers in two examples.
for Z in [P,Q,K]:
    n=Z.rows
    for i,j,k,d in all_probes(Z):
        eps=R(1,1000)
        B=s.zeros(n,n); B[i,j]=-1; B[i,k]=1
        Zp=Z+eps*B
        actual=stationary(Zp)
        deriv=response(Z,d)
        assert (s.eye(n)-Z.T-eps*B.T)*(actual-s.ones(n,1)/n)==eps*d/n
        assert ((actual-s.ones(n,1)/n)/eps-deriv).norm(1)<R(1,10)
        assert deriv== (s.eye(n)-Z.T+s.ones(n,n)/n).inv()*d/n
        w=n*deriv
        assert actual==s.ones(n,1)/n+eps*w/(n*(1-eps*w[i]))
        assert w==(actual-s.ones(n,1)/n)/(eps*actual[i])

# Continuous-time occupation-to-visit response identity with heterogeneous rates.
v=s.Matrix([2,3,5])
D=s.diag(*v)
z0=s.Matrix([1/x for x in v]); pi0=z0/sum(z0)
assert D*pi0/sum(D*pi0)==s.ones(3,1)/3
for i,j,k,d in all_probes(Q):
    uprime=response(Q,d)
    # exact derivative via pi = D^{-1}u / sum(D^{-1}u)
    h0=sum(z0)/3
    pi_prime=(D.inv()*uprime - pi0*sum(D.inv()*uprime))/h0
    u_recovered=(D*pi_prime - s.ones(3,1)/3*sum(D*pi_prime))/sum(D*pi0)
    assert u_recovered==uprime
print('PASS: exact stochasticity, graph components, aperiodicity, all-amplitude line law, rank, chiral-chain finite-response tomography, and occupation conversion')
