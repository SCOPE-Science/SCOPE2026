#!/usr/bin/env python3
"""Finite elementary tests for periodic directed-path avalanche homology."""
import itertools, math, hashlib, json
from collections import defaultdict

def firing_sets(d,h,k):
    n=d*k
    # binary initial configuration: two zero residues, repeated k times
    c=[1 if i%d not in (0,h) else 0 for i in range(n)]
    out=[]
    for t in range(n):
        fire=frozenset(i for i in range(n) if c[i]>=1)
        out.append(fire)
        new=[0]*n
        for i in range(n):
            if i in fire:
                if i+1<n: new[i+1]+=1
            else:
                new[i]+=c[i]
        c=new
    assert c==[0]*n, (d,h,k,c)
    return out

def complex_faces(sets):
    f=set([0]); m=len(sets)
    for v in range(1,1<<m):
        xs=[sets[i] for i in range(m) if (v>>i)&1]
        if set.intersection(*map(set,xs)): f.add(v)
    return f

def rank_f2(columns):
    pivots={}
    for x in columns:
        while x:
            p=x.bit_length()-1
            if p not in pivots:
                pivots[p]=x; break
            x ^=pivots[p]
    return len(pivots)

def homology_f2(faces,m):
    bydim=defaultdict(list)
    for x in faces:
        if x: bydim[x.bit_count()-1].append(x)
    ranks={}; nfaces={i:len(v) for i,v in bydim.items()}
    for i in sorted(bydim):
        if i==0: ranks[i]=0; continue
        lo={x:j for j,x in enumerate(bydim[i-1])}
        cols=[]
        for x in bydim[i]:
            col=0
            for p in range(m):
                if x>>p&1: col ^=1 << lo[x^(1<<p)]
            cols.append(col)
        ranks[i]=rank_f2(cols)
    # reduced H_0: subtract one for nonempty complexes
    return {i:nfaces[i]-ranks[i]-ranks.get(i+1,0)-(1 if i==0 else 0) for i in nfaces if nfaces[i]-ranks[i]-ranks.get(i+1,0)-(1 if i==0 else 0)}

def expected(d,h):
    g=math.gcd(d,h); L=d//g
    q=(L+1)//3
    degree=d-g*q-2
    multiplicity=(2**g if L%3==0 else 1)
    return {degree:multiplicity}

def run():
    casecount=0; records=[]
    for d in range(3,12):
        for h in range(1,d):
            for k in (2,3):
                fs=firing_sets(d,h,k)
                # all later sets are subsumed by the initial period
                assert all(fs[t]<=fs[t-d] for t in range(d,len(fs)))
                fs0=fs[:d]
                actual=complex_faces(fs0)
                # independently construct cyclic complement-of-edge facet complex
                cyc=set([0])
                for mask in range(1,1<<d):
                    if any((mask & (1<<a))==0 and (mask & (1<<((a-h)%d)))==0 for a in range(d)):
                        cyc.add(mask)
                assert actual==cyc, (d,h,k)
                betti=homology_f2(actual,d)
                ex=expected(d,h)
                assert betti==ex, (d,h,k,betti,ex)
                casecount+=1
                if k==2:records.append((d,h,betti))
    general_count=0
    for d in range(3,9):
        for motif in range(1, 1<<d):
            r={j for j in range(d) if motif & (1<<j)}
            # exact shift dynamics of a repeated generic binary motif
            for k in (2,3):
                n=d*k
                c=[1 if i%d in r else 0 for i in range(n)]
                sets=[]
                for t in range(n):
                    sets.append({i for i in range(n) if c[i]==1})
                    c=[0]+c[:-1]
                assert all(sets[t] <= sets[t-d] for t in range(d,n))
                ns=complex_faces([frozenset(a) for a in sets[:d]])
                symbolic={0}
                for mask in range(1,1<<d):
                    if any(all((a-t)%d in r for t in range(d) if mask>>t&1) for a in range(d)):
                        symbolic.add(mask)
                assert ns==symbolic,(d,motif,k)
                general_count+=1
    print('PASS',casecount,'full simulated two-/three-period cases;',len(records),'distinct period/separation cases.')
    print('PASS',general_count,'generic binary motif/period cases (all nonempty motifs, periods 3 through 8).')
    print('Checks include support-subsumption, actual intersection nerve, Alexander-dual facets, mod-2 chain boundary ranks.')
    print('records_sha256',hashlib.sha256(json.dumps(records,separators=(',',':')).encode()).hexdigest())
    for d,h,b in records:
        if h==1 or h==d//2:
            print(f'd={d} h={h}: {b}')

if __name__=='__main__':run()
