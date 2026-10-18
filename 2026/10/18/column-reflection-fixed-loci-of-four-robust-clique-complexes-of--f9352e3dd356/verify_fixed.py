"""Independent finite checks for column-reflection fixed loci of 4-robust grid complexes.

Run: python3 verify_grid_reflection.py
No nonstandard dependencies. Exhaustive finite checks support, but do not replace,
the separate all-width combinatorial proof.
"""
from itertools import combinations

def graph(n):
    neighbors = [0] * (3*n)
    for row in range(3):
        for col in range(n):
            a = row*n + col
            for rr, cc in ((row+1,col),(row,col+1)):
                if rr<3 and cc<n:
                    b=rr*n+cc
                    neighbors[a] |= 1<<b
                    neighbors[b] |= 1<<a
    return neighbors

def fixed_complex(n):
    nb = graph(n)
    orbits=[];seen=set()
    for a in range(3*n):
        if a not in seen:
            b=(a//n)*n+(n-1-a%n)
            oo=tuple(sorted(set((a,b))))
            seen.update(oo);orbits.append(oo)
    faces={0}
    for s in range(1,min(4,len(orbits))+1):
        for ix in combinations(range(len(orbits)),s):
            vv=tuple(v for i in ix for v in orbits[i])
            if len(vv)>6:continue
            if any(all((nb[x]>>y & 1)==0 for x,y in combinations(z,2))
                   for z in combinations(vv,4)):
                continue
            faces.add(sum(1<<i for i in ix))
    return orbits,faces

def even_model(n,orbits):
    h=n//2
    # Folded grid: orbit vertices indexed by their smallest column, reordered through dictionary.
    ix={ (orbits[i][0]//n,orbits[i][0]%n):i for i in range(len(orbits)) }
    marks=[ix[row,h-1] for row in range(3)]
    other=[i for i in range(len(orbits)) if i not in marks]
    edges=[]
    for a,b in combinations(other,2):
        ra,ca=divmod(orbits[a][0],n)
        rb,cb=divmod(orbits[b][0],n)
        if abs(ra-rb)+abs(ca-cb)==1: edges.append((a,b))
    result={0}
    for a in range(len(orbits)):result.add(1<<a)
    for a,b in combinations(range(len(orbits)),2):
        if a in marks or b in marks or (a,b) in edges:
            result.add((1<<a)|(1<<b))
    for m in marks:
        for a,b in edges:result.add((1<<m)|(1<<a)|(1<<b))
    for a,b in combinations(marks,2):
        for m in (a,b):
            rr=orbits[m][0]//n
            inward=ix[rr,h-2]
            result.add((1<<a)|(1<<b)|(1<<inward))
    result.add(sum(1<<m for m in marks))
    return result

def betti_mod2(faces):
    deg=max(f.bit_count() for f in faces)
    layers=[[f for f in sorted(faces) if f.bit_count()==j] for j in range(deg+1)]
    ranks=[0]
    for j in range(1,deg+1):
        index={face:i for i,face in enumerate(layers[j-1])}
        pivot={}; rank=0
        for f in layers[j]:
            v=0
            for i in range(f.bit_length()):
                if f>>i&1:v^=1<<index[f^(1<<i)]
            while v:
                key=v.bit_length()-1
                if key not in pivot:
                    pivot[key]=v;rank+=1;break
                v^=pivot[key]
        ranks.append(rank)
    return tuple(len(layers[j])-ranks[j]-(ranks[j+1] if j<deg else 0) for j in range(deg+1))

def verify():
    count=0
    for n in range(3,41):
        orbits,faces=fixed_complex(n)
        if n%2:
            mid=1*n+n//2
            m=next(i for i,o in enumerate(orbits) if o==(mid,))
            assert all((f&(1<<m)) or (f|(1<<m)) in faces for f in faces)
            assert betti_mod2(faces)==(0,)* (max(f.bit_count() for f in faces)+1)
        else:
            assert faces==even_model(n,orbits)
            b=betti_mod2(faces)
            assert b==(0,0,0,2*n-4), (n,b)
        count+=1
    print('PASS: exact invariant-face model, odd cone or even folded model,')
    print('and all mod-two reduced homology checks for 38 widths, 3 <= n <= 40.')
    print('This is a finite cross-check; all-width claims follow from the written proof.')
if __name__=='__main__': verify()
