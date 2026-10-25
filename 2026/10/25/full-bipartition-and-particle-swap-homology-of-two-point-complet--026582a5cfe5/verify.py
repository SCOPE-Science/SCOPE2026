"""Exact finite checks for two-point configurations on complete bipartite graphs.

Uses only the Python standard library. A finite check corroborates, but does not
replace, the general homological and representation-theoretic argument.
"""
from itertools import product


def partitions(n, maximum=None):
    if n == 0:
        yield ()
        return
    for j in range(min(maximum or n, n), 0, -1):
        for rest in partitions(n-j, j):
            yield (j,) + rest


def cycle_type_rep(partition):
    out = []
    offset = 0
    for k in partition:
        out.extend(offset + (i+1)%k for i in range(k))
        offset += k
    return out


def gf2_rank(columns):
    basis = {}
    for v in columns:
        while v:
            pivot = v.bit_length()-1
            if pivot in basis:
                v ^= basis[pivot]
            else:
                basis[pivot] = v
                break
    return len(basis)


def cells(p,q):
    vertices = list(range(p+q))
    edges = [(a,p+b) for a in range(p) for b in range(q)]
    c0 = [(a,b) for a in vertices for b in vertices if a != b]
    c1 = [("e",i,v) for i,e in enumerate(edges) for v in vertices if v not in e]
    c1 += [("v",v,i) for v in vertices for i,e in enumerate(edges) if v not in e]
    c2 = [(i,j) for i,e in enumerate(edges) for j,f in enumerate(edges) if not (set(e)&set(f))]
    return edges,c0,c1,c2


def ranks(p,q):
    edges,c0,c1,c2 = cells(p,q)
    idx0={c:i for i,c in enumerate(c0)}
    idx1={c:i for i,c in enumerate(c1)}
    b1cols=[]
    for tag,a,b in c1:
        e = edges[a] if tag=='e' else edges[b]
        v = b if tag=='e' else a
        c = (e[0],v) if tag=='e' else (v,e[0])
        d = (e[1],v) if tag=='e' else (v,e[1])
        b1cols.append((1<<idx0[c])^(1<<idx0[d]))
    b2cols=[]
    for i,j in c2:
        a,b=edges[i];c,d=edges[j]
        boundary=[('v',a,j),('v',b,j),('e',i,c),('e',i,d)]
        z=0
        for x in boundary:
            z^=1<<idx1[x]
        b2cols.append(z)
    r1=gf2_rank(b1cols)
    r2=gf2_rank(b2cols)
    assert r1==len(c0)-1,(p,q,"disconnected")
    b2=len(c2)-r2
    b1=len(c1)-r1-r2
    B=(p-1)*(q-1)
    pred_b2=B*B-B+1-p*(q-1)*(q-2)-q*(p-1)*(p-2)
    assert (b1,b2)==(2*B,pred_b2),(p,q,b1,b2,pred_b2)
    return len(c0),len(c1),len(c2),r1,r2,b1,b2


def count_two_cycles(g):
    return sum(1 for i,j in enumerate(g) if j>i and g[j]==i)


def trace_chains(p,q,perm_a,perm_b,swap):
    edges,c0,c1,c2=cells(p,q)
    vertex_map={a:perm_a[a] for a in range(p)}
    vertex_map.update({p+b:p+perm_b[b] for b in range(q)})
    edge_index={e:i for i,e in enumerate(edges)}
    edge_map=[edge_index[(vertex_map[a],vertex_map[b])] for a,b in edges]
    if swap:
        tr0=sum(vertex_map[b]==a and vertex_map[a]==b for a,b in c0)
        tr1=0
        tr2=-sum(edge_map[j]==i and edge_map[i]==j for i,j in c2)
    else:
        tr0=sum(vertex_map[a]==a and vertex_map[b]==b for a,b in c0)
        tr1=sum(vertex_map[b]==b and edge_map[a]==a if tag=='e'
                else vertex_map[a]==a and edge_map[b]==b for tag,a,b in c1)
        tr2=sum(edge_map[i]==i and edge_map[j]==j for i,j in c2)
    return tr0,tr1,tr2


