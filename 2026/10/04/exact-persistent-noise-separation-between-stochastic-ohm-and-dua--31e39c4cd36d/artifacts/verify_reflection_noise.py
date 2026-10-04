from fractions import Fraction as Q
from math import pi

def add(a,b):
    out=dict(a)
    for k,v in b.items():
        out[k]=out.get(k,Q(0))+v
        if out[k]==0:
            del out[k]
    return out

def scale(c,a):
    return {k:c*v for k,v in a.items() if c*v}

def dual_terminal(N):
    x=[{"x0":Q(1)}]
    qprev={"x0":Q(1)}
    for k in range(N-1):
        q=add(scale(Q(-1),x[k]), {f"e{k}":Q(-1)})  # alpha normalized to 1
        ak=Q(N-k-1,N-k)
        xnext=add(x[k],scale(ak,add(q,scale(Q(-1),qprev))))
        x.append(xnext)
        qprev=q
    return x[-1]

def ohm_terminal(N):
    x={"x0":Q(1)}
    for k in range(N-1):
        q=add(scale(Q(-1),x), {f"e{k}":Q(-1)})
        x=add({"x0":Q(1,k+2)},scale(Q(k+1,k+2),q))
    return x

def c_reflect(m):
    if m%2==0:
        return Q(1,2*(m-1))
    return Q(-1,2*m)

for N in range(2,25):
    d=dual_terminal(N)
    h=ohm_terminal(N)
    det=Q(1,N) if N%2 else Q(0)
    assert d.get("x0",Q(0))==det
    assert h.get("x0",Q(0))==det
    for j in range(N-1):
        assert d.get(f"e{j}",Q(0)) == -c_reflect(N-j)
        expected = -Q(j+1,N) * (Q(-1) ** (N-2-j))
        assert h.get(f"e{j}",Q(0)) == expected

    dual_var = sum(v*v for k,v in d.items() if k.startswith("e"))
    D = Q(0)
    for m in range(2,N+1):
        if m%2==0:
            D += Q(1,(m-1)**2)
        else:
            D += Q(1,m**2)
    assert 4*dual_var == D

    ohm_var = sum(v*v for k,v in h.items() if k.startswith("e"))
    closed = Q((N-1)*(2*N-1),6*N)
    assert ohm_var == closed

limit = pi*pi/4 - 1
assert 1.46 < limit < 1.48
print("VERIFY_OK")
