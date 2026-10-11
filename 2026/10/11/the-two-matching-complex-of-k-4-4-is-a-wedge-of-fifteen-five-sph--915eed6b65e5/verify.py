#!/usr/bin/env python3
import collections, json

ROWS = COLS = 4
EDGES = [(i,j) for i in range(ROWS) for j in range(COLS)]
N = len(EDGES)
TOGGLE_ORDER = [7,2,5,10,1,11,13,9,12,15,8,0,4,3,14,6]
EXPECTED = {
    "face_count": 7342,
    "f_vector": [16,120,528,1428,2304,2040,816,90],
    "matching_pairs": 3663,
    "critical_counts": {"0":1,"5":15},
    "critical_masks": [128,873,2403,10522,10777,17969,17976,25904,33562,34401,35347,42568,42576,44098,49761,50736],
    "hasse_covers": 37728,
    "boundary_ranks_f2": {"1":15,"2":105,"3":423,"4":1005,"5":1299,"6":726,"7":90},
    "reduced_betti_f2": {"5":15},
    "euler_characteristic": -14,
    "reduced_euler_characteristic": -15,
}

def enumerate_faces():
    faces=set(); bydim=collections.defaultdict(list)
    for mask in range(1,1<<N):
        dr=[0]*ROWS; dc=[0]*COLS; ok=True
        for k,(i,j) in enumerate(EDGES):
            if (mask>>k)&1:
                dr[i]+=1; dc[j]+=1
                if dr[i]>2 or dc[j]>2:
                    ok=False; break
        if ok:
            faces.add(mask); bydim[mask.bit_count()-1].append(mask)
    for d in bydim: bydim[d].sort()
    return faces, bydim

def greedy_toggle_matching(faces):
    unmatched=set(faces); up={}; down={}
    for e in TOGGLE_ORDER:
        bit=1<<e
        for low in sorted(tuple(unmatched)):
            if low not in unmatched or (low & bit):
                continue
            high=low|bit
            if high in unmatched:
                unmatched.remove(low); unmatched.remove(high)
                up[low]=high; down[high]=low
    return up,down,unmatched

def verify_acyclic(faces,down):
    indeg={x:0 for x in faces}; adj={x:[] for x in faces}; covers=0
    for high in faces:
        for i in range(N):
            if not ((high>>i)&1): continue
            low=high^(1<<i)
            if low==0 or low not in faces: continue
            covers+=1
            if down.get(high)==low: u,v=high,low
            else: u,v=low,high
            adj[u].append(v); indeg[v]+=1
    q=collections.deque(x for x in faces if indeg[x]==0); seen=0
    while q:
        u=q.popleft(); seen+=1
        for v in adj[u]:
            indeg[v]-=1
            if indeg[v]==0: q.append(v)
    return covers, seen==len(faces), seen

def rank_f2(cols):
    piv={}; r=0
    for col in cols:
        x=col
        while x:
            p=x.bit_length()-1
            if p in piv: x^=piv[p]
            else:
                piv[p]=x; r+=1; break
    return r

def homology_f2(bydim):
    ranks={}
    maxd=max(bydim)
    for d in range(1,maxd+1):
        lower=bydim[d-1]; idx={f:i for i,f in enumerate(lower)}; cols=[]
        for high in bydim[d]:
            col=0
            for i in range(N):
                if (high>>i)&1:
                    low=high^(1<<i)
                    if low in idx: col ^= 1<<idx[low]
            cols.append(col)
        ranks[d]=rank_f2(cols)
    betti={}
    for d in range(maxd+1):
        b=len(bydim[d])-ranks.get(d,0)-ranks.get(d+1,0)
        if d==0: b-=1
        if b: betti[d]=b
    return ranks,betti

def main():
    faces,bydim=enumerate_faces()
    up,down,critical=greedy_toggle_matching(faces)
    assert all(low in faces and high in faces and high.bit_count()==low.bit_count()+1 and (low&high)==low for low,high in up.items())
    covers,acyclic,seen=verify_acyclic(faces,down)
    ranks,betti=homology_f2(bydim)
    chi=sum(((-1)**d)*len(bydim[d]) for d in bydim)
    actual={
        "face_count":len(faces),
        "f_vector":[len(bydim[d]) for d in range(max(bydim)+1)],
        "matching_pairs":len(up),
        "critical_counts":{str(d):c for d,c in sorted(collections.Counter(x.bit_count()-1 for x in critical).items())},
        "critical_masks":sorted(critical),
        "hasse_covers":covers,
        "acyclic":acyclic,
        "topological_sort_seen":seen,
        "boundary_ranks_f2":{str(k):v for k,v in sorted(ranks.items())},
        "reduced_betti_f2":{str(k):v for k,v in sorted(betti.items())},
        "euler_characteristic":chi,
        "reduced_euler_characteristic":chi-1,
    }
    for k,v in EXPECTED.items():
        assert actual[k]==v, (k,actual[k],v)
    assert actual["acyclic"] and actual["topological_sort_seen"]==actual["face_count"]
    print(json.dumps(actual,sort_keys=True,separators=(",",":")))

if __name__=="__main__": main()
