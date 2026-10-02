"""Exact fraction-free positive-definiteness certificates for the explicit
SL(2,7) Cayley witness.  No scratch files are required.

Usage:
    python3 artifacts/bareiss_cert.py lo
    python3 artifacts/bareiss_cert.py up
"""
import sys, time
q=7
M=[(a,b,c,d) for a in range(q) for b in range(q) for c in range(q) for d in range(q) if (a*d-b*c)%q==1]
n=len(M); idx={m:i for i,m in enumerate(M)}
def mul(X,Y):
    a,b,c,d=X; e,f,g,h=Y
    return ((a*e+b*g)%q,(a*f+b*h)%q,(c*e+d*g)%q,(c*f+d*h)%q)
SR=[(6,0,0,6),(4,2,6,5),(2,4,5,0),(1,4,0,1),(5,5,1,4),(0,3,2,2),(1,3,0,1)]
nbr=[[idx[mul(x,g)] for g in SR] for x in M]
def build(which):
    if which=='lo':
        A=[[0]*n for _ in range(n)]
        for i in range(n):
            A[i][i]=489
            for j in nbr[i]: A[i][j]+=100
        return A,'M_lo=100A+489I'
    if which=='up':
        A=[[21436]*n for _ in range(n)]
        for i in range(n):
            for j in nbr[i]: A[i][j]-=3360000
            A[i][i]+=16430400
        return A,'M_up=16430400I-3360000A+21436J'
    raise SystemExit('choose lo or up')
def bareiss_sym(A):
    prev=1; minpivot=None
    for k in range(n-1):
        piv=A[k][k]
        if piv<=0: return False,k,piv
        minpivot=piv if minpivot is None or piv<minpivot else minpivot
        Ak=A[k]
        for i in range(k+1,n):
            Ai=A[i]; aik=Ai[k]
            for j in range(i,n): Ai[j]=(Ai[j]*piv-aik*Ak[j])//prev
            for j in range(i,n): A[j][i]=Ai[j]
            Ai[k]=0
        prev=piv
    last=A[n-1][n-1]
    return last>0,minpivot,last
which=sys.argv[1] if len(sys.argv)>1 else 'lo'
A,tag=build(which); t=time.time(); ok,info,last=bareiss_sym(A)
print(f'{tag}: PD={ok} min_pivot={info} determinant_digits={len(str(last))} elapsed={time.time()-t:.1f}s')
assert ok
print('BAREISS_CERT_OK')
