"""An independent isomorphism and automorphism identity for exact p-morphism counts."""
from itertools import permutations
from count_pmorphisms_dp import trees_up_to,parent_from_shape,count_bounded_surjections

def graph_iso_number(p,q):
    n=len(p)
    if len(q)!=n:return 0
    # A rooted-tree isomorphism is a root-preserving bijection respecting parent arcs.
    tot=0
    for rest in permutations(range(1,n)):
        im=(0,)+rest
        if all(im[p[i]]==q[im[i]] for i in range(1,n)):
            tot+=1
    return tot

if __name__=='__main__':
    bysize=trees_up_to(7)
    tests=0;aut=0
    for n in range(1,8):
        for pshape in bysize[n]:
            p=parent_from_shape(pshape)
            for qshape in bysize[n]:
                q=parent_from_shape(qshape)
                got=count_bounded_surjections(p,q)
                expected=graph_iso_number(p,q)
                if got!=expected:raise AssertionError((p,q,got,expected))
                tests+=1
                if got:aut+=1
    print('EQUAL_SIZE_BOUNDED_MAPS_ARE_ROOTED_ISOMORPHISMS',tests,'PAIRS',aut,'POSITIVE')
