#!/usr/bin/env python3
"""Standalone plain k-variable type refinement, without counting; standard library."""
from itertools import product
from collections import defaultdict

def graph(a,b):
    m=len(a);vertices=[];blocks=[]
    for z in (a,b):
        row=[]
        for count in z:
            row.append(list(range(len(vertices),len(vertices)+count)))
            vertices.extend(row[-1])
        blocks.append(row)
    n=len(vertices);adj=[[0]*n for _ in range(n)]
    for i in range(m):
        for j in range(i+1):
            for x in blocks[0][i]:
                for y in blocks[1][j]:adj[x][y]=adj[y][x]=1
    return adj

def key(a,b):
    return min((tuple(a),tuple(b)),(tuple(b[::-1]),tuple(a[::-1])))

def classify(specs,k):
    GS=[graph(a,b) for a,b in specs]
    ns=[len(G) for G in GS]
    ids={};colors=[]
    for G,n in zip(GS,ns):
        C=[]
        for z in product(range(n),repeat=k):
            s=tuple((z[i]==z[j],G[z[i]][z[j]]) for i in range(k) for j in range(i))
            if s not in ids:ids[s]=len(ids)
            C.append(ids[s])
        colors.append(C)
    rounds=0
    while True:
        rounds+=1
        ids={};future=[]
        for n,C in zip(ns,colors):
            step=[];positions=[n**(k-1-i) for i in range(k)]
            for idx in range(n**k):
                types=[]
                for stride in positions:
                    base=idx-((idx//stride)%n)*stride
                    types.append(tuple(sorted({C[base+t*stride] for t in range(n)})))
                s=(C[idx],tuple(types))
                if s not in ids:ids[s]=len(ids)
                step.append(ids[s])
            future.append(step)
        oldcount=len({x for C in colors for x in C})
        colors=future
        if len(ids)==oldcount:break
        assert rounds<=30
    sig=[]
    for n,C in zip(ns,colors):
        # A one-variable type corresponds to the all-equal diagonal k-tuple.
        diagonal=sum(n**j for j in range(k))
        sig.append(tuple(sorted({C[x*diagonal] for x in range(n)})))
    return sig,rounds

def main():
    jobs=[]
    for m,r in ((1,range(1,5)),(2,range(1,5)),(3,range(1,4))):
        specs=[]
        for v in product(r,repeat=2*m):
            a,b=v[:m],v[m:]
            if key(a,b)==(a,b):specs.append((a,b))
        sig,rounds=classify(specs,3)
        groups=defaultdict(list)
        for spec,ss in zip(specs,sig):groups[ss].append(spec)
        for members in groups.values():
            trueclasses={key(tuple(min(t,3) for t in a),tuple(min(t,3) for t in b)) for a,b in members}
            assert len(trueclasses)==1, members
        assert len(groups)==len({key(tuple(min(t,3) for t in a),tuple(min(t,3) for t in b)) for a,b in specs})
        print('width3',m,'graphs',len(specs),'theories',len(groups),'rounds',rounds)
        jobs.append(len(specs))
    for k in (3,4):
        specs=[((k,), (1,)),((k+1,), (1,))]
        sig,rounds=classify(specs,k)
        assert sig[0]==sig[1]
        print('sharp_equiv',k,'rounds',rounds)
        sig,rounds=classify(specs,k+1)
        assert sig[0]!=sig[1]
        print('sharp_separate',k+1,'rounds',rounds)
    print('compared_graph_instances',sum(jobs))
    print('LOGIC_PASS')
if __name__=='__main__':main()
