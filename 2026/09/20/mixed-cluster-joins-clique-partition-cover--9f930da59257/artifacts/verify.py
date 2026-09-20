from math import comb, ceil


def make_graph(p,q,h,l,r):
    A=[]; B=[]; nxt=0
    for i in range(h):
        cl=list(range(nxt,nxt+p)); nxt += p; A.append(cl)
    for j in range(l):
        sz=q+1 if j<r else q
        cl=list(range(nxt,nxt+sz)); nxt += sz; B.append(cl)
    E=set()
    for cl in A+B:
        for x in range(len(cl)):
            for y in range(x+1,len(cl)):
                E.add(tuple(sorted((cl[x],cl[y]))))
    for ca in A:
        for cb in B:
            for u in ca:
                for v in cb:
                    E.add((u,v) if u<v else (v,u))
    return A,B,E


def internal_edges(cl):
    return [tuple(sorted((cl[i],cl[j]))) for i in range(len(cl)) for j in range(i+1,len(cl))]


def edge_set_of_clique(vertices):
    return {tuple(sorted((vertices[i],vertices[j]))) for i in range(len(vertices)) for j in range(i+1,len(vertices))}


def verify_case(p,q,h,l,r):
    dp=comb(p,2); dq=comb(q,2)
    a=h*dp
    assert dp <= l
    assert ceil(a/l) <= dq
    assert comb(q+1,2) <= h
    assert 0 <= r <= l

    A,B,E=make_graph(p,q,h,l,r)
    Aedges=[internal_edges(cl) for cl in A]
    Bedges=[internal_edges(cl) for cl in B]

    # Assign every A-internal edge to a distinct B-cluster within its A-row,
    # with globally balanced B loads. Flattening the A-edge positions and
    # reducing modulo l has both properties because dp <= l.
    assigned=[[] for _ in range(l)]
    used_pair=set()
    for i in range(h):
        for u,eA in enumerate(Aedges[i]):
            j=(i*dp+u)%l
            assert (i,j) not in used_pair
            used_pair.add((i,j))
            assigned[j].append((i,eA))
    loads=[len(x) for x in assigned]
    assert max(loads, default=0) <= ceil(a/l) <= dq

    parts=[]
    # Pair assigned A edges with distinct B-internal edges to make K4s.
    used_B=[set() for _ in range(l)]
    for j,items in enumerate(assigned):
        for idx,(i,eA) in enumerate(items):
            eB=Bedges[j][idx]
            used_B[j].add(eB)
            Q=tuple(eA+eB)
            assert len(set(Q))==4
            parts.append(Q)

    # Each remaining B-internal edge gets a triangle in a previously unused
    # A_i--B_j cluster pair. The size hypothesis guarantees enough such pairs.
    for j in range(l):
        remaining=[e for e in Bedges[j] if e not in used_B[j]]
        free_i=[i for i in range(h) if (i,j) not in used_pair]
        assert len(remaining) <= len(free_i)
        for eB,i in zip(remaining,free_i):
            parts.append(tuple(eB)+(A[i][0],))
            used_pair.add((i,j))

    covered=set()
    for Q in parts:
        QE=edge_set_of_clique(Q)
        assert QE <= E
        assert covered.isdisjoint(QE)
        covered |= QE

    # Remaining edges are 2-cliques.
    for e in sorted(E-covered):
        parts.append(e)
        covered.add(e)
    assert covered==E

    # Recheck that every listed part is a clique and that edge sets partition E.
    chk=set()
    for Q in parts:
        QE=edge_set_of_clique(Q)
        assert QE <= E and chk.isdisjoint(QE)
        chk |= QE
    assert chk==E

    b=l*dq+r*q
    s=(h*p)*(l*q+r)
    expected=s-2*a-b
    assert len(parts)==expected, (p,q,h,l,r,len(parts),expected)
    assert a <= b
    return len(E), expected, h*l


def main():
    cases=0
    # A varied finite box of admissible parameters, including unequal p,q
    # and mixed q/q+1 clusters on the B side.
    for p in range(2,7):
        for q in range(max(2,p),8):
            dp=comb(p,2); dq=comb(q,2)
            h0=comb(q+1,2)
            for h in range(h0,h0+3):
                for l in range(max(dp, (h*dp + dq - 1)//dq), max(dp, (h*dp + dq - 1)//dq)+4):
                    if ceil(h*dp/l)>dq:
                        continue
                    for r in sorted(set([0, min(1,l), min(q-1,l), l])):
                        verify_case(p,q,h,l,r)
                        cases += 1
    print(f"verified {cases} admissible mixed-cluster parameter tuples")
    print("all constructed clique families are exact edge partitions with the stated cardinality")

if __name__=='__main__':
    main()
