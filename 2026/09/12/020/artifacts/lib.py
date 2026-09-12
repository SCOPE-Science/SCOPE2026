"""Exact integer / Q(omega) linear algebra + Sturm isolation (stdlib only)."""
from fractions import Fraction as F

# ---------- polynomials: lowest-first coefficient lists ----------
def pdeg(p):
    d = len(p)-1
    while d > 0 and p[d] == 0: d -= 1
    return d
def pnorm(p):
    d = pdeg(p)
    return list(p[:d+1])
def padd(a,b):
    n = max(len(a),len(b)); return [ (a[i] if i < len(a) else 0)+(b[i] if i < len(b) else 0) for i in range(n)]
def psub(a,b):
    n = max(len(a),len(b)); return [ (a[i] if i < len(a) else 0)-(b[i] if i < len(b) else 0) for i in range(n)]
def pmul(a,b):
    if not a or not b: return [0]
    r = [0]* (len(a)+len(b)-1)
    for i,ca in enumerate(a):
        for j,cb in enumerate(b): r[i+j] += ca*cb
    return pnorm(r)
def pder(p):
    if len(p) <= 1: return [0]
    return [i*p[i] for i in range(1,len(p))]
def peval(p, x):
    r = 0
    for c in reversed(p): r = r*x + c
    return r
def prem_frac(a, b):
    """Remainder of a divided by b over a field (exact)."""
    a = [F(c) for c in a]; b = [F(c) for c in b]
    da = pdeg(a); db = pdeg(b)
    if da < db: return pnorm(a)
    a = list(a)
    lb = b[db]
    while da >= db:
        coeff = a[da]/lb
        for i in range(db+1): a[da-db+i] -= coeff*b[i]
        da = pdeg(a)
    return pnorm(a)

def _content_int(p):
    from math import gcd
    g = 0
    for c in p: g = gcd(g, abs(int(c)))
    return g

