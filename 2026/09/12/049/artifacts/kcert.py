from fractions import Fraction as Fr
import sympy as sp
# Rank certificate: exhibit an explicit invertible 12x12 rational minor for the S_A system,
# and verify: (i) all entries integers (small), (ii) det != 0, (iii) identity-system nullity 3 basis.
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
T=(Fr(0),Fr(1),Fr(0)); T2=mul(T,T)
p0=sub((Fr(2),Fr(0),Fr(0)),T2); pt=neg(T); TWO=(Fr(2),Fr(0),Fr(0))
M0=((ZERO,neg(ONE)),(ONE,p0))
M1=((ONE,ONE),(sub(p0,TWO),sub(p0,ONE)))
d=(Fr(-1),Fr(0),Fr(0)); e=(Fr(0),Fr(-2),Fr(1)); f=(Fr(-2),Fr(1),Fr(1))
def matmul(A,B):
    return ((add(mul(A[0][0],B[0][0]),mul(A[0][1],B[1][0])),add(mul(A[0][0],B[0][1]),mul(A[0][1],B[1][1]))),
            (add(mul(A[1][0],B[0][0]),mul(A[1][1],B[1][0])),add(mul(A[1][0],B[0][1]),mul(A[1][1],B[1][1]))))
Mt=((d,e),(f,sub(pt,d)))
P=matmul(matmul(Mt,M1),M0)
Minf=((P[1][1],neg(P[0][1])),(neg(P[1][0]),P[0][0]))
def emC(ex,ey,ez):
    c1=sp.Matrix([ex,ey,ez]); c2=sp.Matrix([ez,ex+2*ez,ey-ez]); c3=sp.Matrix([ey-ez,2*ey-ez,ex-ey+3*ez])
    return sp.Matrix.hstack(c1,c2,c3)
def sysmat(pairs):
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
    return sp.Matrix(rows)
SA=[(M0,M1),(M1,M0),(Mt,Minf),(Minf,Mt)]
M=sysmat(SA)
print("shape",M.shape,"rank",M.rank())
# find 12 independent rows greedily
sel=[]
for i in range(M.rows):
    T2m=M.extract(sel+[i],list(range(12)))
    if T2m.rank()==len(sel)+1: sel.append(i)
print("indep rows:",sel)
B=M.extract(sel,list(range(12)))
print("det minor:",B.det())
print("max abs entry:",max(abs(int(v)) for v in M))
# identity nullspace basis
MI=sysmat([(M0,M0),(M1,M1),(Mt,Mt)])
print("identity rank",MI.rank(),"null",12-MI.rank())
print("null basis:",MI.nullspace())
# single-pair ranks
print("single01 rank",sysmat([(M0,M1)]).rank(),"null",12-sysmat([(M0,M1)]).rank())
print("single t-inf rank",sysmat([(Mt,Minf)]).rank(),"null",12-sysmat([(Mt,Minf)]).rank())
# save minor rows + det to file
with open("rank_certificate.txt","w") as fh:
    fh.write("independent row indices: %s\n" % sel)
    fh.write("minor det: %s\n" % B.det())
    fh.write("matrix rows (all %d x 12, integer entries):\n" % M.rows)
    for i,r in enumerate(M.tolist()):
        fh.write("%02d %s\n" % (i,[int(v) for v in r]))
print("wrote rank_certificate.txt")
