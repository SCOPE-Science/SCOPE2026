"""Exact integral simplicial-homology certificate for the bidirected K(2,5)."""
from itertools import combinations
from math import gcd


def make_complex():
    leaves = (2, 3, 4, 5, 6)
    arcs = tuple(arc for w in leaves for arc in ((0,w),(w,0),(1,w),(w,1)))
    faces = [set() for _ in range(4)]
    faces_by_mask={0}
    for mask in range(1, 1 << len(arcs)):
        if mask ^ (mask & -mask) not in faces_by_mask:
            continue
        chosen = [arcs[i] for i in range(len(arcs)) if (mask >> i) & 1]
        sources = [a for a,b in chosen]
        targets = [b for a,b in chosen]
        if len(set(sources)) != len(chosen) or len(set(targets)) != len(chosen):
            continue
        # All indegrees and outdegrees <=1. A directed cycle must have length 2 or 4.
        succ=dict(chosen)
        cyclic=False
        for v in range(7):
            visited=set()
            while v in succ:
                if v in visited:
                    cyclic=True
                    break
                visited.add(v)
                v=succ[v]
            if cyclic:
                break
        if not cyclic:
            faces_by_mask.add(mask)
            faces[len(chosen)-1].add(mask)
    return arcs,[sorted(F) for F in faces]


def boundaries(faces):
    output=[]
    for degree in range(1,4):
        row_index={m:i for i,m in enumerate(faces[degree-1])}
        columns=[]
        for mask in faces[degree]:
            inds=[i for i in range(20) if mask & (1 << i)]
            columns.append({row_index[mask^(1<<i)]:(-1)**j for j,i in enumerate(inds)})
        output.append((len(faces[degree-1]),columns))
    return output


def unit_diagonal_and_remainder(nrows, columns):
    rows=[{} for _ in range(nrows)]
    cols=[{} for _ in columns]
    for j,col in enumerate(columns):
        for i,value in col.items():
            rows[i][j]=value
            cols[j][i]=value
    eliminated=0
    while True:
        cand=None;best=None
        for i,row in enumerate(rows):
            for j,val in row.items():
                if abs(val)!=1:
                    continue
                cost=(len(row)-1)*(len(cols[j])-1)
                if best is None or cost<best:
                    best=cost;cand=(i,j)
        if cand is None:
            break
        i,j=cand
        pivot=rows[i][j]
        old_col=list(cols[j].items())
        old_row=list(rows[i].items())
        for a,val in old_col:
            if a==i:continue
            for b,w in old_row:
                if b==j:continue
                new=rows[a].get(b,0)-val*w*pivot
                if new:
                    rows[a][b]=new;cols[b][a]=new
                else:
                    rows[a].pop(b,None);cols[b].pop(a,None)
        for a,_ in old_col:
            rows[a].pop(j,None)
        for b,_ in old_row:
            cols[b].pop(i,None)
        rows[i].clear();cols[j].clear()
        eliminated+=1
    left={(i,j):v for i,row in enumerate(rows) for j,v in row.items()}
    return eliminated,left


def rank_one_certificate(residual):
    # Integer rank <=1 is exactly equivalent to vanishing of all 2x2 minors.
    rowlist=sorted({i for i,j in residual})
    collist=sorted({j for i,j in residual})
    for k,i in enumerate(rowlist):
        for h in rowlist[k+1:]:
            for l,j in enumerate(collist):
                for b in collist[l+1:]:
                    assert residual.get((i,j),0)*residual.get((h,b),0)==residual.get((i,b),0)*residual.get((h,j),0)
    g=0
    for val in residual.values():
        g=gcd(g,abs(val))
    return (1 if residual else 0),g


def check_chain(faces,matrices):
    for k in (0,1):
        lower=matrices[k][1]
        higher=matrices[k+1][1]
        for column in higher:
            accum={}
            for i,v in column.items():
                for j,w in lower[i].items():
                    accum[j]=accum.get(j,0)+v*w
            assert all(v==0 for v in accum.values())


def verify_module(arcs):
    # Every directed two-cycle and every directed four-cycle is forced
    # into any dynamical region containing one of its edges.
    parent=list(range(len(arcs)))
    where={a:i for i,a in enumerate(arcs)}
    def root(i):
        while parent[i]!=i:
            i=parent[i]
        return i
    def join(i,j):
        parent[root(i)]=root(j)
    def join_cycle(cycle):
        for a,b in zip(cycle,cycle[1:]):
            join(where[a],where[b])
    for a,b in arcs:
        join_cycle(((a,b),(b,a)))
    for u,v in combinations((2,3,4,5,6),2):
        for a,b in ((u,v),(v,u)):
            join_cycle(((0,a),(a,1),(1,b),(b,0)))
    assert len({root(i) for i in range(len(arcs))})==1
    for v in range(7):
        assert any(a==v for a,b in arcs) and any(b==v for a,b in arcs)


def main():
    arcs,faces=make_complex()
    assert len(arcs)==20
    fv=tuple(map(len,faces))
    assert fv==(20,130,320,240),fv
    matrices=boundaries(faces)
    check_chain(faces,matrices)
    answer=[]
    for i,(rows,cols) in enumerate(matrices):
        units,residual=unit_diagonal_and_remainder(rows,cols)
        rr,g=rank_one_certificate(residual)
        answer.append((units,rr,g,len(residual)))
    assert answer[0]==(19,0,0,0),answer
    assert answer[1]==(111,0,0,0),answer
    assert answer[2][0]==208 and answer[2][1:3]==(1,2),answer
    rank3=answer[2][0]+answer[2][1]
    assert rank3==209
    verify_module(arcs)
    print('VERIFIED f_vector=',fv)
    print('VERIFIED integer Smith ranks (units, residual_rank, residual_gcd, residual_nnz)=',answer)
    print('VERIFIED integral homology: H0=Z, H1=0, H2=Z/2, H3=Z^31')
    print('VERIFIED arc-cycle connectedness: single unstable dynamical module')

if __name__=='__main__':
    main()
