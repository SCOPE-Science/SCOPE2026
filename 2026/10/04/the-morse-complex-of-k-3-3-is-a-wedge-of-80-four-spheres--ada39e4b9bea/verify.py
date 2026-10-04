#!/usr/bin/env python3
from itertools import product
from collections import defaultdict, Counter, deque
import hashlib, json

# K_{3,3}: left vertices 0,1,2; right vertices 3,4,5.
EDGES=[(i,3+j) for i in range(3) for j in range(3)]
NPRIM=18


def acyclic_arrows(arrows):
    out={u:v for u,v in arrows}
    done=set()
    for s in list(out):
        x=s; local=set()
        while x in out:
            if x in local:
                return False
            if x in done:
                break
            local.add(x)
            x=out[x]
        done.update(local)
    return True


def enumerate_faces():
    faces=set()
    counts=Counter()
    state_count=0
    for states in product((0,1,2), repeat=9):
        state_count += 1
        tails=set(); arrows=[]; ids=[]; ok=True
        for ei,(st,(u,v)) in enumerate(zip(states,EDGES)):
            if st==0:
                continue
            if st==1:
                tail,head=u,v; pid=2*ei
            else:
                tail,head=v,u; pid=2*ei+1
            if tail in tails:
                ok=False; break
            tails.add(tail); arrows.append((tail,head)); ids.append(pid)
        if ok and ids and acyclic_arrows(arrows):
            f=frozenset(ids)
            faces.add(f); counts[len(f)] += 1
    assert state_count == 3**9
    return faces, counts


def matrix_forest_coeffs():
    # K_{3,3} Laplacian eigenvalues are 0,6,3,3,3,3.
    # det(lambda I + L)=lambda(lambda+6)(lambda+3)^4.
    poly=[1]
    for a in (0,6,3,3,3,3):
        new=[0]*(len(poly)+1)
        for i,c in enumerate(poly):
            new[i] += a*c
            new[i+1] += c
        poly=new
    # ascending powers of lambda
    return poly


def sequential_vertex_matching(faces):
    unmatched=set(faces)
    pairs=[]
    for v in range(NPRIM):
        lows=[s for s in unmatched if v not in s and (s|{v}) in unmatched]
        lows.sort(key=lambda s:(len(s),tuple(sorted(s))))
        for s in lows:
            t=s|{v}
            if s in unmatched and t in unmatched:
                unmatched.remove(s); unmatched.remove(t)
                pairs.append((s,t,v))
    return pairs, unmatched


def check_hasse_acyclic(faces,pairs):
    matched={(a,b) for a,b,_ in pairs}
    adj={f:[] for f in faces}
    indeg={f:0 for f in faces}
    hasse_edges=0
    for high in faces:
        if len(high)<=1: continue
        for x in high:
            low=high-{x}
            if low not in faces:
                raise AssertionError('missing face')
            hasse_edges += 1
            if (low,high) in matched:
                a,b=low,high
            else:
                a,b=high,low
            adj[a].append(b); indeg[b]+=1
    q=deque([f for f,d in indeg.items() if d==0])
    seen=0
    while q:
        u=q.popleft(); seen+=1
        for v in adj[u]:
            indeg[v]-=1
            if indeg[v]==0: q.append(v)
    return seen==len(faces), hasse_edges


def gf2_rank(columns):
    piv={}; rank=0
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p in piv:
                x ^= piv[p]
            else:
                piv[p]=x; rank+=1; break
    return rank


def boundary_ranks(faces):
    byk=defaultdict(list)
    for f in faces:
        byk[len(f)].append(tuple(sorted(f)))
    for k in byk: byk[k].sort()
    idx={k:{f:i for i,f in enumerate(byk[k])} for k in byk}
    ranks={1:1}
    for k in range(2,6):
        cols=[]
        for f in byk[k]:
            bits=0
            for j in range(k):
                sub=f[:j]+f[j+1:]
                bits ^= 1 << idx[k-1][sub]
            cols.append(bits)
        ranks[k]=gf2_rank(cols)
    betti=[]
    for k in range(1,6):
        betti.append(len(byk[k])-ranks[k]-ranks.get(k+1,0))
    return ranks, betti


def main():
    faces,counts=enumerate_faces()
    fvec=[counts[k] for k in range(1,6)]
    assert fvec == [18,126,432,729,486], fvec
    assert len(faces)==1791

    poly=matrix_forest_coeffs()
    # coefficients of lambda^5,...,lambda^1 count rooted forests with 1,...,5 edges.
    forest=[poly[5],poly[4],poly[3],poly[2],poly[1]]
    assert forest == fvec, (forest,fvec)

    pairs,critical=sequential_vertex_matching(faces)
    assert len(pairs)==855
    assert len(critical)==81
    profile=Counter(len(f)-1 for f in critical)
    assert profile == Counter({0:1,4:80}), profile
    assert [tuple(sorted(f)) for f in critical if len(f)==1] == [(0,)]

    ok,hasse_edges=check_hasse_acyclic(faces,pairs)
    assert ok
    assert hasse_edges==6894

    ranks,betti=boundary_ranks(faces)
    assert ranks == {1:1,2:17,3:109,4:323,5:406}, ranks
    assert betti == [0,0,0,0,80], betti

    serial=[(tuple(sorted(a)),tuple(sorted(b)),v) for a,b,v in pairs]
    serial.sort()
    cert_sha=hashlib.sha256(json.dumps(serial,separators=(',',':')).encode()).hexdigest()
    print('K33_MORSE_VERIFY_OK')
    print('states',3**9)
    print('nonempty_faces',len(faces))
    print('f_vector',fvec)
    print('hasse_edges',hasse_edges)
    print('matching_pairs',len(pairs))
    print('critical_profile',dict(sorted(profile.items())))
    print('gf2_boundary_ranks',[ranks[k] for k in range(1,6)])
    print('reduced_gf2_betti',betti)
    print('matching_certificate_sha256',cert_sha)

if __name__=='__main__':
    main()
