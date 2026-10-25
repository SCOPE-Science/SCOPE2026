"""Exact enumeration and algebraic smoothness checks for binary cubic surfaces.

Run after compiling orbit.cpp:
    g++ -O3 -std=c++17 orbit.cpp -o orbit
    ./orbit > orbit_representatives.csv
    python classify.py
Requires sympy. All arithmetic in the geometric smoothness test is exact over GF(2).
"""
import csv
from collections import Counter
from pathlib import Path
from sympy import symbols, prod, diff, groebner, Integer

ROOT=Path(__file__).resolve().parent
X=symbols('x0:4')
E=[(i,j,k,3-i-j-k) for i in range(4) for j in range(4-i) for k in range(4-i-j)]
assert len(E)==20
MON=[prod(X[j]**e[j] for j in range(4)) for e in E]
EV=[];DER=[]
for p in range(1,16):
    ev=0;de=[0]*4
    for b,e in enumerate(E):
        if all((p>>j)&1 or e[j]==0 for j in range(4)):
            ev|=1<<b
        for a in range(4):
            if e[a]&1 and all((p>>j)&1 or e[j]-(j==a)==0 for j in range(4)):
                de[a]|=1<<b
    EV.append(ev);DER.append(de)

def gauss(mask):
    images=[]
    for k in range(15):
        if ((mask&EV[k]).bit_count()&1)==0:
            normal=sum((((mask&DER[k][j]).bit_count())&1)<<j for j in range(4))
            images.append(normal)
    part=tuple(sorted(Counter(images).values(),reverse=True))
    return part,0 not in images

def smooth(mask):
    f=sum(MON[i] for i in range(20) if mask>>i&1)
    derivatives=[diff(f,x) for x in X]
    for a in range(4):
        v=[X[j] for j in range(4) if j!=a]
        gb=groebner([h.subs(X[a],1) for h in derivatives],*v,order='grevlex',modulus=2)
        if not gb.contains(Integer(1)):return False
    return True

with open(ROOT/'orbit_representatives.csv',newline='',encoding='utf8') as handle:
    representatives=[(int(r['mask']),int(r['orbit_size'])) for r in csv.DictReader(handle)]
assert len(representatives)==141 and sum(n for _,n in representatives)==(1<<20)-1
certificate=[]; distribution=Counter()
for mask,n in representatives:
    partition,rational_smooth=gauss(mask)
    geometric_smooth=rational_smooth and smooth(mask)
    if geometric_smooth:distribution[(sum(partition),partition)]+=n
    certificate.append(dict(mask=mask,orbit_size=n,geometrically_smooth=int(geometric_smooth),rational_point_count=sum(partition),gauss_fiber_partition=';'.join(map(str,partition))))
with open(ROOT/'cubic_orbit_certificate.csv','w',newline='',encoding='utf8') as handle:
    dw=csv.DictWriter(handle,fieldnames=list(certificate[0]));dw.writeheader();dw.writerows(certificate)
with open(ROOT/'gauss_profile.csv','w',newline='',encoding='utf8') as handle:
    writer=csv.writer(handle);writer.writerow(['rational_point_count','gauss_fiber_partition','number_of_equations'])
    for (points,part),number in sorted(distribution.items()):
        writer.writerow([points,';'.join(map(str,part)),number])
print('All cubic projective orbits:',len(representatives))
print('Smooth cubic projective orbits:',sum(c['geometrically_smooth'] for c in certificate))
print('Smooth cubic equations:',sum(c['orbit_size'] for c in certificate if c['geometrically_smooth']))
print('Gauss fiber partitions:',len(distribution))
print('Full distribution:',sorted((n,p,num) for (n,p),num in distribution.items()))
