"""Complete GF(2) enumeration of quartic forms on P^3 vanishing at its 15 F2-points.
Run: python census_monomials.py. Python standard library only.
"""
from collections import Counter
from itertools import product

MON = [m for m in product(range(5), repeat=4) if sum(m)==4]
assert len(MON)==35
P = range(1, 16)

def mon_eval(exp, p):
    return int(all(e == 0 or (p >> j) & 1 for j,e in enumerate(exp)))

vals=[]; grads=[]
for m in MON:
    vals.append(sum(mon_eval(m,p)<<k for k,p in enumerate(P)))
    g=0
    for k,p in enumerate(P):
        for i,e in enumerate(m):
            if e % 2:
                deriv=tuple(ej-(j==i) for j,ej in enumerate(m))
                if mon_eval(deriv,p):g|=1<<(4*k+i)
    grads.append(g)

piv={}; kernel=[]
for i,a in enumerate(vals):
    c=1<<i
    while a:
        j=a.bit_length()-1
        if j not in piv:
            piv[j]=(a,c)
            break
        a^=piv[j][0]
        c^=piv[j][1]
    else:kernel.append(c)
assert len(piv)==15 and len(kernel)==20
B=[]
for m in kernel:
    e=0;g=0
    for i in range(35):
        if m>>i&1:e^=vals[i];g^=grads[i]
    assert e==0
    B.append(g)

hist=Counter(); zeros=Counter(); v=0
for idx in range(1<<20):
    if idx:v ^= B[(idx&-idx).bit_length()-1]
    planes=0; z=0
    for p in range(15):
        g=(v>>(4*p))&15
        if g:planes |= 1<<g
        else:z+=1
    if z:zeros[z]+=1
    else:hist[planes.bit_count()]+=1
assert hist=={10:24192,11:80640,12:20160}
assert sum(hist.values())==124992
assert sum(zeros.values())+sum(hist.values())==1<<20
print('degree_four_monomials',len(MON))
print('evaluation_rank',len(piv))
print('vanishing_space_dimension',len(kernel))
print('total_forms',1<<20)
print('rationally_nonsingular',sum(hist.values()))
print('tangent_plane_histogram',sorted(hist.items()))
print('max_distinct_tangent_planes',max(hist))
