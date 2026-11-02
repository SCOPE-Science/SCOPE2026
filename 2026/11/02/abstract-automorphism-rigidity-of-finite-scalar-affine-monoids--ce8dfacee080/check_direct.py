"""Independent brute-force multiplication-table automorphism counts for small prime fields."""
from itertools import permutations, product

def count_direct(p,d):
    points=list(product(range(p), repeat=d))
    els=[(z,v) for z in range(p) for v in points]
    ix={v:i for i,v in enumerate(els)}
    def mul(a,b):
        z,v=a; w,u=b
        return (z*w%p, tuple((x+z*y)%p for x,y in zip(v,u)))
    tab=[[ix[mul(a,b)] for b in els] for a in els]
    # Identity is (z=1,v=0), fixed by all monoid automorphisms.
    ident=ix[(1, (0,)*d)]
    # Characteristic left-zero ideal must be mapped to itself.
    left=[i for i in range(len(els)) if all(tab[i][j]==i for j in range(len(els)))]
    right=[i for i in range(len(els)) if i not in left and i!=ident]
    assert len(left)==p**d
    choices=[None]*len(els)
    choices[ident]=ident
    count=0
    for lp in permutations(left):
        for rp in permutations(right):
            for i,j in zip(left,lp):choices[i]=j
            for i,j in zip(right,rp):choices[i]=j
            if all(choices[tab[a][b]]==tab[choices[a]][choices[b]] for a in range(len(els)) for b in range(len(els))):
                count+=1
    return count

for p,d,expected in [(2,1,2),(2,2,24),(3,1,6)]:
    actual=count_direct(p,d)
    assert actual==expected,(p,d,actual,expected)
    print(f'DIRECT p={p} d={d}: all monoid permutations tested; automorphisms={actual} PASS')
print('VERIFY_OK')
