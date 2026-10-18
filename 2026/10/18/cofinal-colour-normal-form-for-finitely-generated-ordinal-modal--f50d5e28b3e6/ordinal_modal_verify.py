"""Finite exact checker for cofinal-layer normal form on ordinal chains."""
from itertools import product

def layer_atoms(colors):
    right = len(colors)
    parts=[]
    while right:
        # On a finite successor initial segment, exactly the last color is cofinal.
        top_color = colors[right-1]
        nxt = max((i+1 for i in range(right) if colors[i] != top_color), default=0)
        for c in sorted(set(colors[nxt:right])):
            parts.append(sum(1 << i for i in range(nxt,right) if colors[i] == c))
        right = nxt
    return parts

def brute_size(colors, q):
    n=len(colors); universe=(1<<n)-1
    gens=[sum(1<<i for i,c in enumerate(colors) if c & (1<<j)) for j in range(q)]
    a=set([0,universe]+gens)
    while True:
        orig=len(a)
        old=list(a)
        for x in old:
            a.add(universe^x)
            if x:a.add((1<<x.bit_length())-1) # diamond under <=
            for y in old:a.add(x|y);a.add(x&y)
        if len(a)==orig:break
    return len(a)

def verify():
    tested=0
    for q, nmax in [(1,8),(2,5),(3,4)]:
        for n in range(1,nmax+1):
            for w in product(range(1<<q), repeat=n):
                atoms=layer_atoms(w)
                assert sum(atoms)==(1<<n)-1
                assert all(a & b==0 for i,a in enumerate(atoms) for b in atoms[i+1:])
                assert brute_size(w,q)==1<<len(atoms), (q,n,w,atoms)
                tested+=1
    print('ORDINAL_MODAL_COFINAL_LAYER_NORMAL_FORM_OK', tested)
if __name__=='__main__':verify()
