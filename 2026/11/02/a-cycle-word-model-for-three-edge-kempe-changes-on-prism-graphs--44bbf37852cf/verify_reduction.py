"""Independent check of the cycle-word model of prism edge-Kempe moves."""
from itertools import product
from collections import Counter
from verify_direct import enumerate_colours, kempe_neighbours


def words(n):
    for mid in product((1, 2, 3), repeat=n-2):
        x=(1,)+mid+(2,)
        if all(x[i] != x[(i+1)%n] for i in range(n)):
            yield x


def canonical_edges(n):
    edges = tuple(sorted({tuple(sorted(e)) for i in range(n)
        for e in ((i,(i+1)%n), (i+n,(i+1)%n+n), (i,i+n))}))
    return edges


def edge_coloring(word, bottom):
    n=len(word); E=canonical_edges(n); out=[]
    for a,b in E:
        if a<n and b<n:
            # Top rim edge.
            i=a if (a+1)%n==b else b
            out.append(word[i])
        elif a>=n and b>=n:
            aa,bb=a-n,b-n
            i=aa if (aa+1)%n==bb else bb
            out.append(word[i] ^ bottom)
        else:
            i=a if a<n else b
            out.append(word[(i-1)%n]^word[i])
    return tuple(z-1 for z in out)


def type_two(n):
    if n%2: return None
    return tuple(1 if i%2==0 else 2 for i in range(n))


def cycle_word_moves(x):
    n=len(x); ans=set()
    for c in (1,2,3):
        seen=set()
        for i in range(n):
            if i in seen or x[i]==c: continue
            st=[i]; seen.add(i); comp=[]
            while st:
                v=st.pop();comp.append(v)
                for w in ((v-1)%n,(v+1)%n):
                    if w not in seen and x[w]!=c:
                        seen.add(w);st.append(w)
            if 0 in comp or n-1 in comp:continue
            y=list(x)
            for j in comp:y[j]^=c
            ans.add(tuple(y))
    return ans


def main():
    for n in range(3,13):
        E,inc,C=enumerate_colours(n)
        # Direct labeled coloring uses 0,1,2; binary-color map is +1.
        fixed={tuple((a,b)) for a,b in ((0,1),(0,2))} if False else None
        top=tuple(i for i,(a,b) in enumerate(E) if 0==a or 0==b)
        # edge index of (0,1) has binary-color 1, edge (0,n-1) binary-color 2, rung (0,n) binary-color 3.
        target={tuple(sorted((0,1))):0,tuple(sorted((0,n-1))):1,tuple(sorted((0,n))):2}
        specified={next(i for i,e in enumerate(E) if e==edge): c for edge,c in target.items()}
        direct={z for z in C if all(z[j]==v for j,v in specified.items())}
        encoded={edge_coloring(w,0): (w,0) for w in words(n)}
        q=type_two(n)
        if q is not None: encoded[edge_coloring(q,3)]=(q,3)
        assert set(encoded)==direct,(n,len(encoded),len(direct))
        for state,(w,bottom) in encoded.items():
            actual={z for z in kempe_neighbours(state,E,inc)[0] if z in encoded}
            if bottom==0:
                target={edge_coloring(y,0) for y in cycle_word_moves(w)}
                if q==w:target.add(edge_coloring(q,3))
            else:
                target={edge_coloring(q,0)}
            assert actual==target,(n,w,bottom,len(actual),len(target),actual^target)
        print(f'n={n} states={len(encoded)} fixed_cycle_reduction_ok')
    print('PRISM_CYCLE_REDUCTION_PASS')

if __name__=='__main__':main()
