#!/usr/bin/env python3
"""Independent finite checks for small binary 2-out digraphs.
No dependencies outside the Python standard library."""
import csv,itertools,collections,math,json,sys,pathlib,argparse

def all_parts(n):
    def rec(groups, i):
        if i == n:
            if 2 <= len(groups) < n:
                yield [tuple(x) for x in groups]
            return
        for j in range(len(groups)):
            groups[j].append(i)
            yield from rec(groups,i+1)
            groups[j].pop()
        groups.append([i]); yield from rec(groups,i+1); groups.pop()
    yield from rec([[0]],1)

def lumpable(edges,blocks):
    owner={x:i for i,group in enumerate(blocks) for x in group}
    for block in blocks:
        patterns=[tuple(sorted(owner[y] for y in edges[x])) for x in block]
        if len(set(patterns)) > 1: return False
    return True

def synchronize_pairwise(edges, bits):
    n=len(edges)
    trans=[]
    for letter in range(2):
        trans.append(tuple(edges[q][letter^((bits>>q)&1)] for q in range(n)))
    P=list(itertools.combinations(range(n),2))
    known=set()
    successors={}
    for u,v in P:
        nex=[]
        for t in trans:
            a,b=t[u],t[v]
            nex.append(tuple(sorted((a,b))) if a!=b else None)
        successors[(u,v)]=nex
        if None in nex: known.add((u,v))
    changed=True
    while changed:
        changed=False
        for pair, successor in successors.items():
            if pair not in known and any(z in known for z in successor):
                known.add(pair);changed=True
    return len(known)==len(P)

def independent_canonical_orbit(edges):
    n=len(edges)
    opts=[(a,b) for a in range(n) for b in range(a,n)]
    encode={e:i for i,e in enumerate(opts)}
    powers=[len(opts)**i for i in range(n)]
    codes=[]
    for perm in itertools.permutations(range(n)):
        changed=[None]*n
        for u,(v,w) in enumerate(edges):
            changed[perm[u]]=tuple(sorted((perm[v],perm[w])))
        codes.append(sum(encode[changed[i]]*powers[i] for i in range(n)))
    return min(codes),len(set(codes))

def independent_primitive(edges):
    n=len(edges)
    adj=[set(e) for e in edges]
    reachable={0}
    for _ in range(n):
        reachable |= {v for u in reachable for v in adj[u]}
    if len(reachable)!=n: return False
    reverse=[{u for u in range(n) if v in adj[u]} for v in range(n)]
    seen={0}
    for _ in range(n):seen|={u for v in seen for u in reverse[v]}
    if len(seen)!=n:return False
    # Every vertex recurrence admits gcd of lengths of closed walks.
    distance=[None]*n;distance[0]=0;queue=collections.deque([0])
    while queue:
        u=queue.popleft()
        for v in adj[u]:
            if distance[v] is None:distance[v]=distance[u]+1;queue.append(v)
    period=0
    for u in range(n):
        for v in adj[u]:period=math.gcd(period,distance[u]+1-distance[v])
    return period==1

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--data-dir',default='data'); args=ap.parse_args()
    root=pathlib.Path(args.data_dir)
    record={}
    for n in range(2,6):
        parts=list(all_parts(n))
        with open(root / f'graph_{n}.csv') as f:
            rec=[r for r in csv.reader(f) if r and r[0]=='R']
        counter=collections.Counter(); orbtotal=0; labels_sync=0; labels_simple=0; labels_both=0; identifiers=set()
        for row in rec:
            _,code,orbit,sy,simp,equip,edges,pi = row
            edges=[tuple(map(int,x.split(':'))) for x in edges.split(';')]
            assert len(edges)==n
            assert independent_primitive(edges)
            canonical,osize=independent_canonical_orbit(edges)
            assert canonical==int(code) and osize==int(orbit),(n,code,canonical,osize)
            assert int(code) not in identifiers
            identifiers.add(int(code))
            orbtotal+=osize
            pi=tuple(map(int,pi.split(':')))
            assert all(v>0 for v in pi) and math.gcd(*pi)==1
            for target in range(n):
                assert sum(pi[i] for i,edge in enumerate(edges) for v in edge if v==target)==2*pi[target]

            s=sum(synchronize_pairwise(edges,bits) for bits in range(1<<n))
            assert s==int(sy),(n,code,s,sy)
            simple=not any(lumpable(edges,part) for part in parts)
            assert simple==(simp=='1'),(n,code)
            indeg=[sum(y==u for edge in edges for y in edge) for u in range(n)]
            eulerian=(indeg==[2]*n)
            counter[(simple,s==(1<<n),eulerian,s)] += 1
            if s==(1<<n):labels_sync+=osize
            if simple: labels_simple+=osize
            if simple and s==(1<<n):labels_both+=osize
            if simple and s<(1<<n) and n==5:
                counter[('obstruction',tuple(sorted(pi)),s)]+=1
        if n==5:
            assert (len(rec),orbtotal,labels_sync,labels_simple,labels_both)==(1220,141420,104340,56208,53760)
        record[n]={str(k):v for k,v in sorted(counter.items(),key=lambda z:str(z[0]))}
        print(n, 'types',len(rec),'totally',sum(s==(1<<n) for x in rec for s in [int(x[3])]), 'simple',sum(x[4]=='1' for x in rec), 'simple-not-totally',sum(x[4]=='1' and int(x[3])<(1<<n) for x in rec), flush=True)
    assert len(record)==4
    assert sum(v for k,v in counter.items() if isinstance(k,tuple) and len(k)==4 and k[0]==True and k[1]==False)==22
    print('STATIONARY_OBSTRUCTION_PROFILE',[(k,v) for k,v in sorted(counter.items(),key=lambda z:str(z[0])) if k[0]=='obstruction'])
    print('INDEPENDENT_CHECK_PASS')
if __name__=='__main__':main()
