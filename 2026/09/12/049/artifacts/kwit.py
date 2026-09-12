from fractions import Fraction as Fr
import sympy as sp
ZERO=(Fr(0),Fr(0),Fr(0)); ONE=(Fr(1),Fr(0),Fr(0))
def add(x,y): return (x[0]+y[0],x[1]+y[1],x[2]+y[2])
def neg(x): return (-x[0],-x[1],-x[2])
def sub(x,y): return (x[0]-y[0],x[1]-y[1],x[2]-y[2])
def mul(x,y):
    a0,a1,a2=x; b0,b1,b2=y
    c=[Fr(0)]*5
    a=[a0,a1,a2]; b=[b0,b1,b2]
    for i in range(3):
        for j in range(3):
            c[i+j]+=a[i]*b[j]
    c0,c1,c2,c3,c4=c
    return (c0+c3-c4, c1+2*c3-c4, c2-c3+3*c4)
def matmul(A,B):
    return ((add(mul(A[0][0],B[0][0]),mul(A[0][1],B[1][0])),add(mul(A[0][0],B[0][1]),mul(A[0][1],B[1][1]))),
            (add(mul(A[1][0],B[0][0]),mul(A[1][1],B[1][0])),add(mul(A[1][0],B[0][1]),mul(A[1][1],B[1][1]))))
T=(Fr(0),Fr(1),Fr(0)); T2=mul(T,T)
p0=sub((Fr(2),Fr(0),Fr(0)),T2); pt=neg(T); TWO=(Fr(2),Fr(0),Fr(0))
M0=((ZERO,neg(ONE)),(ONE,p0))
M1=((ONE,ONE),(sub(p0,TWO),sub(p0,ONE)))
d=(Fr(-1),Fr(0),Fr(0)); e=(Fr(0),Fr(-2),Fr(1)); f=(Fr(-2),Fr(1),Fr(1))
Mt=((d,e),(f,sub(pt,d)))
P=matmul(matmul(Mt,M1),M0)
Minf=((P[1][1],neg(P[0][1])),(neg(P[1][0]),P[0][0]))
def emC(ex,ey,ez):
    c1=sp.Matrix([ex,ey,ez]); c2=sp.Matrix([ez,ex+2*ez,ey-ez]); c3=sp.Matrix([ey-ez,2*ey-ez,ex-ey+3*ez])
    return sp.Matrix.hstack(c1,c2,c3)
def nullity(pairs):
    rows=[]
    def vi(r,c,k): return (r*2+c)*3+k
    for (X,Y) in pairs:
        for i in range(2):
            for j in range(2):
                kd={}
                for l in range(2):
                    kd[(i,l)]=add(kd.get((i,l),ZERO),X[l][j])
                    kd[(l,j)]=add(kd.get((l,j),ZERO),neg(Y[i][l]))
                for k2 in range(3):
                    row=[sp.Integer(0)]*12
                    for (r,c),kv in kd.items():
                        Mm=emC(*[int(v) for v in kv])
                        for k in range(3):
                            row[vi(r,c,k)]+=Mm[k2,k]
                    rows.append(row)
    M=sp.Matrix(rows)
    return 12-M.rank(), M.rank()
tests={
 "identity (sanity: M0->M0,M1->M1,Mt->Mt)": [(M0,M0),(M1,M1),(Mt,Mt)],
 "fold-swap S_A: M0<->M1, Mt<->Minf": [(M0,M1),(M1,M0),(Mt,Minf),(Minf,Mt)],
 "swap S_B: M0<->Mt, M1<->Minf": [(M0,Mt),(Mt,M0),(M1,Minf),(Minf,M1)],
 "swap S_C: M0<->Minf, M1<->Mt": [(M0,Minf),(Minf,M0),(M1,Mt),(Mt,M1)],
 "single M0->M1 only": [(M0,M1)],
 "single Mt->Minf only": [(Mt,Minf)],
}
for name,pairs in tests.items():
    n,r=nullity(pairs); print(name,"-> nullity",n,"rank",r)
# numeric irreducibility
import math
t=2*math.cos(2*math.pi/7)
def num(x): return float(x[0])+float(x[1])*t+float(x[2])*t*t
import numpy as np
def nm(M): return np.array([[num(v) for v in row] for row in M])
N0,N1,Nt,Ni=nm(M0),nm(M1),nm(Mt),nm(Minf)
print("traces:",np.trace(N0),np.trace(N1),np.trace(Nt),np.trace(Ni))
for n,X in [("01",N0@N1),("0t",N0@Nt),("1t",N1@Nt),("0i",N0@Ni),("ti",Nt@Ni),("1i",N1@Ni)]:
    print("tr",n,float(np.trace(X)))
def shared(A,B):
    wA,vA=np.linalg.eig(A); wB,vB=np.linalg.eig(B); best=1e9
    for i in range(2):
        for j in range(2):
            a=vA[:,i]/np.linalg.norm(vA[:,i]); b=vB[:,j]/np.linalg.norm(vB[:,j])
            best=min(best,abs(abs(np.vdot(a,b))-1))
    return best
print("shared01",shared(N0,N1),"shared0t",shared(N0,Nt),"shared1t",shared(N1,Nt))