def trace_test(p,q):
    cases=0
    for part_a,part_b in product(partitions(p),partitions(q)):
        a=cycle_type_rep(part_a); b=cycle_type_rep(part_b)
        fixed_a=sum(i==j for i,j in enumerate(a))
        fixed_b=sum(i==j for i,j in enumerate(b))
        two_a=count_two_cycles(a); two_b=count_two_cycles(b)
        for swap in (False,True):
            c0,c1,c2=trace_chains(p,q,a,b,swap)
            h1=(0 if swap else 2*(fixed_a-1)*(fixed_b-1))
            h2=c0-c1+c2-1+h1
            pred=-(2*two_a-1)*(2*two_b-1) if swap else (fixed_a**2-3*fixed_a+1)*(fixed_b**2-3*fixed_b+1)
            assert h2==pred,(p,q,part_a,part_b,swap,h2,pred)
            # Independent irreducible-character identity for the four summands.
            def w_s(f,t):
                w=(f*f-3*f+2)//2-t
                s=(f*f-3*f)//2+t
                return w,s
            wa,sa=w_s(fixed_a,two_a);wb,sb=w_s(fixed_b,two_b)
            assert h2==(wa+sa)*(wb+sb) if not swap else h2==-(sa-wa)*(sb-wb)
            cases+=1
    return cases



def odd_prime_rank(columns, prime=101):
    """Sparse column elimination over a field of odd characteristic."""
    basis = {}
    for raw in columns:
        col = {i: a % prime for i,a in raw.items() if a % prime}
        while col:
            pivot = max(col)
            if pivot not in basis:
                inv = pow(col[pivot], -1, prime)
                basis[pivot] = {i:(a*inv)%prime for i,a in col.items()}
                break
            multiplier = col[pivot]
            for i,a in basis[pivot].items():
                b = (col.get(i,0)-multiplier*a)%prime
                if b: col[i]=b
                elif i in col: del col[i]
    return len(basis)


def particle_swap_eigenspace_test(p,q):
    edges,c0,c1,c2=cells(p,q)
    idx1={c:i for i,c in enumerate(c1)}
    c2set=set(c2)
    assert all((j,i) in c2set for i,j in c2)
    def boundary(i,j):
        a,b=edges[i];c,d=edges[j]
        return {idx1[('v',b,j)]:1, idx1[('v',a,j)]:-1,
                idx1[('e',i,c)]:1, idx1[('e',i,d)]:-1}
    representatives=[(i,j) for i,j in c2 if i<j]
    eigens={}
    for sign in (1,-1):
        cols=[]
        for i,j in representatives:
            # swap(e_i x e_j)=-e_j x e_i: sign eigenspace uses v_+=a-b.
            x=boundary(i,j); y=boundary(j,i)
            for index,value in y.items():
                x[index]=x.get(index,0)-sign*value
            cols.append(x)
        r=odd_prime_rank(cols)
        eigens[sign]=len(cols)-r
    b2=ranks(p,q)[-1]
    assert eigens=={1:(b2-1)//2, -1:(b2+1)//2},(p,q,eigens,b2)
    return eigens


def main():
    tested=0
    for p,q in [(3,3),(3,4),(3,5),(3,6),(4,4),(4,5),(4,6),(5,5),(5,6),(6,6)]:
        r=ranks(p,q)
        print('DIMENSIONS',p,q,'cells',r[:3],'ranks',r[3:5],'Betti',r[5:])
        tested+=trace_test(p,q)
        if p<=5 and q<=5:
            print('SWAP_EIGENSPACES',p,q,particle_swap_eigenspace_test(p,q))
    print('COMPLETE_BIPARTITE_TWO_POINT_CHARACTERS_VERIFIED',tested)

if __name__=='__main__':
    main()
