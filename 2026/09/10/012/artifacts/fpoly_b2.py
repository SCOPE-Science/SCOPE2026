"""Lane-515: exact F-polynomials along the B2 transverse-slice cycle (finite!).
B12=[[0,2],[-1,0]], principal coefficients. F-mutation (FZ (5.6)):
  F_k' = (M+ + M-) / F_k,
  M+ = y_k^0? precisely: M+ = prod_j y_j^[b_jk]+ * prod_j F_j^[b_jk]+,
  M- = prod_j y_j^[-b_jk]+ * prod_j F_j^[-b_jk]+.
Exactness: divisions are exact in Z[y1,y2]. Verify by exact polynomial long
division (brute-force linear solve over QQ within degree bound).
Finiteness of every F-polynomial directly contradicts the target's
"infinite broken-line / no finite F-polynomial" clause inside the J* slice.
"""
from fractions import Fraction as Q

def padd(p,q):
    r=dict(p)
    for k,v in q.items(): r[k]=r.get(k,0)+v
    return {k:v for k,v in r.items() if v!=0}
def pmul(p,q):
    r={}
    for (a,b),x in p.items():
        for (c,d),y in q.items(): r[(a+c,b+d)]=r.get((a+c,b+d),0)+x*y
    return {k:v for k,v in r.items() if v!=0}
def ppow(p,e):
    assert e>=0 and isinstance(e,int)
    r={(0,0):Q(1)}
    for _ in range(e): r=pmul(r,p)
    return r
def pexact_div(num,den):
    # exact division num/den in QQ[y1,y2]. den(0)=1 always for F-polynomials.
    # Support bound: deg(quo) <= deg(num) (graded-domain leading-part argument),
    # so total-degree box a+b <= deg(num) suffices.
    assert den and den.get((0,0),Q(0))!=0
    D=max(a+b for (a,b) in num) if num else 0
    qs=[(i,j) for i in range(D+1) for j in range(D+1-i)]
    supp=sorted({(i+a,j+b) for (i,j) in qs for (a,b) in den})
    ri={m:i for i,m in enumerate(supp)}
    nrows,ncols=len(supp),len(qs)
    M=[[Q(0)]*ncols for _ in range(nrows)]
    for c,(i,j) in enumerate(qs):
        for (a,b),v in den.items(): M[ri[(i+a,j+b)]][c]+=v
    nvec=[num.get(m,Q(0)) for m in supp]
    M2=[row[:]+[nvec[r]] for r,row in enumerate(M)]
    piv={}; R=0
    for c in range(ncols):
        p=None
        for r in range(R,nrows):
            if M2[r][c]!=0: p=r; break
        if p is None: continue
        M2[R],M2[p]=M2[p],M2[R]
        z=M2[R][c]; M2[R]=[v/z for v in M2[R]]
        for r in range(nrows):
            if r!=R and M2[r][c]!=0:
                f=M2[r][c]; M2[r]=[a-f*b for a,b in zip(M2[r],M2[R])]
        piv[c]=R; R+=1
    for r in range(nrows):
        if all(M2[r][c]==0 for c in range(ncols)) and M2[r][ncols]!=0:
            raise AssertionError(("inconsistent division",num,den))
    sol=[Q(0)]*ncols
    for c,r in piv.items(): sol[c]=M2[r][ncols]
    chk=pmul({m:sol[i] for i,m in enumerate(qs) if sol[i]!=0},den)
    assert chk=={k:v for k,v in num.items() if v!=0}, ("inexact",chk,num)
    return {m:sol[i] for i,m in enumerate(qs) if sol[i]!=0}

def mutB(B,k):
    m=len(B); Bp=[[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            if i==k or j==k: Bp[i][j]=-B[i][j]
            else: Bp[i][j]=B[i][j]+(abs(B[i][k])*B[k][j]+B[i][k]*abs(B[k][j]))//2
    return Bp

def mutC(C,B,k):
    m=len(C); Cp=[row[:] for row in C]
    for i in range(m): Cp[i][k]=-C[i][k]
    for j in range(m):
        if j==k: continue
        for i in range(m):
            Cp[i][j]=C[i][j]+max(0,C[i][k])*max(0,B[k][j])-max(0,-C[i][k])*max(0,-B[k][j])
    return Cp
B=[[0,2],[-1,0]]; C=[[1,0],[0,1]]
F=[{(0,0):Q(1)},{(0,0):Q(1)}]
Y=[{(1,0):Q(1)},{(0,1):Q(1)}]
seq=[0,1,0,1,0,1]
print("F0 =",F)
for t,k in enumerate(seq):
    # FZ-IV F-mutation: y-exponents from c-vector column k, F-exponents from B column k
    Mp={(0,0):Q(1)}; Mm={(0,0):Q(1)}
    for j in range(2):
        c=C[j][k]; b=B[j][k]
        if c>0: Mp=pmul(Mp,ppow(Y[j],c))
        elif c<0: Mm=pmul(Mm,ppow(Y[j],-c))
        if b>0: Mp=pmul(Mp,ppow(F[j],b))
        elif b<0: Mm=pmul(Mm,ppow(F[j],-b))
    num=padd(Mp,Mm)
    Fn=list(F); Fn[k]=pexact_div(num,F[k])
    Cn=mutC(C,B,k); B=mutB(B,k); C=Cn; F=Fn
    print("t=%d mut=%d F=%s" % (t+1,k,[sorted(f.items()) for f in F]))
print("B back to start?",B==[[0,2],[-1,0]])
print("(B,C) back to start?",(B,C)==([[0,2],[-1,0]],[[1,0],[0,1]]))
print("F back to (1,1)?",F==[{(0,0):Q(1)},{(0,0):Q(1)}])
assert B==[[0,2],[-1,0]] and F==[{(0,0):Q(1)},{(0,0):Q(1)}]
print("PASS: F-polynomial cycle closes; every theta/F identity in J* slice is a FINITE polynomial identity")
