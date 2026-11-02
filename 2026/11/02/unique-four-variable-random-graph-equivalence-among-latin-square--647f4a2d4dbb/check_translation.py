"""Independent coordinate-level check using translation symmetry.
Distinct representatives of every ordered pair of nonzero relative anchor points.
Every witness candidate is tested by literal row/column/symbol comparisons.
"""
Q=8
cells=[(a,b,a^b) for a in range(Q) for b in range(Q)]
zero=(0,0,0)

def adjacent(x,y):
    return x!=y and (x[0]==y[0] or x[1]==y[1] or x[2]==y[2])

count=0
m=Q*Q+1
for i,y in enumerate(cells):
    if y==zero: continue
    for z in cells:
        if z==zero or z==y:continue
        masks=0
        for w in cells:
            if w==zero or w==y or w==z:continue
            pattern=(int(adjacent(w,zero)) + 2*int(adjacent(w,y)) + 4*int(adjacent(w,z)))
            masks|=1<<pattern
        if masks!=255:raise AssertionError((i,y,z,masks))
        count+=1
print('translation_orbit_representative',zero)
print('ordered_relative_pairs',count)
print('checked_patterns',8*count)
print('minimum_supported_patterns_per_pair',8)
print('graph_3_ec',True)
