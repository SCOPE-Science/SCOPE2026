"""Independent direct check that the 8-bit signature records all atoms.

Enumerates the entire 27 multiplication atoms and 9 equality atoms for
all ordered pairs of permutations of degrees up to six, using direct
composition and compares each against the signature class. Does not call
the exact-profile code.
"""
from itertools import permutations,product

def prod(a,b): return tuple(a[k] for k in b)

def atom_diagram(e,x,y):
    tup=(e,x,y)
    equal=tuple(a==b for a,b in product(tup,repeat=2))
    mult=tuple(prod(a,b)==c for a,b,c in product(tup,repeat=3))
    return equal+mult

def eight(e,x,y):
    xx=prod(x,x);yy=prod(y,y)
    return (x==e,y==e,x==y,xx==e,yy==e,xx==y,yy==x,prod(x,y)==e)

for n in range(1,7):
    e=tuple(range(n)); group=list(permutations(range(n)))
    by_key={}
    for x in group:
        for y in group:
            a=eight(e,x,y)
            d=atom_diagram(e,x,y)
            if a in by_key: assert by_key[a]==d
            else: by_key[a]=d
    print(f'degree={n}, ordered_pairs={len(group)**2}, atomic_diagrams={len(by_key)}')
print('ALL_36_ATOMIC_COMPARISONS_REDUCED_PASS')
