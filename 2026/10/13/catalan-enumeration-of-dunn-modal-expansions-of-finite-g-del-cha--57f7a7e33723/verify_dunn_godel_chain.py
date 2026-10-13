#!/usr/bin/env python3
from itertools import product
from math import comb

checks = 0

def catalan(n):
    return comb(2*n,n)//(n+1)

def monotone_maps(m, top_fixed=False, bottom_fixed=False):
    for vals in product(range(m), repeat=m):
        if top_fixed and vals[-1] != m-1:
            continue
        if bottom_fixed and vals[0] != 0:
            continue
        if all(vals[i] <= vals[i+1] for i in range(m-1)):
            yield vals

def dunn(box, dia, m):
    global checks
    for a in range(m):
        for b in range(m):
            # D1: box(a v b) <= box(a) v dia(b)
            checks += 1
            if box[max(a,b)] > max(box[a], dia[b]):
                return False
            # D2: box(a) ^ dia(b) <= dia(a ^ b)
            checks += 1
            if min(box[a], dia[b]) > dia[min(a,b)]:
                return False
    return True

for m in range(2,7):
    boxes=list(monotone_maps(m, top_fixed=True))
    dias=list(monotone_maps(m, bottom_fixed=True))
    good=[]
    for box in boxes:
        for dia in dias:
            if dunn(box,dia,m):
                good.append((box,dia))
    normal=[]
    exceptional=[]
    for box,dia in good:
        n=(dia[-1]==m-1 and box[0]==0 and all(box[i] <= dia[i] for i in range(m)))
        e=(all(x==m-1 for x in box) and all(x==0 for x in dia))
        checks += 1
        assert n ^ e
        (normal if n else exceptional).append((box,dia))
    formula=1+(2*m-3)*catalan(m-2)*catalan(m-1)
    checks += 4
    assert len(exceptional)==1
    assert len(good)==formula
    assert len(normal)==formula-1
    # In the normal case both maps fix both endpoints, are monotone, and box<=dia.
    assert all(b[0]==0 and d[-1]==m-1 and all(b[i]<=d[i] for i in range(m)) for b,d in normal)
    print(m, len(good), formula)

# Check the MacMahon-box product simplification used in the proof.
for m in range(2,31):
    # plane partitions in a 2 x (m-2) x (m-1) box
    num=1
    den=1
    for i in range(1,3):
        for j in range(1,m-1):
            num *= i+j+m-2
            den *= i+j-1
    checks += 2
    assert num % den == 0
    mac=num//den
    assert mac==(2*m-3)*catalan(m-2)*catalan(m-1)

print(f'VERIFY_OK {checks} exact assertions/comparisons')
