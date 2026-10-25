"""Cross-check every local size distribution by explicit path-bitmask enumeration."""
from itertools import combinations
from collections import Counter
from verify_grid import TABLE


def route_masks(start, end, index):
    found=[]
    def walk(v, internal):
        if v == end:
            found.append(internal)
            return
        remaining=abs(end[0]-v[0])+abs(end[1]-v[1])
        for w in ((v[0]+1,v[1]),(v[0]-1,v[1]),(v[0],v[1]+1),(v[0],v[1]-1)):
            if abs(end[0]-w[0])+abs(end[1]-w[1])!=remaining-1:continue
            walk(w,internal if w==end else internal|(1<<index[w]))
    walk(start,0)
    return found


def full_profile(h,w,k):
    cells=[(i,j) for i in range(h) for j in range(w)]
    index={p:i for i,p in enumerate(cells)}
    route={}
    for a,b in combinations(range(len(cells)),2):
        u,v=cells[a],cells[b]
        if abs(u[0]-v[0])+abs(u[1]-v[1])<=k:
            route[a,b]=route_masks(u,v,index)
    hist=Counter()
    for bits in range(1,1<<(h*w)):
        selected=[i for i in range(h*w) if bits&(1<<i)]
        if not(0 in [cells[t][0] for t in selected] and h-1 in [cells[t][0] for t in selected]
               and 0 in [cells[t][1] for t in selected] and w-1 in [cells[t][1] for t in selected]):continue
        if all((a,b) in route and any(bits&path==0 for path in route[a,b]) for a,b in combinations(selected,2)):
            hist[len(selected)]+=1
    return dict(sorted(hist.items()))


def verify():
    for k in (2,3):
        for h in range(1,5):
            for w in range(1,5):
                got=full_profile(h,w,k)
                expect=TABLE[k].get((min(h,w),max(h,w)),{})
                assert got==expect,(k,h,w,got,expect)
        print(f'k={k}: independent shortest-path-bitmask census PASS')
if __name__=='__main__':verify()
