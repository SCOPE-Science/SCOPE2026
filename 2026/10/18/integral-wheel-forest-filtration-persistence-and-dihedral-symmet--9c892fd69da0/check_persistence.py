#!/usr/bin/env python3
"""Independent GF(2) persistence reduction of wheel forest filtrations."""
from collections import Counter
from itertools import combinations
from check_wheel import forest_faces,predicted,r_beta


def barcode(m):
    a=m//2
    stages=[forest_faces(m,d) for d in range(2,a+1)]
    grades={}
    for d,fs in enumerate(stages,2):
        for k,faces in fs.items():
            for f in faces:
                grades.setdefault(f,d)
    ordered=sorted(grades,key=lambda s:(grades[s],len(s),s))
    positions={s:i for i,s in enumerate(ordered)}
    piv={}; birth=set(); intervals=Counter()
    for j,f in enumerate(ordered):
        v=0
        for k in range(len(f)) if len(f)>1 else ():
            v^=1<<positions[f[:k]+f[k+1:]]
        while v:
            p=v.bit_length()-1
            if p in piv: v^=piv[p]
            else:break
        if v==0:
            birth.add(j)
        else:
            p=v.bit_length()-1
            piv[p]=v
            if p not in birth:raise RuntimeError('unborn death')
            birth.remove(p)
            b,e=grades[ordered[p]],grades[f]
            if b<e:intervals[(len(ordered[p])-1,b,e)]+=1
    for j in birth:
        if len(ordered[j])>1:
            intervals[(len(ordered[j])-1,grades[ordered[j]],'inf')]+=1
    return intervals


def expected(m):
    a=m//2;r,beta=r_beta(m)
    result=Counter({(m-2,2,'inf'):1,(r+1,r+1,'inf'):beta})
    for d in range(2,a+1):
        v=predicted(m,d)-(beta if d==r+1 else 0)
        if v:result[(d,d,d+1)]+=v
    return result

for m in range(8,11):
    actual=barcode(m);exp=expected(m)
    assert actual==exp,('barcode',m,actual,exp)
    print('m=%d; GF2 bars=%s'%(m,sorted(actual.items(),key=str)))
print('PASS: independent full-matrix persistent homology for m=8,9,10')
