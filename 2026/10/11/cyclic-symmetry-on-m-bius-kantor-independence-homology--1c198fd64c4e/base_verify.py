#!/usr/bin/env python3
from collections import Counter, defaultdict, deque
from functools import lru_cache

N = 16
ORDER = [0,8,1,9,2,10,3,11,4,12,5,13,6,14,7,15]
PRIMES = [2,3,5]


def graph_edges():
    E=set()
    n=8; k=3
    for i in range(n):
        E.add(tuple(sorted((i,(i+1)%n))))
        E.add(tuple(sorted((i,n+i))))
        E.add(tuple(sorted((n+i,n+((i+k)%n)))))
    return sorted(E)


def adjacency_masks(E):
    adj=[0]*N
    for a,b in E:
        adj[a] |= 1<<b
        adj[b] |= 1<<a
    return adj


def enumerate_independent_faces(adj):
    faces=[0]
    for m in range(1,1<<N):
        x=m
        ok=True
        while x:
            lsb=x & -x
            v=lsb.bit_length()-1
            x ^= lsb
            if adj[v] & x:
                ok=False
                break
        if ok:
            faces.append(m)
    return faces


def toggle_matching(nonempty_faces):
    unmatched=set(nonempty_faces)
    pairs=[]
    for v in ORDER:
        bit=1<<v
        for low in sorted(m for m in unmatched if not (m & bit)):
            up=low|bit
            if up in unmatched:
                unmatched.remove(low)
                unmatched.remove(up)
                pairs.append((low,up))
    return pairs, unmatched


def hasse_covers(face_set):
    covers=[]
    for up in sorted(face_set):
        verts=[v for v in range(N) if (up>>v)&1]
        if len(verts)<=1:
            continue
        for v in verts:
            low=up & ~(1<<v)
            if low in face_set:
                covers.append((low,up))
    return covers


def verify_acyclic(face_set,pairs,covers):
    pairset=set(pairs)
    out=defaultdict(list)
    indeg={m:0 for m in face_set}
    for low,up in covers:
        if (low,up) in pairset:
            a,b=low,up
        else:
            a,b=up,low
        out[a].append(b)
        indeg[b]+=1
    q=deque(sorted(m for m,d in indeg.items() if d==0))
    seen=0
    while q:
        a=q.popleft(); seen+=1
        for b in out[a]:
            indeg[b]-=1
            if indeg[b]==0:
                q.append(b)
    return seen==len(face_set), seen


def incidence(face,simplex):
    verts=[v for v in range(N) if (simplex>>v)&1]
    missing=[v for v in verts if not ((face>>v)&1)]
    assert len(missing)==1
    pos=verts.index(missing[0])
    return 1 if pos%2==0 else -1


def exact_morse_boundary_4_to_3(pairs,crit):
    lower_to_upper={a:b for a,b in pairs}
    upper_to_lower={b:a for a,b in pairs}
    crit3=sorted(m for m in crit if m.bit_count()-1==3)
    crit4=sorted(m for m in crit if m.bit_count()-1==4)
    assert len(crit3)==4 and len(crit4)==1
    index={m:i for i,m in enumerate(crit3)}
    visiting=set()

    @lru_cache(None)
    def proj3(sigma):
        if sigma in index:
            vec=[0]*len(crit3); vec[index[sigma]]=1
            return tuple(vec)
        if sigma in upper_to_lower:
            return (0,)*len(crit3)
        tau=lower_to_upper.get(sigma)
        assert tau is not None
        assert sigma not in visiting
        visiting.add(sigma)
        eps=incidence(sigma,tau)
        out=[0]*len(crit3)
        for v in range(N):
            if (tau>>v)&1:
                f=tau & ~(1<<v)
                if f==sigma:
                    continue
                e=incidence(f,tau)
                pv=proj3(f)
                for j,x in enumerate(pv):
                    out[j] += -eps*e*x
        visiting.remove(sigma)
        return tuple(out)

    alpha=crit4[0]
    bd=[0]*len(crit3)
    for v in range(N):
        if (alpha>>v)&1:
            f=alpha & ~(1<<v)
            e=incidence(f,alpha)
            pv=proj3(f)
            for j,x in enumerate(pv):
                bd[j]+=e*x
    return crit3,alpha,bd


