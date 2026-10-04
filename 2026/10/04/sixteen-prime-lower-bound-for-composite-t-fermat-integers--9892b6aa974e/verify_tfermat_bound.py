#!/usr/bin/env python3
import math, json, time

def primes_below(n):
    sieve=bytearray(b'\x01')*n
    if n>0:sieve[0]=0
    if n>1:sieve[1]=0
    for p in range(2,int(n**0.5)+1):
        if sieve[p]:
            sieve[p*p:n:p]=b'\x00'*(((n-1-p*p)//p)+1)
    return [p for p in range(2,n) if sieve[p]]

def v2(n):
    s=0
    while n%2==0:
        n//=2;s+=1
    return s

def factor(n):
    d=2; out=[]
    while d*d<=n:
        if n%d==0:
            e=0
            while n%d==0:n//=d;e+=1
            out.append((d,e))
        d=3 if d==2 else d+2
    if n>1: out.append((n,1))
    return out

_phi_cache={}
_fact_cache={}
def phi(n):
    if n not in _phi_cache:
        x=n
        for p,e in factor(n): x=x//p*(p-1)
        _phi_cache[n]=x
    return _phi_cache[n]

def order_mod(a,m):
    if math.gcd(a,m)!=1: return None
    o=phi(m)
    fs=_fact_cache.get(o)
    if fs is None:
        fs=[p for p,e in factor(o)]; _fact_cache[o]=fs
    for p in fs:
        while o%p==0 and pow(a,o//p,m)==1:
            o//=p
    return o

def compatible(p,q):
    op=order_mod(q,p-1)
    if op is None or op%2==0:return False
    oq=order_mod(p,q-1)
    return oq is not None and oq%2==1

def build_graph(prs):
    n=len(prs)
    adj=[set() for _ in range(n)]
    for i,p in enumerate(prs):
        for j in range(i+1,n):
            q=prs[j]
            if compatible(p,q):
                adj[i].add(j);adj[j].add(i)
    return adj

def k_cliques(prs,adj,k,stop_after=None):
    out=[]
    # ordered recursion; candidates are indices > last chosen
    def rec(chosen,cands):
        if len(chosen)==k:
            out.append(tuple(prs[i] for i in chosen))
            return stop_after is not None and len(out)>=stop_after
        need=k-len(chosen)
        if len(cands)<need:return False
        # degree-style ordering: try more constrained later? keep canonical increasing
        for pos,v in enumerate(cands):
            if len(cands)-pos<need: break
            tail=cands[pos+1:]
            nxt=[u for u in tail if u in adj[v]]
            if len(nxt)>=need-1:
                if rec(chosen+[v],nxt):return True
        return False
    rec([],list(range(len(prs))))
    return out

def korselt_remainders(prs):
    n=math.prod(prs)
    return {str(p):(n-1)%(p-1) for p in prs}

def main():
    allp=[p for p in primes_below(1<<15) if p%2]
    byv={}
    for p in allp:byv.setdefault(v2(p-1),[]).append(p)
    graphs={a:build_graph(g) for a,g in sorted(byv.items())}
    rows=[]
    total_kcliques=0
    for M in range(3,16):
        lim=1<<M
        found=[]
        vertex_counts={}
        edge_counts={}
        for a,gall in sorted(byv.items()):
            inds=[i for i,p in enumerate(gall) if p<lim]
            if len(inds)<M: continue
            # induced prefix because gall is increasing
            L=len(inds); g=gall[:L]; full=graphs[a]
            adj=[{j for j in full[i] if j<L} for i in range(L)]
            vertex_counts[str(a)]=L
            edge_counts[str(a)]=sum(len(x) for x in adj)//2
            cls=k_cliques(g,adj,M)
            found.extend(cls)
        total_kcliques += len(found)
        row={"M":M,"limit":lim,"vertex_counts_by_v2":vertex_counts,"edge_counts_by_v2":edge_counts,"compatible_M_cliques":found}
        if found:
            row["korselt_remainders"]=[korselt_remainders(c) for c in found]
        rows.append(row)
    assert all(len(r['compatible_M_cliques'])==0 for r in rows if r['M']<=14)
    r15=rows[-1]
    assert len(r15['compatible_M_cliques'])==1
    c15=r15['compatible_M_cliques'][0]
    rem=korselt_remainders(c15)
    assert any(v!=0 for v in rem.values())
    print('VERIFY_OK M=3..14_no_compatible_cliques M=15_unique_compatible_clique_not_Carmichael')
    print('M15_CLIQUE',' '.join(map(str,c15)))
    print('M15_KORSELT_WITNESS',next((p,r) for p,r in rem.items() if r))
    with open('/mnt/data/tfermat_bound_certificate.json','w',encoding='utf-8') as f:
        json.dump({"claim":"no composite T-Fermat integer has at most 15 prime factors","rows":rows},f,sort_keys=True,separators=(',',':'))
        f.write('\n')
if __name__=='__main__':main()
