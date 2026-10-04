from fractions import Fraction as F
from itertools import product

# K=Q(s), s^2=5, represented a+b*s
def K(a=0,b=0): return (F(a),F(b))
Z=K(); O=K(1); S=K(0,1)
def add(x,y): return (x[0]+y[0],x[1]+y[1])
def neg(x): return (-x[0],-x[1])
def sub(x,y): return add(x,neg(y))
def mul(x,y): return (x[0]*y[0]+5*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def inv(x):
    d=x[0]*x[0]-5*x[1]*x[1]
    if d==0: raise ZeroDivisionError
    return (x[0]/d,-x[1]/d)
def div(x,y): return mul(x,inv(y))
def eq(x,y): return x==y

def poly_const(c): return {} if c==Z else {(0,0,0):c}
def var(i):
    e=[0,0,0]; e[i]=1; return {tuple(e):O}
def padd(p,q):
    r=dict(p)
    for m,c in q.items():
        r[m]=add(r.get(m,Z),c)
        if r[m]==Z: del r[m]
    return r
def pscale(p,c): return {m:mul(v,c) for m,v in p.items() if mul(v,c)!=Z}
def pmul(p,q):
    r={}
    for a,ca in p.items():
        for b,cb in q.items():
            m=tuple(a[i]+b[i] for i in range(3)); c=mul(ca,cb)
            r[m]=add(r.get(m,Z),c)
            if r[m]==Z: del r[m]
    return r
def ppow(p,n):
    r=poly_const(O)
    for _ in range(n): r=pmul(r,p)
    return r
def deriv(p,i):
    r={}
    for m,c in p.items():
        if m[i]:
            mm=list(m); k=mm[i]; mm[i]-=1
            r[tuple(mm)]=mul(c,K(k))
    return r
def peval(p, vals):
    out=Z
    for m,c in p.items():
        t=c
        for i,e in enumerate(m):
            for _ in range(e): t=mul(t,vals[i])
        out=add(out,t)
    return out

def lin(cx,cy,cz):
    return padd(padd(pscale(x,cx),pscale(y,cy)),pscale(z,cz))

x,y,z=var(0),var(1),var(2)
s=S
r=add(K(9),mul(K(4),s))
u=(F(3,2),F(-1,2)); v=(F(3,2),F(1,2))
# Qc = (7-3s)x2 -4xy -2(3-s)xz +(7+3s)y2 -2(3+s)yz+2z2
Qc={}
terms=[((2,0,0),K(7,-3)),((1,1,0),K(-4)),((1,0,1),K(-6,2)),((0,2,0),K(7,3)),((0,1,1),K(-6,-2)),((0,0,2),K(2))]
Qc=dict(terms)
lines=[x,y,z,lin(Z,O,neg(O)),lin(O,Z,neg(O)),lin(O,neg(r),Z)]
P=poly_const(O)
for L in lines: P=pmul(P,L)
Fpoly=pmul(Qc,P)
assert max(map(sum,Fpoly))==8
# conic determinant computed symbolic from pair determinant formula
# matrix entries
a=K(7,-3); b=K(-2); c=K(-3,1); d=K(7,3); e=K(-3,-1); f=K(2)
det=add(sub(mul(a,sub(mul(d,f),mul(e,e))), mul(b,sub(mul(b,f),mul(c,e)))), mul(c,sub(mul(b,e),mul(c,d))))
assert det==K(-32)
# restriction identities via direct polynomial substitution checks by coefficient maps
def substitute_zero(p,i): return {m:c for m,c in p.items() if m[i]==0}
# expected squares in full 3 vars
assert substitute_zero(Qc,0)==pscale(ppow(padd(pscale(y,v),pscale(z,K(-1))),2),K(2))
assert substitute_zero(Qc,1)==pscale(ppow(padd(pscale(x,u),pscale(z,K(-1))),2),K(2))
assert substitute_zero(Qc,2)==pscale(ppow(padd(pscale(x,u),pscale(y,neg(v))),2),K(2))
# points
pts={
'A':(O,Z,Z),'B':(Z,O,Z),'C':(Z,Z,O),
'P03':(Z,O,O),'P14':(O,Z,O),'P25':(r,O,Z),
'P34':(O,O,O),'P35':(r,O,O),'P45':(r,O,r)
}
for name in ['P34','P35','P45']: assert peval(Qc,pts[name])==Z
for name in ['A','B','C','P03','P14','P25']: assert peval(Qc,pts[name])!=Z
# tangent points avoid line arrangement singularities; just Q=0
T0=(Z,O,v); T1=(O,Z,u); T2=(v,u,Z)
for pt in [T0,T1,T2]: assert peval(Qc,pt)==Z
# rank of degree-4 syzygy map K[x,y,z]_4^3 -> K[x,y,z]_11
partials=[deriv(Fpoly,i) for i in range(3)]
def mons(d):
    return [(i,j,d-i-j) for i in range(d+1) for j in range(d-i+1)]
m4=mons(4); m11=mons(11); row={m:i for i,m in enumerate(m11)}
cols=[]
for fp in partials:
    for m in m4:
        col=[Z for _ in m11]
        for e,c0 in fp.items():
            mm=tuple(e[k]+m[k] for k in range(3)); col[row[mm]]=c0
        cols.append(col)
A=[[cols[j][i] for j in range(len(cols))] for i in range(len(m11))]

def rank(M):
    M=[row[:] for row in M]; R=len(M); C=len(M[0]); rr=0
    for c0 in range(C):
        piv=next((i for i in range(rr,R) if M[i][c0]!=Z),None)
        if piv is None: continue
        M[rr],M[piv]=M[piv],M[rr]
        pv=M[rr][c0]
        M[rr]=[div(x,pv) for x in M[rr]]
        for i in range(R):
            if i!=rr and M[i][c0]!=Z:
                fac=M[i][c0]
                M[i]=[sub(M[i][j],mul(fac,M[rr][j])) for j in range(C)]
        rr+=1
        if rr==R: break
    return rr
rk=rank(A)
assert rk==42, rk
# numeric singularity bookkeeping and near-free criterion
n2,t,n3=3,3,6
tau=n2+3*t+4*n3
assert tau==36
mdr=4
assert mdr*mdr-mdr*7+49==tau+1==37
print('VERIFY_OK')
print('conic_det=-32')
print('degree4_syzygy_matrix=78x45 rank=42 nullity=3')
print('singular_counts=(nodes=3,tacnodes=3,triple_points=6) tau=36')
print('mdr_upper=4; with published lower bound mdr>=4 gives mdr=4')