def sturm_seq(p_int):
    """Sturm sequence with positive-scaling normalization (signs preserved)."""
    f0 = [F(c) for c in pnorm(p_int)]
    f1 = pder(f0)
    seq = [f0, pnorm(f1)]
    while True:
        r = prem_frac(seq[-2], seq[-1])
        r = pnorm(r)
        if all(c == 0 for c in r): break
        # scale to integers, remove content (both positive scalings)
        dens = 1
        from math import gcd
        for c in r:
            dens = dens * c.denominator // gcd(dens, c.denominator)
        rint = [int(c*dens) for c in r]
        g = _content_int(rint)
        rint = [c//g for c in rint]
        seq.append([-F(c) for c in rint])
        if len(seq) > len(p_int)+2: raise RuntimeError("sturm non-termination")
    return seq

def _signs_right(seq, a):
    """Signs of sequence at a+ (exact one-sided limit)."""
    out = []
    for f in seq:
        v = peval(f, a)
        if v != 0: out.append(1 if v > 0 else -1); continue
        # first nonzero derivative determines right-limit sign
        g = f
        while True:
            g = pder(g)
            if all(c == 0 for c in g):
                out.append(0); break
            v2 = peval(g, a)
            if v2 != 0: out.append(1 if v2 > 0 else -1); break
    return out
def _signs_left(seq, b):
    out = []
    for f in seq:
        v = peval(f, b)
        if v != 0: out.append(1 if v > 0 else -1); continue
        g = f; k = 0
        while True:
            g = pder(g); k += 1
            if all(c == 0 for c in g):
                out.append(0); break
            v2 = peval(g, b)
            if v2 != 0:
                s = 1 if v2 > 0 else -1
                out.append(s if k % 2 == 0 else -s); break
    return out
def _var(signs):
    nz = [s for s in signs if s != 0]
    return sum(1 for i in range(len(nz)-1) if nz[i]*nz[i+1] < 0)
def count_distinct_roots_open(p_int, a, b):
    """Number of distinct roots of integer poly p in open interval (a,b), a,b Fractions."""
    seq = sturm_seq(p_int)
    return _var(_signs_right(seq, a)) - _var(_signs_left(seq, b))

# ---------- Q(omega) arithmetic: (a,b) = a + b*omega, Fractions ----------
def wadd(x,y): return (x[0]+y[0], x[1]+y[1])
def wsub(x,y): return (x[0]-y[0], x[1]-y[1])
def wmul(x,y):
    a,b = x; c,d = y
    return (a*c-b*d, a*d+b*c-b*d)
def wdivint(x,k):
    return (x[0]/k, x[1]/k)
ZERO = (F(0),F(0)); ONE = (F(1),F(0))

def matmul(A,B):
    n=len(A); m=len(B[0]); l=len(B)
    zero = ZERO if isinstance(A[0][0],tuple) else 0
    C=[[zero]*m for _ in range(n)]
    for i in range(n):
        for k in range(l):
            aik=A[i][k]
            if aik==zero: continue
            for j in range(m):
                if isinstance(aik,tuple): C[i][j]=wadd(C[i][j],wmul(aik,B[k][j]))
                else: C[i][j]+=aik*B[k][j]
    return C
def matadd(A,B):
    n=len(A); m=len(A[0])
    C=[[None]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            a=A[i][j]; b=B[i][j]
            C[i][j]=wadd(a,b) if isinstance(a,tuple) else a+b
    return C
def trace(A):
    t=A[0][0]
    for i in range(1,len(A)):
        a=A[i][i]
        t=wadd(t,a) if isinstance(a,tuple) else t+a
    return t

def charpoly_leverrier(A):
    """A: n x n over int or Q(omega) tuples. Returns lowest-first coeffs (highest coeff 1)."""
    n=len(A)
    isw=isinstance(A[0][0],tuple)
    zero=ZERO if isw else 0
    M=[[zero]*n for _ in range(n)]
    cs=[1]  # c_0..c_n placeholder; cs[k] computed
    coeffs=[None]*(n+1)
    coeffs[n]=ONE if isw else 1
    for k in range(1,n+1):
        # M_k = A*M_{k-1} + c_{k-1} I ; with c_0 = 1
        AM=matmul(A,M)
        ck1 = 1 if k-1==0 else coeffs[n-(k-1)]
        for i in range(n):
            if isw: AM[i][i]=wadd(AM[i][i],(F(ck1[0]),F(ck1[1])) if isinstance(ck1,tuple) else (F(ck1),F(0)))
            else: AM[i][i]+=ck1
        M=AM
        AM2=matmul(A,M)
        tr=trace(AM2)
        if isw: ck=wdivint(tr,-k)
        else: ck=-tr/k if isinstance(tr,float) else F(-tr,k)
        coeffs[n-k]=ck
    return coeffs  # lowest-first? coeffs[i] for x^i: coeffs[n-k] is c_k for x^{n-k}. index = power. yes lowest-first.

def bareiss_det(A):
    """Exact det of integer matrix (list of lists)."""
    n=len(A); M=[row[:] for row in A]
    prev=1
    for k in range(n-1):
        if M[k][k]==0:
            piv=None
            for i in range(k+1,n):
                if M[i][k]!=0: piv=i; break
            if piv is None: return 0
            M[k],M[piv]=M[piv],M[k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                M[i][j]=(M[i][j]*M[k][k]-M[i][k]*M[k][j])//prev
            M[i][k]=0
        prev=M[k][k]
    return M[n-1][n-1]

def charpoly_at_via_bareiss(Aint, t):
    n=len(Aint)
    M=[[ (t if i==j else 0)-Aint[i][j] for j in range(n)] for i in range(n)]
    return bareiss_det(M)

def sturm_count(seq, a, b):
    return _var(_signs_right(seq, a)) - _var(_signs_left(seq, b))
