#!/usr/bin/env python3
"""Reproduce crown-graph higher-independence homology and permutation traces.
Scientific reference: the bounded-component vertex-set complex of K_(n,n)-M.
Requires only Python 3 standard library; no external data.
"""
import argparse
import itertools
import json
import math
from collections import defaultdict


def induced_component_ok(n, mask):
    remaining=mask
    while remaining:
        root=remaining & -remaining
        seen=root
        frontier=root
        while frontier:
            next_frontier=0
            cur=frontier
            while cur:
                bit=cur & -cur
                cur-=bit
                v=bit.bit_length()-1
                if v<n:
                    neigh=((1<<n)-1) ^ (1<<v)
                    neigh <<= n
                else:
                    neigh=((1<<n)-1) ^ (1<<(v-n))
                next_frontier |= neigh & mask & ~seen
            seen|=next_frontier
            if seen.bit_count()>2:
                return False
            frontier=next_frontier
        remaining &= ~seen
    return True


def predicted(n,mask):
    a=mask&((1<<n)-1)
    b=(mask>>n)
    p,q=a.bit_count(),b.bit_count()
    if not p or not q:return True
    if p==q==1:return True
    if p==1 and q==2:return bool(a&b)
    if p==2 and q==1:return bool(a&b)
    if p==2 and q==2:return a==b
    return False


def ranks_mod2(face_by_dim):
    piv={}
    ranks={}
    for k in range(1,max(face_by_dim)+1):
        row_index={f:i for i,f in enumerate(face_by_dim[k-1])}
        piv={}
        for face in face_by_dim[k]:
            col=0
            bits=face
            while bits:
                bit=bits&-bits
                bits-=bit
                col ^=1<<row_index[face^bit]
            while col:
                i=col.bit_length()-1
                if i in piv: col^=piv[i]
                else:piv[i]=col;break
        ranks[k]=len(piv)
    betti={k:len(face_by_dim[k])-ranks.get(k,0)-ranks.get(k+1,0)-(k==0)
           for k in range(max(face_by_dim)+1)}
    return {k:v for k,v in betti.items() if v}


def permutation_image(v,n,sigma,swap):
    if not swap:
        return sigma[v] if v<n else n+sigma[v-n]
    return n+sigma[v] if v<n else sigma[v-n]


def fixed_face_sign(mask,n,sigma,swap):
    vertices=[j for j in range(2*n) if mask>>j&1]
    images=[permutation_image(j,n,sigma,swap) for j in vertices]
    if sum(1<<v for v in images)!=mask:return 0
    inv=sum(images[i]>images[j] for i in range(len(images)) for j in range(i+1,len(images)))
    return -1 if inv%2 else 1


def lef_trace(faces,n,sigma,swap):
    result=-1  # augmented degree minus one
    for mask in faces:
        if mask:
            sign=fixed_face_sign(mask,n,sigma,swap)
            result+=sign * (-1 if mask.bit_count()%2==0 else 1)
    return result


def predicted_trace(n,sigma,swap):
    f=sum(i==sigma[i] for i in range(n))
    f2=sum(i==sigma[sigma[i]] for i in range(n))
    x=((f-1)**2-(f2-1))//2
    return -x if swap else x


def check(n, full_characters):
    bydim=defaultdict(list)
    all_faces=[]
    mismatch=[]
    for mask in range(1<<(2*n)):
        a=induced_component_ok(n,mask)
        b=predicted(n,mask)
        if a!=b:mismatch.append(mask)
        if a:
            all_faces.append(mask)
            if mask:bydim[mask.bit_count()-1].append(mask)
    assert not mismatch, f'mismatched subsets: {mismatch[:10]}'
    # Facets must be the two colour classes plus the n-choose-2 four-vertex blocks
    facets=set()
    allset=set(all_faces)
    for f in all_faces:
        if not any((f|(1<<v)) in allset for v in range(2*n) if not(f>>v&1)):
            facets.add(f)
    expected={((1<<n)-1),((1<<n)-1)<<n}
    for i,j in itertools.combinations(range(n),2):
        expected.add((1<<i)|(1<<j)|(1<<(n+i))|(1<<(n+j)))
    assert facets==expected,(n,facets^expected)
    betti=ranks_mod2(bydim)
    want={2:math.comb(n-1,2)}
    assert betti==want,(n,betti)
    f_vector=[len(bydim[k]) for k in range(max(bydim)+1)]
    assert len(all_faces)==2*(2**n-1)+n*n+5*math.comb(n,2)+1
    reps=[]
    if full_characters:
        perms=list(itertools.permutations(range(n)))
    else:
        p0=tuple(range(n))
        perms=[p0, tuple((i+1)%n for i in range(n)),tuple(n-1-i for i in range(n))]
        for j in range(1,n):
            p=list(p0);p[0],p[j]=p[j],p[0];perms.append(tuple(p))
        perms=list(dict.fromkeys(perms))
    for perm in perms:
        for flip in (False,True):
            observed=lef_trace(all_faces,n,perm,flip)
            anticipated=predicted_trace(n,perm,flip)
            assert observed==anticipated,(n,perm,flip,observed,anticipated)
            reps.append((perm,flip))
    return {'n':n,'facets':len(facets),'nonempty_faces':len(all_faces)-1,
            'f_vector':f_vector,'reduced_mod2_betti':betti,
            'checked_automorphisms':len(reps),'trace_checks':'pass'}


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--max-n',type=int,default=8)
    args=parser.parse_args()
    for n in range(3,args.max_n+1):
        print(json.dumps(check(n,full_characters=(n<=6)),sort_keys=True))
    print('PASS: exact subset/facet enumeration, mod-two homology, and signed Lefschetz characters')

if __name__=='__main__':main()
