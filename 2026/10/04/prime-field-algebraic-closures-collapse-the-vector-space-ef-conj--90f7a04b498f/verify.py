from fractions import Fraction

# Q(sqrt(2)) represented as a+b*r with r^2=2.
def add(x,y): return (x[0]+y[0], x[1]+y[1])
def mul(x,y): return (x[0]*y[0]+2*x[1]*y[1], x[0]*y[1]+x[1]*y[0])
def neg(x): return (-x[0],-x[1])
ZERO=(Fraction(0),Fraction(0)); ONE=(Fraction(1),Fraction(0)); R=(Fraction(0),Fraction(1))

def vadd(u,v): return tuple(add(a,b) for a,b in zip(u,v))
def smul(c,u): return tuple(mul(c,a) for a in u)

def qrank(cols):
    # cols are rational-coordinate columns; exact Gaussian elimination.
    A=[list(row) for row in zip(*cols)]
    m=len(A); n=len(A[0]) if m else 0; r=0
    for c in range(n):
        piv=next((i for i in range(r,m) if A[i][c]),None)
        if piv is None: continue
        A[r],A[piv]=A[piv],A[r]
        z=A[r][c]; A[r]=[x/z for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                z=A[i][c]; A[i]=[a-z*b for a,b in zip(A[i],A[r])]
        r+=1
    return r

def flatten_q(v):
    out=[]
    for a,b in v: out.extend([a,b])
    return out

for m in range(2,9):
    e=[]
    for i in range(m):
        v=[ZERO]*m; v[i]=ONE; e.append(tuple(v))
    wlast=vadd(e[0], smul(R,e[-1]))
    ws=e+[wlast]
    assert qrank([flatten_q(v) for v in ws])==m+1
    rel=vadd(vadd(wlast, smul(neg(ONE),e[0])), smul(neg(R),e[-1]))
    assert all(x==ZERO for x in rel)
print('VERIFY_OK m=2..8 qlinear_independence_and_named_scalar_exposure')
