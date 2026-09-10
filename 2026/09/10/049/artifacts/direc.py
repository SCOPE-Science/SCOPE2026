import numpy as np
P=13
XS=np.arange(P)
INV=np.zeros(P,dtype=np.int64)
for d in range(1,P): INV[d]=pow(d,-1,P)
def ndirs_of_vals(f):
    s=set()
    for x in range(P):
        fx=int(f[x])
        for y in range(x+1,P):
            s.add(((fx-int(f[y]))*int(INV[(x-y)%P]))%P)
    return s
def eval_coeff(coeff_lo, p=P):
    # coeff lowest-first
    r=np.zeros(P,dtype=np.int64)
    for c in reversed(coeff_lo):
        r=(r*XS+c)%p
    return r
