#!/usr/bin/env python3
"""Finite independent tests of stable-range higher independence topology of spider trees.
No third-party modules. Finite tests do not prove the all-parameter theorem.
"""
from itertools import product, permutations
from math import comb


def layout(lengths):
    arms=[];pos=1
    for length in lengths:
        arms.append(tuple(range(pos,pos+length)))
        pos+=length
    return arms,pos


def legal(mask, lengths, r):
    arms,size=layout(lengths)
    # Build induced components by DFS independently of proposed proof's face rule.
    adj=[[] for _ in range(size)]
    for arm in arms:
        previous=0
        for v in arm:
            adj[previous].append(v)
            adj[v].append(previous)
            previous=v
    found=set()
    for v in range(size):
        if not (mask>>v&1) or v in found:
            continue
        stack=[v];found.add(v);comp=0
        while stack:
            w=stack.pop();comp+=1
            for u in adj[w]:
                if mask>>u&1 and u not in found:
                    found.add(u);stack.append(u)
        if comp>r:return False
    return True


def faces(lengths,r):
    size=1+sum(lengths)
    return [mask for mask in range(1,1<<size) if legal(mask,lengths,r)]


def rank2(cols):
    pivots={}
    for c in cols:
        while c:
            k=c.bit_length()-1
            if k in pivots:c^=pivots[k]
            else:
                pivots[k]=c;break
    return len(pivots)


def betti(lengths,r):
    d={}
    for face in faces(lengths,r):
        d.setdefault(face.bit_count()-1,[]).append(face)
    ranks={}
    for k,fs in d.items():
        if k==0:
            ranks[k]=0;continue
        low={f:i for i,f in enumerate(d[k-1])}
        cols=[]
        for f in fs:
            c=0; v=f
            while v:
                one=v&-v;v^=one
                c^=1<<low[f^one]
            cols.append(c)
        ranks[k]=rank2(cols)
    out={k:len(fs)-ranks[k]-ranks.get(k+1,0)-(k==0) for k,fs in d.items()}
    return {k:v for k,v in out.items() if v}


def induced_vertex_perm(lengths,armperm):
    arms,size=layout(lengths)
    assert all(lengths[i]==lengths[armperm[i]] for i in range(len(arms)))
    v=[0]*size
    for i,arm in enumerate(arms):
        for j,k in enumerate(arm):v[k]=arms[armperm[i]][j]
    return v


def sign(p):
    return (-1)**sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))


def lefschetz(lengths,r,p):
    v=induced_vertex_perm(lengths,p)
    total=-1
    for f in faces(lengths,r):
        ids=[i for i in range(len(v)) if f>>i&1]
        im=[v[i] for i in ids]
        if set(im)!=set(ids):continue
        total+=(-1)**(len(ids)-1+sum(im[i]>im[j] for i in range(len(im)) for j in range(i+1,len(im))))
    return total


def expected_char(lengths,r,p):
    n=len(lengths)
    N=sum(x-1 for x in lengths)
    s=r-N-1
    if s<0 or s>=n:return 0
    # natural signed vertex-permutation on all nonterminal vertices
    v=induced_vertex_perm(lengths,p)
    interior=[v0 for arm in layout(lengths)[0] for v0 in arm[:-1]]
    images=[v[i] for i in interior]
    det=(-1)**sum(images[i]>images[j] for i in range(len(images)) for j in range(i+1,len(images)))
    # characteristic det(1+tP)/(1+t) of terminal augmentation lattice
    visited=set(); cycles=[]
    for i in range(n):
        if i not in visited:
            j=i;c=0
            while j not in visited:
                visited.add(j);c+=1;j=p[j]
            cycles.append(c)
    coeff=[1]+[0]*n
    for length in cycles:
        nxt=[0]*(n+1)
        for j,x in enumerate(coeff):
            nxt[j]+=x
            if j+length<=n:nxt[j+length]-=x*(-1)**length
        coeff=nxt
    h=0
    for j in range(s+1):h=coeff[j]-h
    return (-1)**(r-1)*det*h


def symmetry_perms(lengths):
    n=len(lengths)
    return [p for p in permutations(range(n)) if all(lengths[i]==lengths[p[i]] for i in range(n))]



def check_link_matching(lengths,r):
    # A second combinatorial test: direct Hasse-diagram acyclicity of the
    # paper's non-equivariant matching on the hub link, not just its homology.
    arms,total=layout(lengths)
    inner=[arm[:-1] for arm in arms]
    jmask=sum(1<<(v-1) for interior in inner for v in interior)
    leaves=[arm[-1]-1 for arm in arms]
    lf={f for f in range(1<<(total-1)) if legal((f<<1)|1,lengths,r)}
    paired={};top=[]
    t=r-(sum(l-1 for l in lengths))-1
    for f in sorted(lf):
        missing=next((i for i,intr in enumerate(inner)
                      if any(not (f>>(v-1)&1) for v in intr)),None)
        pivot=leaves[missing if missing is not None else 0]
        if f>>pivot&1:continue
        hi=f|(1<<pivot)
        if hi not in lf:continue
        if f==0:continue  # Reduced matching's one unmatched nonempty vertex.
        assert f not in paired and hi not in paired
        paired[f]=hi;paired[hi]=f
    leftover={f for f in lf if f and f not in paired}
    critical_leaf=1<<leaves[0]
    critical_top={f for f in leftover if f & jmask==jmask}
    assert leftover-{critical_leaf}==critical_top
    assert len(critical_top)==(comb(len(lengths)-1,t) if 0<=t<len(lengths) else 0)
    assert all(f.bit_count()==r-1 for f in critical_top)  # Link top face size r-1
    # Orient every cover relation downward except paired relations upward.
    adj={f:[] for f in lf if f}; indeg=dict.fromkeys(adj,0)
    for upper in adj:
        rem=upper
        while rem:
            one=rem&-rem;rem^=one
            lower=upper^one
            if lower==0 or lower not in adj:continue
            if paired.get(lower)==upper:
                adj[lower].append(upper);indeg[upper]+=1
            else:
                adj[upper].append(lower);indeg[lower]+=1
    q=[f for f in adj if indeg[f]==0];pos=0
    while pos<len(q):
        f=q[pos];pos+=1
        for g in adj[f]:
            indeg[g]-=1
            if indeg[g]==0:q.append(g)
    assert pos==len(adj), ('Morse cycle',lengths,r)


def run():
    cases=[]
    for n in range(3,5):
        for lengths in product((3,4,5),repeat=n):
            if sum(lengths)>12:continue
            r0=max(lengths)
            for r in range(r0,1+sum(lengths)+1):
                cases.append((lengths,r))
    bc=0;ch=0
    for lengths,r in cases:
        N=sum(a-1 for a in lengths);n=len(lengths);s=r-N-1
        goal=({r-1:comb(n-1,s)} if 0<=s<n else {})
        actual=betti(lengths,r)
        assert actual==goal,(lengths,r,actual,goal)
        bc+=1
        check_link_matching(lengths,r)
        for p in symmetry_perms(lengths):
            trace=lefschetz(lengths,r,p)
            expected=expected_char(lengths,r,p)
            assert trace==expected,(lengths,r,p,trace,expected)
            ch+=1
    print('PASS',bc,'mod-two Betti plus acyclic-Morse checks and',ch,'signed-Lefschetz checks, arms 3 to 5, 3-4 arms, at most 12 nonhub vertices')

if __name__=='__main__':run()
