"""Independent direct H_2 character computation from an integral torus basis.
Run `python check_character_direct.py` in this directory; see requirements.txt.
"""
from collections import Counter
from sympy import Matrix
import verify as v

B=v.B
rows=v.rows
Rinv=B[rows,:].inv()
found=Counter()
for a in v.AUTOS:
    diag=[]
    for k in range(B.cols):
        image=[0]*len(v.TWOS)
        for i,(e,f) in enumerate(v.TWOS):
            coeff=int(B[i,k])
            if not coeff:continue
            ep=(a[e[0]],a[e[1]]); fp=(a[f[0]],a[f[1]])
            es=tuple(sorted(ep));fs=tuple(sorted(fp))
            sign=(1 if ep==es else -1)*(1 if fp==fs else -1)*(1 if es<fs else -1)
            image[v.TI[(es,fs) if es<fs else (fs,es)]]+=sign*coeff
        coords=Rinv*Matrix([image[i] for i in rows])
        assert B*coords==Matrix(image)
        diag.append(int(coords[k]))
    found[sum(diag)]+=1
assert found==Counter({-4:13,0:66,2:16,20:1})
assert sum(k*n for k,n in found.items())==0
print('DIRECT_H2_CHARACTER',dict(sorted(found.items())))
print('DIRECT_AUTOMORPHISM_FIXED_RANK',0)
print('VERIFY_OK_DIRECT_MOBIUS_KANTOR_H2_CHARACTER')
