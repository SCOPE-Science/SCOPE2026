"""Exact finite checks for inball of symmetric edge polytopes of dense graphs.

Pure Python 3 standard library; independent enumeration of integer Lipschitz
potentials for complements of all unlabeled disjoint path/cycle unions up to 11.
"""
from itertools import product


def component_catalog(n):
    return [('P', k) for k in range(1, n+1)] + [('C', k) for k in range(3, n+1)]


def families(n):
    catalog=component_catalog(n)
    out=[]
    def rec(min_index, remaining, chosen):
        if remaining==0:
            edges=set()
            offset=0
            for typ,k in chosen:
                if typ=='P':
                    edges.update((offset+i,offset+i+1) for i in range(k-1))
                else:
                    edges.update((offset+i,offset+(i+1)%k) for i in range(k))
                offset+=k
            assert offset==n
            if max([0]+[sum(v in e for e in edges) for v in range(n)])==2:
                out.append((tuple(chosen),frozenset(frozenset(e) for e in edges)))
            return
        for j in range(min_index,len(catalog)):
            typ,k=catalog[j]
            if k<=remaining:
                rec(j,remaining-k,chosen+[(typ,k)])
    rec(0,n,[])
    return out


def predicted_score(n,H):
    # n * (maximum squared Euclidean norm in the polar)
    has_c4=any(all(frozenset((x,y)) in H for x in A for y in B)
               for A in __import__('itertools').combinations(range(n),2)
               for B in __import__('itertools').combinations([j for j in range(n) if j not in A],2))
    return max((n//2)*(n-n//2), (4*n if has_c4 else 3*n-1)),has_c4


def enumerate_potentials(n,G):
    # The polar is an integral difference-constraint polytope, so the
    # optimum is attained at integral potentials. Diameter(G)<=2.
    best=-1
    winners=[]
    for f in product((0,1,2),repeat=n):
        if 0 not in f:
            continue
        if any(abs(f[u]-f[v])>1 for u,v in G):
            continue
        score=n*sum(x*x for x in f)-sum(f)**2
        if score>best:
            best=score
            winners=[f]
        elif score==best:
            winners.append(f)
    return best,winners


def verify():
    profiles=0
    c4prof=0
    for n in range(5,12):
        for desc,H in families(n):
            G=[(i,j) for i in range(n) for j in range(i+1,n)
               if frozenset((i,j)) not in H]
            # Each missing edge has a two-step replacement.
            for ij in H:
                a,b=tuple(ij)
                assert any((min(a,z),max(a,z)) in G and (min(b,z),max(b,z)) in G
                           for z in range(n) if z not in ij)
            expected,c4=predicted_score(n,H)
            observed,winners=enumerate_potentials(n,G)
            assert observed==expected,(n,desc,observed,expected)
            if c4:
                component_c4=sum(typ=='C' and k==4 for typ,k in desc)
                expected_contacts=2*component_c4
            else:
                expected_contacts=2*sum(sum(v in e for e in H)==2 for v in range(n))
            assert len(winners)==expected_contacts,(n,desc,len(winners),expected_contacts)
            profiles+=1
            c4prof+=int(c4)
    for n in range(5,60):
        u=(n//2)*(n-n//2)
        assert (u>=3*n-1)==(n>=12)
        assert (u>=4*n)==(n>=16)
    print('VERIFY_OK max-degree-two dense-edge-polytope inradii',
          'component-profiles=',profiles,'with-C4=',c4prof,
          'n=5..11; thresholds-checked=5..59; exact-polar=yes')

if __name__=='__main__':
    verify()
