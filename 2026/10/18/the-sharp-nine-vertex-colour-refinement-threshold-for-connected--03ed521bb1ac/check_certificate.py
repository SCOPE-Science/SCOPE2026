"""Independent validation of the finite representative list and refinement classes.
Usage: python3 check_certificate.py representatives.tsv
Only Python standard library is required.
"""
import csv
import itertools
import sys
from collections import Counter, defaultdict


def transpose(a, b, mask):
    return sum(1 << (j*a+i) for i in range(a) for j in range(b)
               if (mask >> (i*b+j)) & 1)


def canonical(a, b, mask):
    if b == 0:
        return 0
    def one_side(h, w, x):
        for p in itertools.permutations(range(h)):
            vals = [sum(((x >> (p[i]*w+j)) & 1) << i
                        for i in range(h)) for j in range(w)]
            yield tuple(sorted(vals))
    c = min(one_side(a,b,mask))
    if a == b:
        c = min(c,min(one_side(b,a,transpose(a,b,mask))))
    return c


def graph(a, b, mask):
    n=a+b
    result=[[] for _ in range(n)]
    for i in range(a):
        for j in range(b):
            if (mask>>(i*b+j))&1:
                result[i].append(a+j)
                result[a+j].append(i)
    return result


def connected(adj):
    seen={0}; stack=[0]
    while stack:
        for v in adj[stack.pop()]:
            if v not in seen:
                seen.add(v);stack.append(v)
    return len(seen)==len(adj)


def c4(a,b,mask):
    rows = [{j for j in range(b) if (mask>>(i*b+j))&1} for i in range(a)]
    return sum(len(rows[i]&rows[j])*(len(rows[i]&rows[j])-1)//2
               for i in range(a) for j in range(i+1,a))


def classes_at(n,graphs):
    colors=[[0]*n for _ in graphs]
    for _ in range(2*n+2):
        keys=[]
        for adj,c in zip(graphs,colors):
            keys.append([(c[v],tuple(sorted(c[w] for w in adj[v])))
                         for v in range(n)])
        vocabulary={key:i for i,key in enumerate(sorted(set(
            item for row in keys for item in row)))}
        nxt=[[vocabulary[item] for item in row] for row in keys]
        if colors==nxt:break
        colors=nxt
    groups=defaultdict(list)
    for i,row in enumerate(colors):
        groups[tuple(sorted(row))].append(i)
    return groups


def main(path):
    by_n=defaultdict(list)
    with open(path,newline='',encoding='utf-8') as f:
        for row in csv.DictReader(f,delimiter='\t'):
            n,a,b,m=(int(row[k]) for k in ('n','a','b','mask'))
            assert (n==1 and (a,b,m)==(1,0,0)) or (a>=1 and b>=a and a+b==n)
            adj=graph(a,b,m)
            assert connected(adj)
            by_n[n].append((a,b,m,adj))
    expected={1:1,2:1,3:1,4:3,5:5,6:17,7:44,8:182,9:730}
    expected_wl={**{n:expected[n] for n in range(1,9)},9:728}
    for n in range(1,10):
        rows=by_n[n]
        assert len(rows)==expected[n],(n,len(rows))
        codes=[(a,b,canonical(a,b,m)) for a,b,m,adj in rows]
        assert len(set(codes))==len(rows), f'duplicate isomorphism class at {n}'
        parts=classes_at(n,[adj for a,b,m,adj in rows])
        assert len(parts)==expected_wl[n],(n,len(parts))
        if n==9:
            ambiguous=sorted(sorted(rows[i][2] for i in ids)
                             for ids in parts.values() if len(ids)>1)
            assert ambiguous==[[106268,111290],[237369,241337]],ambiguous
            assert [c4(4,5,m) for m in ambiguous[0]]==[2,0]
            assert [c4(4,5,m) for m in ambiguous[1]]==[6,4]
        print(f'n={n}: {len(rows)} distinct connected bipartite types, {len(parts)} C2 classes')
    print('CERTIFICATE_CHECK_PASS')

if __name__=='__main__':
    if len(sys.argv)!=2:
        raise SystemExit('usage: python3 check_certificate.py representatives.tsv')
    main(sys.argv[1])
