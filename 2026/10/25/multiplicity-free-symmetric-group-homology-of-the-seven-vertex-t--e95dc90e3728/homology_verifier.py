#!/usr/bin/env python3
"""Standalone exact reduced simplicial Morse chain certificate for triangle-free graphs."""
import itertools, collections, functools, sys, time, hashlib, json, argparse
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

def sign_boundary(mask):
    pos=0
    while mask:
        bit=mask&-mask; mask^=bit
        yield bit, -1 if pos%2 else 1
        pos+=1

def verify(n, reverse=False, graph_check=True):
    edges=list(itertools.combinations(range(n),2)); positions={e:i for i,e in enumerate(edges)}
    triangles=[sum(1<<positions[e] for e in itertools.combinations(t,2)) for t in itertools.combinations(range(n),3)]
    face_set={mask for mask in range(1<<len(edges)) if all(mask&t!=t for t in triangles)}
    fv=collections.Counter(x.bit_count()-1 for x in face_set)
    rem=face_set.copy();pairs={}
    for j in (range(len(edges)-1,-1,-1) if reverse else range(len(edges))):
        bit=1<<j
        for mask in tuple(rem):
            if not mask&bit and mask|bit in rem:
                rem.remove(mask);rem.remove(mask|bit);pairs[mask]=mask|bit
    critical=rem
    counts=collections.Counter(x.bit_count()-1 for x in critical)
    if graph_check:
        # Orient every cover relation of the face poset; matched incidences go up.
        # Kahn's algorithm certifies absence of every closed gradient path.
        names=sorted(face_set);idx={m:i for i,m in enumerate(names)}
        adj=[[] for _ in names];indegree=[0]*len(names);incident=0
        for upper in names:
            for bit,sign in sign_boundary(upper):
                lower=upper^bit
                if pairs.get(lower)==upper:src,dst=lower,upper
                else:src,dst=upper,lower
                a=idx[src]; b=idx[dst]
                adj[a].append(b);indegree[b]+=1;incident+=1
        q=collections.deque(i for i,k in enumerate(indegree) if k==0)
        visited=0
        while q:
            u=q.popleft();visited+=1
            for v in adj[u]:
                indegree[v]-=1
                if not indegree[v]:q.append(v)
        assert visited==len(names),(visited,len(names))
    else:incident=None
    upper_set=set(pairs.values())
    sys.setrecursionlimit(500000)
    @functools.lru_cache(maxsize=None)
    def project(s):
        if s in critical:return {s:1}
        if s in upper_set:return {}
        u=pairs[s];b=u^s
        eps=next(sig for bit,sig in sign_boundary(u) if bit==b)
        res={}
        for bit,sig in sign_boundary(u):
            t=u^bit
            if t==s:continue
            for w,v in project(t).items():
                new=res.get(w,0)-eps*sig*v
                if new:res[w]=new
                elif w in res:del res[w]
        return res
    mats={}; outputs={}
    for d in range(max(fv)+1,0,-1):
        cols=sorted(x for x in critical if x.bit_count()-1==d)
        rows=sorted(x for x in critical if x.bit_count()-1==d-1)
        if not cols and not rows:continue
        matrix=[]
        for c in cols:
            accumulation={}
            for bit,sign in sign_boundary(c):
                for row,val in project(c^bit).items():
                    new=accumulation.get(row,0)+sign*val
                    if new:accumulation[row]=new
                    elif row in accumulation:del accumulation[row]
            matrix.append([accumulation.get(row,0) for row in rows])
        M=Matrix(matrix).T if cols and rows else Matrix.zeros(len(rows),len(cols))
        mats[d]=M
        if M.rows and M.cols:
            D=smith_normal_form(M,domain=ZZ)
            nonzero=[int(abs(D[i,i])) for i in range(min(D.rows,D.cols)) if D[i,i]]
        else:nonzero=[]
        outputs[d]={'shape':[M.rows,M.cols],'smith_nonzero':nonzero,'rank':len(nonzero),'nonzero_entries':sum(v!=0 for v in M)}
    for d in mats:
        if d-1 in mats:assert mats[d-1]*mats[d]==Matrix.zeros(mats[d-1].rows,mats[d].cols),d
    # torsion in H_d comes from Smith factors >1 of im d_{d+1}; boundary
    # subgroup im d_{d+1} is contained in ker d_d, a primitive sublattice.
    result={}
    for d,k in sorted(counts.items()):
        above=outputs.get(d+1,{'rank':0,'smith_nonzero':[]})
        below=outputs.get(d,{'rank':0})
        rank=k-above['rank']-below['rank']
        torsion=[x for x in above['smith_nonzero'] if x>1]
        if rank or torsion:result[d]={'free_rank':rank,'torsion':torsion}
    return {'n':n,'reverse':reverse,'f_vector':dict(sorted(fv.items())),
       'number_of_faces_including_empty':len(face_set),'matched_pairs':len(pairs),
       'critical_cell_counts':dict(sorted(counts.items())),
       'directed_hasse_incidences':incident,'acyclicity_certified':graph_check,
       'differentials':outputs,'reduced_integral_homology':result,
       'matching_sha256':hashlib.sha256('\n'.join(f'{l}:{u}' for l,u in sorted(pairs.items())).encode()).hexdigest()}

if __name__=='__main__':
    T=time.monotonic()
    for n in (5,6,7):
        for rev in (False,True) if n>=6 else (False,):
            dat=verify(n,rev,True)
            print(json.dumps(dat,sort_keys=True,separators=(',',':')),flush=True)
    print('VERIFY_OK', 'elapsed', round(time.monotonic()-T,2),flush=True)
