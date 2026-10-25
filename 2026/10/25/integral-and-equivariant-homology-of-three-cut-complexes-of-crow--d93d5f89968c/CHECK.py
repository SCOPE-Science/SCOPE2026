#!/usr/bin/env python3
"""Finite reproducibility checks for crown-graph three-cut complexes.

All tests use exact integer combinatorics. The all-parameter homology proof
uses the published shellability theorem and combinatorial Alexander duality;
finite tests below are explicitly not a proof for every parameter.
"""
from itertools import combinations
from math import comb


def parts(total, least=1):
    if total == 0:
        yield ()
    for k in range(least, total + 1):
        for p in parts(total-k, k):
            yield (k,) + p


def permutation(partition):
    p = list(range(sum(partition)))
    j = 0
    for k in partition:
        for t in range(k):
            p[j+t] = j+(t+1)%k
        j += k
    return p


def sign_on_face(face, g):
    pos = {v:i for i,v in enumerate(face)}
    arr = [pos[g[v]] for v in face]
    return -1 if sum(arr[i] > arr[j] for i in range(len(arr))
                     for j in range(i+1,len(arr)))%2 else 1


def signed_face_sum(faces, g):
    # Sum of (-1) to face size, including the empty face.
    return sum((-1)**len(f) * sign_on_face(f,g)
               for f in faces if all(g[v] in f for v in f))


def crown_connected_triples(n):
    out = set()
    for triple in combinations(range(2*n),3):
        a = [v for v in triple if v<n]
        b = [v-n for v in triple if v>=n]
        if (len(a)==2 and len(b)==1 and b[0] not in a) or (
                len(a)==1 and len(b)==2 and a[0] not in b):
            out.add(triple)
    return out


def complexes(n):
    connected = crown_connected_triples(n)
    all_triples = set(combinations(range(2*n),3))
    disconnected = all_triples-connected
    bfaces = []
    lfaces = []
    xfaces = []
    for mask in range(1<<(2*n)):
        face = tuple(v for v in range(2*n) if mask>>v&1)
        a = {v for v in face if v<n}
        b = {v-n for v in face if v>=n}
        in_b = len(a)<=2 and len(b)<=2 and not a.intersection(b)
        if in_b:
            bfaces.append(face)
        # The actual Alexander dual is the complex avoiding a disconnected triple.
        in_l = not any(set(triple).issubset(face) for triple in disconnected)
        if in_l:
            lfaces.append(face)
        if in_l != (in_b or (len(face)==2 and any(face==(i,n+i) for i in range(n)))):
            raise AssertionError('Alexander-dual decomposition mismatch')
        in_x = any(not set(triple).intersection(face) for triple in disconnected)
        if in_x:
            xfaces.append(face)
    return bfaces,lfaces,xfaces


def predicted(n, partition, flip):
    c1=partition.count(1); c2=partition.count(2); c4=partition.count(4)
    C=lambda a,k:comb(a,k) if a>=k else 0
    P = 1-c1+C(c1,2)
    Q = 1-2*c1+4*C(c1,2)-6*C(c1,3)+6*C(c1,4)
    t0 = Q - 2*c2*P + c2*(c2-1)
    t1 = 1-2*c2+4*C(c2,2)-2*c4
    low = (-1)**(n*flip) * (t0 if not flip else t1)
    high = (-1)**((n+1)*flip)*c1
    return low,high,t0 if not flip else t1


def rank_mod(columns,nrows,p):
    # Sparse column rank, with each column represented by row-index -> integer.
    pivots={}
    for col in columns:
        v={r:(x%p) for r,x in col.items() if x%p}
        while v:
            row=min(v)
            if row not in pivots:
                factor=pow(v[row],-1,p)
                pivots[row]={r:x*factor%p for r,x in v.items() if x}
                break
            fac=v[row]
            for r,x in pivots[row].items():
                z=(v.get(r,0)-fac*x)%p
                if z:v[r]=z
                elif r in v:del v[r]
    return len(pivots)


def dimensions_and_homology(faces,p):
    nonempty=[f for f in faces if f]
    dims={d:sorted(f for f in nonempty if len(f)==d+1)
          for d in range(max(map(len,nonempty)))}
    ranks={0:0}
    for d in sorted(dims):
        if d==0:continue
        row={f:i for i,f in enumerate(dims[d-1])}
        columns=[]
        for face in dims[d]:
            columns.append({row[face[:i]+face[i+1:]]:(-1)**i
                            for i in range(len(face))})
        ranks[d]=rank_mod(columns,len(row),p)
    out={d:len(faces_d)-ranks[d]-ranks.get(d+1,0)
         for d,faces_d in dims.items()}
    out[0]-=1 # reduced H_0 for connected nonempty complexes
    return {d:r for d,r in out.items() if r}, {d:len(x) for d,x in dims.items()}


def main():
    for n in range(5,8):
        bfaces,lfaces,xfaces=complexes(n)
        b = 1+n*(n-2)*(n-3)*(n-5)//4
        facevec={j:sum(len(face)==j+1 for face in bfaces) for j in range(4)}
        assert facevec == {0:2*n,1:2*n*(n-1),
                           2:n*(n-1)*(n-2),3:comb(n,2)*comb(n-2,2)}
        for p in (101,103):
            hb,_=dimensions_and_homology(bfaces,p)
            hl,_=dimensions_and_homology(lfaces,p)
            assert hb == ({3:b} if b else {}), ('B',n,p,hb,b)
            assert hl == {1:n,3:b}, ('L',n,p,hl,b)
        for partition in parts(n):
            sp=permutation(partition)
            for flip in (0,1):
                g=[sp[i]+n*flip for i in range(n)]+[
                   sp[i]+n*(1-flip) for i in range(n)]
                lo,hi,bchar=predicted(n,partition,flip)
                assert signed_face_sum(bfaces,g)==bchar, ('B action',n,partition,flip)
                assert -signed_face_sum(xfaces,g)==lo+hi, ('X action',n,partition,flip)
        print('PASS',n,'b',b,'X faces',len(xfaces),'all conjugacy characters checked')
    print('CHECK_OK finite tests; parameter-uniform proof is mathematical.')

if __name__=='__main__':main()
