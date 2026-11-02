"""Exact integer verifier for the theta-section special-fibre support formula.
No claim of exhaustive proof of the infinite parameter range.
"""
def minima_signature(d,e,f,N):
    D=N*d
    out=[]
    for c in range(D):
        vals=[]
        for k in range(-100,101):
            A=k*(N*e+c)+D*k*(k-1)//2
            B=k*(N*f+c)+D*k*(k-1)//2
            vals.append((A,B,k))
        ma=min(t[0] for t in vals)
        mb=min(t[1] for t in vals)
        hits=[c+k*D for a,b,k in vals if a==ma and b==mb]
        if hits:
            out.append(tuple(hits))
    return out

def theoretical(d,e,f,N):
    lo=-N*min(e,f)
    hi=N*(d-max(e,f))
    if hi<lo:return []
    if e!=f:return [(c,) for c in range(lo,hi+1)]
    return [(lo,hi)]+[(c,) for c in range(lo+1,hi)]

for d in range(1,8):
 for e in range(-4,5):
  for f in range(-4,5):
   for N in range(1,5):
    actual=minima_signature(d,e,f,N)
    exp=theoretical(d,e,f,N)
    assert sorted(actual)==sorted(exp),(d,e,f,N,actual,exp)
print('VERIFY_OK: 2,268 parameter quadruples, all exact integer valuation calculations')
