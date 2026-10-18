#!/usr/bin/env python3
"""Independent finite enumeration for a Rees zero-matrix semigroup theorem.

No third-party dependencies. All compositions and map domains are evaluated
from the finite multiplication table, independently of the structural proof.
"""
from itertools import permutations, product


def cyclic(n):
    return list(range(n)), lambda x,y:(x+y)%n, lambda x:(-x)%n, 0


def symmetric3():
    el=list(permutations(range(3))); e=(0,1,2)
    return el, lambda p,q:tuple(p[q[k]] for k in range(3)), lambda p:tuple(p.index(k) for k in range(3)),e


def check(name,group,mat):
    elems,op,inv,identity=group
    nlam=len(mat); ni=len(mat[0]); assert all(len(row)==ni for row in mat)
    zero='ZERO'; one='ONE'
    S=[zero]+[(i,g,l) for i in range(ni) for g in elems for l in range(nlam)]
    S1=S+[one]
    def mul(a,b):
        if a==one:return b
        if b==one:return a
        if a==zero or b==zero:return zero
        i,x,l=a; j,y,mu=b
        p=mat[l][j]
        if p is None:return zero
        return(i,op(op(x,p),y),mu)
    def map_gh(g,h):
        gh=mul(g,h)
        graph=[]
        for a in S:
            if mul(gh,a)==a==mul(a,gh):
                graph.append((a,mul(mul(h,a),g)))
        return frozenset(graph)
    actual={map_gh(g,h) for g in S1 for h in S1}
    trivial=frozenset({(zero,zero)})
    expected={trivial, frozenset({(a,a) for a in S})}
    edg=[(i,l) for i in range(ni) for l in range(nlam) if mat[l][i] is not None]
    def normal_src(i,l,a):return op(a,mat[l][i])
    def denormal_dest(j,mu,a):return op(a,inv(mat[mu][j]))
    for (i,l),(j,mu),conj in product(edg,edg,elems):
        graph={(zero,zero)}
        for a in elems:
            norm=normal_src(i,l,a)
            moved=op(op(inv(conj),norm),conj)
            graph.add(((i,a,l),(j,denormal_dest(j,mu,moved),mu)))
        expected.add(frozenset(graph))
    center=[z for z in elems if all(op(z,g)==op(g,z) for g in elems)]
    if not edg:
        formula=2
    elif ni*nlam>1:
        formula=len(edg)**2 * len(elems)//len(center)+2
    else:
        formula=len(elems)//len(center)+1
    if actual!=expected or len(actual)!=formula:
        raise AssertionError((name,len(actual),len(expected),formula,
               'missing expected',list(expected-actual)[:1],
               'extra actual',list(actual-expected)[:1]))
    # Extra independent check: the raw maps are closed under composition.
    # For our finite examples, include every pair only while sets stay small.
    if len(actual)<110:
        for f,g in product(actual,repeat=2):
            gd=dict(g)
            comp=frozenset((x,gd[y]) for x,y in f if y in gd)
            assert comp in actual,(name,'not closed')
    print(name,'OK','underlying_elements',len(S),'nonzero_idempotents',len(edg),
          'center_order',len(center),'partial_inner_maps',len(actual))


def main():
    c2=cyclic(2); c3=cyclic(3); s3=symmetric3()
    e2=c2[-1]; e3=c3[-1]; es=s3[-1]
    check('trivial_zero_group',cyclic(1),[[0]])
    check('group_with_zero_C3',c3,[[0]])
    check('Brandt_C2_two_indices',c2,[[0,None],[None,0]])
    check('Brandt_S3_three_indices',s3,[[es,None,None],[None,es,None],[None,None,es]])
    check('full_C3_two_by_two',c3,[[0,1],[2,0]])
    check('full_S3_two_by_two',s3,[[es,s3[0][1]],[s3[0][2],es]])
    check('sparse_rectangular_C2',c2,[[0,1,None],[None,1,0]])
    check('dense_rectangular_C2',c2,[[0,1,0],[None,1,None]])
    check('nonuniform_2_by_3_S3',s3,[[es,s3[0][1],None],[None,s3[0][2],es]])
    check('nonregular_with_zero_rows_C3',c3,[[0,None,None],[None,None,None]])
    check('nonregular_with_zero_columns_S3',s3,[[es,None],[None,None]])
    check('all_zero_sandwich_C2',c2,[[None,None],[None,None]])
    # The two support patterns have equal numbers of nonzero sandwich cells,
    # but opposite complete-mapping answers (by exhaustive permutation scan).
    def complete_mappings(P):
        entries=[None]+[(i,l) for i in range(3) for l in range(2)]
        def operation(x,y):
            if x is None or y is None:return None
            i,l=x; j,mu=y
            return (i,mu) if P[l][j] else None
        return sum(len({operation(x,y) for x,y in zip(entries,alpha)})==len(entries)
                   for alpha in permutations(entries))
    PA=[[1,1,1],[1,0,0]]
    PB=[[1,1,0],[0,1,1]]
    assert complete_mappings(PA)==0
    assert complete_mappings(PB)==24
    check('profile_A_trivial_group',cyclic(1),[[0,0,0],[0,None,None]])
    check('profile_B_trivial_group',cyclic(1),[[0,0,None],[None,0,0]])
    print('Complete mapping counts: A=0, B=24.')
    print('ALL CHECKS PASSED')
if __name__=='__main__':main()
