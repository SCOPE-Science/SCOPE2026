import pickle, time, sys
q=7
M=[(a,b,c,d) for a in range(q) for b in range(q) for c in range(q) for d in range(q) if (a*d-b*c)%q==1]
n=len(M); idx={m:i for i,m in enumerate(M)}
def mul(X,Y):
    a,b,c,d=X; e,f,g,h=Y
    return ((a*e+b*g)%q,(a*f+b*h)%q,(c*e+d*g)%q,(c*f+d*h)%q)
def inv(X):
    a,b,c,d=X
    return (d%q,(-b)%q,(-c)%q,a%q)
W=pickle.load(open("scratch/witnesses.pkl","rb")); SR=W["SR"]
nbr=[[idx[mul(x,g)] for g in SR] for x in M]

def build(which):
    if which=="lo":
        # M_lo = 100*A + 489*I : PD => lammin(A) >= -4.89 > -2*sqrt(6)
        A=[[0]*n for _ in range(n)]
        for i in range(n):
            A[i][i]=489
            for j in nbr[i]: A[i][j]+=100
        return A, "M_lo=100A+489I"
    else:
        # M_up = 16430400*I - 3360000*A + 21436*J : PD => lam2(A) <= 4.89 < 2*sqrt(6)
        A=[[21436]*n for _ in range(n)]
        for i in range(n):
            for j in nbr[i]: A[i][j]-=3360000
            A[i][i]+=16430400
        return A, "M_up=16430400I-3360000A+21436J"

def bareiss_sym(MAT):
    n=len(MAT); prev=1; minpivot=None
    for k in range(n-1):
        piv=MAT[k][k]
        if piv<=0: return False, k, piv
        if minpivot is None or piv<minpivot: minpivot=piv
        Ak=MAT[k]
        for i in range(k+1,n):
            Ai=MAT[i]; aik=Ai[k]
            if aik!=0:
                for j in range(i,n):
                    Ai[j]=(Ai[j]*piv-aik*Ak[j])//prev
                # mirror
                for j in range(i,n): MAT[j][i]=Ai[j]
            else:
                for j in range(i,n):
                    Ai[j]=(Ai[j]*piv)//prev
                for j in range(i,n): MAT[j][i]=Ai[j]
            Ai[k]=0
        prev=piv
    if MAT[n-1][n-1]<=0: return False, n-1, MAT[n-1][n-1]
    return True, minpivot, MAT[n-1][n-1]

which=sys.argv[1] if len(sys.argv)>1 else "lo"
MAT,tag=build(which)
t0=time.time()
ok,info,det=bareiss_sym(MAT)
dt=time.time()-t0
print(f"{tag}: PD={ok} info={info} det_digits={len(str(det))} time={dt:.1f}s", flush=True)
