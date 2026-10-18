"""Independent graph-level and forbidden-pair enumeration checks."""
from collections import Counter, defaultdict
from functools import lru_cache


def matchings(vertices):
    if not vertices:
        yield ()
        return
    x=vertices[0]
    for j in range(1,len(vertices)):
        y=vertices[j]
        for other in matchings(vertices[1:j]+vertices[j+1:]):
            yield ((x,y),)+other


def representative(parts):
    n=sum(parts)
    anchor=tuple((2*i,2*i+1) for i in range(n))
    other=[];k=0
    for part in parts:
        indices=list(range(k,k+part))
        other.extend((2*indices[i]+1,2*indices[(i+1)%part]) for i in range(part))
        k+=part
    return anchor,tuple(other)


def forbidden_count(anchor,other):
    n=len(anchor);forbid={tuple(sorted(edge)) for edge in anchor+other}
    @lru_cache(None)
    def f(mask):
        if mask==0:return 1
        v=(mask & -mask).bit_length()-1
        remaining=mask^(1<<v)
        out=0
        while remaining:
            b=remaining & -remaining
            w=b.bit_length()-1
            remaining-=b
            if (min(v,w),max(v,w)) not in forbid:
                out+=f((mask ^ (1<<v) ^ (1<<w)))
        return out
    return f((1<<(2*n))-1)


def graph_rounds(n):
    # Aggregate by cycle type of the union with the standard anchor.
    anchor=tuple((2*i,2*i+1) for i in range(n))
    inverse_anchor={u:v for u,v in anchor};inverse_anchor.update({v:u for u,v in anchor})
    ix={(u,v):k for k,(u,v) in enumerate((u,v) for u in range(2*n) for v in range(u+1,2*n))}
    types=[]; masks=[]; representatives={}
    for m in matchings(tuple(range(2*n))):
        q={u:v for u,v in m};q.update({v:u for u,v in m})
        seen=set();p=[]
        for v in range(2*n):
            if v not in seen:
                w=v;s=0
                while w not in seen:
                    seen.add(w);seen.add(inverse_anchor[w]);s+=1
                    w=q[inverse_anchor[w]]
                p.append(s)
        tp=tuple(sorted(p))
        mask=sum(1<<ix[tuple(sorted((u,v)))] for u,v in m)
        masks.append(mask);types.append(tp);representatives.setdefault(tp,mask)
    names=sorted(representatives);nd={x:i for i,x in enumerate(names)};mat=[]
    for tp in names:
        rep=representatives[tp]
        row=[0]*len(names)
        for mask,other in zip(masks,types):
            if not (rep & mask):row[nd[other]]+=1
        mat.append(row)
    color=[0 if t==(1,)*n else 1 for t in names]
    rounds=[len(set(color))]
    snapshots=[]
    while True:
        old=sorted(set(color))
        values=[]
        for i in range(len(names)):
            values.append((color[i], tuple(sum(mat[i][j] for j in range(len(names)) if color[j]==a) for a in old)))
        ids={sig:i for i,sig in enumerate(sorted(set(values)))}
        new=[ids[x] for x in values]
        rounds.append(len(ids));snapshots.append(new)
        if len(ids)==len(set(color)):break
        color=new
    assert len(set(color))==len(names) or len(set(new))==len(names)
    return rounds, names, snapshots


def main():
    tested=0
    for m in range(2,6):
        for r in range(0,3):
            n=2*m+r
            if n>10:continue
            samples=[()] if r==0 else [(1,)*r, (r,)]
            for rho in set(samples):
                A,C=representative((m,m)+rho)
                B,D=representative((2*m,)+rho)
                left=forbidden_count(A,C)
                right=forbidden_count(B,D)
                E,F=representative(rho)
                rest=forbidden_count(E,F)
                assert left-right==2*rest, (m,r,rho,left,right,rest)
                tested+=1
    print('brute perfect-matching switching checks:', tested, 'PASS')
    for n in range(3,8):
        rounds,names,snapshots=graph_rounds(n)
        print('direct derangement orbital graph, n=',n,'round-class counts=',rounds,'orbit count=',len(names))
        assert rounds[-1] == len(names)
        if n>=5 and n%2:
            a=tuple(sorted((1,(n-1)//2,(n-1)//2)))
            b=tuple(sorted((1,n-1)))
            assert snapshots[1][names.index(a)]==snapshots[1][names.index(b)]
            assert snapshots[2][names.index(a)]!=snapshots[2][names.index(b)]
    print('direct refinement and third-round separation: PASS')


if __name__=='__main__':main()