def boundary_rank_modp(cols,rows,p):
    ridx={m:i for i,m in enumerate(rows)}
    A=[[0]*len(cols) for _ in range(len(rows))]
    for j,m in enumerate(cols):
        verts=[v for v in range(N) if (m>>v)&1]
        for pos,v in enumerate(verts):
            f=m & ~(1<<v)
            if f in ridx:
                A[ridx[f]][j]=(1 if pos%2==0 else -1)%p
    r=0
    nrow=len(A); ncol=len(cols)
    for c in range(ncol):
        pivot=None
        for i in range(r,nrow):
            if A[i][c]%p:
                pivot=i; break
        if pivot is None:
            continue
        A[r],A[pivot]=A[pivot],A[r]
        inv=pow(A[r][c]%p,-1,p)
        A[r]=[(x*inv)%p for x in A[r]]
        for i in range(nrow):
            if i!=r and A[i][c]%p:
                factor=A[i][c]%p
                A[i]=[(x-factor*y)%p for x,y in zip(A[i],A[r])]
        r+=1
        if r==nrow:
            break
    return r


def full_betti(faces,p):
    bydim=defaultdict(list)
    for m in faces:
        if m:
            bydim[m.bit_count()-1].append(m)
    top=max(bydim)
    ranks={}
    for d in range(1,top+1):
        ranks[d]=boundary_rank_modp(sorted(bydim[d]),sorted(bydim[d-1]),p)
    betti={0:len(bydim[0])-ranks.get(1,0)}
    for d in range(1,top):
        betti[d]=len(bydim[d])-ranks[d]-ranks.get(d+1,0)
    betti[top]=len(bydim[top])-ranks[top]
    return [betti[d] for d in range(top+1)]


def main():
    E=graph_edges()
    assert len(E)==24
    deg=Counter()
    for a,b in E:
        deg[a]+=1;deg[b]+=1
    assert all(deg[v]==3 for v in range(N))
    adj=adjacency_masks(E)
    faces=enumerate_independent_faces(adj)
    nonempty=[m for m in faces if m]
    fv=Counter(m.bit_count()-1 for m in nonempty)
    expected_fv={0:16,1:96,2:272,3:376,4:240,5:72,6:16,7:2}
    assert dict(sorted(fv.items()))==expected_fv

    pairs,crit=toggle_matching(nonempty)
    assert len(pairs)==542
    cvec=Counter(m.bit_count()-1 for m in crit)
    assert dict(sorted(cvec.items()))=={0:1,3:4,4:1}
    used=set()
    for low,up in pairs:
        assert low in nonempty and up in nonempty
        assert low.bit_count()+1==up.bit_count()
        assert (low & up)==low
        assert low not in used and up not in used
        used.add(low);used.add(up)
    assert used.isdisjoint(crit)
    assert len(used)+len(crit)==len(nonempty)

    face_set=set(nonempty)
    covers=hasse_covers(face_set)
    assert len(covers)==4272
    acyclic,seen=verify_acyclic(face_set,pairs,covers)
    assert acyclic and seen==len(face_set)

    crit3,crit4,bd=exact_morse_boundary_4_to_3(pairs,crit)
    assert bd==[0,0,0,0]

    bettis={p:full_betti(faces,p) for p in PRIMES}
    for p,b in bettis.items():
        assert b==[1,0,0,4,1,0,0,0]

    print('VERIFY_OK')
    print('graph: generalized Petersen G(8,3), vertices=16, edges=24, cubic')
    print('nonempty_faces:',len(nonempty))
    print('face_vector:',[expected_fv[d] for d in range(8)])
    print('hasse_covers:',len(covers))
    print('matching_pairs:',len(pairs))
    print('critical_counts:',dict(sorted(cvec.items())))
    print('critical_3_masks:',crit3)
    print('critical_4_mask:',crit4)
    print('morse_boundary_d4_to_d3:',bd)
    for p in PRIMES:
        print(f'betti_mod_{p}:',bettis[p])
    print('homotopy_conclusion: wedge of four S^3 and one S^4')

if __name__=='__main__':
    main()
