"""Exact four-round FO spectra of iterated directed 3-cycles.
Pure Python 3, no external dependencies. Exact exhaustive orbit-transition search.
"""
from collections import defaultdict


def make_graph(h, q=4):
    N = 3**h
    powers = [3**(h-1-j) for j in range(h)]
    digits = [tuple((v//p)%3 for p in powers) for v in range(N)]
    pair = [[0]*N for _ in range(N)]
    for a in range(N):
        for b in range(a+1,N):
            j = next(j for j in range(h) if digits[a][j]!=digits[b][j])
            val = 2*j+1 if (digits[b][j]-digits[a][j])%3==1 else 2*j+2
            pair[a][b] = val
            pair[b][a] = val ^ 3 if (val%2 and j==0) else 2*j+(2 if val%2 else 1)
    def key(vs):
        return tuple(pair[vs[i]][vs[j]] for i in range(len(vs)) for j in range(i+1,len(vs)))
    sets=[{():()}]
    edges=[]
    for r in range(q):
        successors={}; next_states={}
        for code,vs in sets[-1].items():
            out=set()
            for w in range(N):
                newvs=vs+(w,)
                newkey=key(newvs)
                out.add(newkey)
                if newkey not in next_states:next_states[newkey]=newvs
            successors[code]=out
        edges.append(successors)
        sets.append(next_states)
    return pair,sets,edges

def run(q=4,hmax=5):
    assert q>=1
    all_graphs={}
    for h in range(1,hmax+1):
        pair,sets,edges=make_graph(h,q)
        print('ORBIT_COUNTS',h,tuple(len(x) for x in sets),flush=True)
        all_graphs[h]=(pair,sets,edges)
    ids={}
    maxid=0
    signatures={h:[{} for _ in range(q+1)] for h in all_graphs}
    for r in range(q,-1,-1):
        for h,(pair,sets,edges) in all_graphs.items():
            for key,vs in sets[r].items():
                diagram=tuple(0 if pair[vs[i]][vs[j]]==0 else 1 if pair[vs[i]][vs[j]]%2 else 2
                              for i in range(r) for j in range(i+1,r))
                extension=tuple(sorted({signatures[h][r+1][k] for k in edges[r][key]})) if r<q else ()
                desc=(r,diagram,extension)
                if desc not in ids: maxid+=1;ids[desc]=maxid
                signatures[h][r][key]=ids[desc]
    classes={h:signatures[h][0][()] for h in all_graphs}
    print('TYPE_IDS',classes,flush=True)
    class_repr={h:next(j for j in classes if classes[j]==v) for h,v in classes.items()}
    print('CLASS_REP',class_repr,flush=True)
    if q==4 and hmax>=5:
        assert class_repr=={1:1,2:2,3:3,4:4,5:4},class_repr
        assert len(set(classes.values()))==4
        print('FOUR_RANK4_CLASSES_AND_PUMPING_BASE_OK')
    return classes

if __name__=='__main__':
    run()
