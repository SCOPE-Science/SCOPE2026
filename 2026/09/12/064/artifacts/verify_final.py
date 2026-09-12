"""Final rigorous verification: E1, E2 are genus-3, non-isomorphic, isolated vertices of the flip graph.
Self-contained: face tracer + canon + exhaustive single-vertex flip enumeration. Uses witnesses.json."""
import itertools, json

def build_pos(rotA, rotB):
    posA=[[0]*7 for _ in range(4)]
    for a in range(4):
        for k,b in enumerate(rotA[a]): posA[a][b]=k
    posB=[[0]*4 for _ in range(7)]
    for b in range(7):
        for k,a in enumerate(rotB[b]): posB[b][a]=k
    return posA,posB

def face_lens(rotA, rotB):
    posA,posB=build_pos(rotA,rotB)
    visA=[[False]*7 for _ in range(4)]
    visB=[[False]*4 for _ in range(7)]
    fl=[]
    for a0 in range(4):
        for b0 in range(7):
            if visA[a0][b0]: continue
            ca,cb,side=a0,b0,1
            L=0
            while True:
                if side==1:
                    assert not visA[ca][cb]
                    visA[ca][cb]=True; L+=1
                    na=rotB[cb][(posB[cb][ca]-1)%4]
                    ca,cb,side=na,cb,0
                else:
                    assert not visB[cb][ca]
                    visB[cb][ca]=True; L+=1
                    nb=rotA[ca][(posA[ca][cb]-1)%7]
                    if ca==a0 and nb==b0: break
                    ca,cb,side=ca,nb,1
            fl.append(L)
    return sorted(fl)

def min_cyc(lst):
    n=len(lst); return min(tuple(lst[(i+k)%n] for k in range(n)) for i in range(n))

def canon(rotA, rotB):
    best=None
    for pa0 in range(4):
        row0=rotA[pa0]
        for s in range(7):
            q=[0]*7
            for j,c in enumerate(row0): q[c]=(j+s)%7
            pb=[0]*7
            for c in range(7): pb[q[c]]=c
            rest=[a for a in range(4) if a!=pa0]
            for perm in itertools.permutations(rest):
                pa=(pa0,)+perm
                pinv=[0]*4
                for i,a in enumerate(pa): pinv[a]=i
                tA=tuple(min_cyc([q[b] for b in rotA[pa[i]]]) for i in range(4))
                tB=tuple(min_cyc([pinv[a] for a in rotB[pb[j]]]) for j in range(7))
                t=(tA,tB)
                if best is None or t<best: best=t
    return best

def check_isolated(tag, rotA, rotB):
    fl=face_lens(rotA,rotB)
    assert len(fl)==13 and sum(fl)==56, (tag,fl)
    g=1-(11-28+len(fl))/2
    assert g==3, (tag,g)
    c0=canon(rotA,rotB)
    total=0; nonself=0
    for a in range(4):
        base=rotA[a]; seen=set()
        for p in itertools.permutations(base):
            if list(p)==base or tuple(p) in seen: continue
            seen.add(tuple(p))
            nA=[x[:] for x in rotA]; nA[a]=list(p)
            if len(face_lens(nA,rotB))==13:
                total+=1
                if canon(nA,rotB)!=c0: nonself+=1
    for b in range(7):
        base=rotB[b]; seen=set()
        for p in itertools.permutations(base):
            if list(p)==base or tuple(p) in seen: continue
            seen.add(tuple(p))
            nB=[x[:] for x in rotB]; nB[b]=list(p)
            if len(face_lens(rotA,nB))==13:
                total+=1
                if canon(rotA,nB)!=c0: nonself+=1
    print(f"{tag}: faces={len(fl)} genus={g} lens={fl} genus3flips={total} nonself={nonself}")
    return c0, total, nonself

if __name__=="__main__":
    import sys
    sys.path.insert(0,"/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1262/output/artifacts")
    with open("/srv/scope-research/rounds/2026-09-07-first-light-01/workspaces/research/lane-1262/output/artifacts/witnesses.json") as f:
        w=json.load(f)
    c1,_,n1=check_isolated("E1",w["E1"]["rotA"],w["E1"]["rotB"])
    c2,_,n2=check_isolated("E2",w["E2"]["rotA"],w["E2"]["rotB"])
    print("non-isomorphic:", c1!=c2)
    assert c1!=c2 and n1==0 and n2==0
    print("VERIFIED: flip graph disconnected (two isolated non-isomorphic genus-3 vertices)")
