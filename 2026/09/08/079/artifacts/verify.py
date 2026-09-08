"""Independent verifier (stdlib only). Re-derives words from committed definitions,
computes EXACT distinct-factor counts per length via suffix array + LCP/Kasai,
checks each exact-min witness by EXACT string cover test, checks each greedy set
as a valid upper bound by exact test, and re-checks hash-group soundness
(within-group exact equality + merged-group count agreement with suffix array).
Usage: python3 verify.py  -> exits nonzero on any failure; writes verify.log."""
import json, sys

def rs_prefix(n):
    w=[]
    for i in range(n):
        c=bin(i).count('11') if False else 0
        b=bin(i)[2:]; c=0
        for k in range(len(b)-1):
            if b[k]=='1' and b[k+1]=='1': c^=1
        w.append(c)
    return w
def pf_prefix(n):
    w=[]
    for m in range(1,n+1):
        u=m
        while u%2==0: u//=2
        w.append(0 if u%4==1 else 1)
    return w

def suffix_array(s):
    n=len(s); sa=list(range(n)); r=list(s); tmp=[0]*n; k=1
    while True:
        sa.sort(key=lambda i:(r[i], r[i+k] if i+k<n else -1))
        tmp[sa[0]]=0
        for t in range(1,n):
            a,b=sa[t-1],sa[t]
            tmp[b]=tmp[a]+((r[a],r[a+k] if a+k<n else -1)!=(r[b],r[b+k] if b+k<n else -1))
        r=tmp[:]
        if r[sa[-1]]==n-1: break
        k*=2
    return sa
def lcp_kasai(s,sa):
    n=len(s); rank=[0]*n
    for i,a in enumerate(sa): rank[a]=i
    lcp=[0]*n; h=0
    for i in range(n):
        ri=rank[i]
        if ri==0: continue
        j=sa[ri-1]
        while i+h<n and j+h<n and s[i+h]==s[j+h]: h+=1
        lcp[ri]=h
        if h: h-=1
    return lcp
def exact_D_per_length(w):
    n=len(w); sa=suffix_array(w); lcp=lcp_kasai(w,sa)
    D={}
    for ell in range(1,n+1):
        cnt=0
        for t in range(n):
            if sa[t]+ell<=n and lcp[t]<ell: cnt+=1
        D[ell]=cnt
    return D

def exact_covers(w, gamma):
    """Exact cover check with real string comparisons (no hashing)."""
    n=len(w); g=set(gamma)
    seen={}  # factor tuple -> list of starts
    for i in range(n):
        for j in range(i+1,n+1):
            key=tuple(w[i:j])
            if key in seen: seen[key].append(i)
            else: seen[key]=[i]
    for key,S in seen.items():
        l=len(key); ok=False
        for s in S:
            # span s..s+l-1 hits g?
            for p in range(s,s+l):
                if p in g: ok=True; break
            if ok: break
        if not ok: return False, (key,S)
    return True, None

def hash_groups(w):
    n=len(w); B=9113823; M=(1<<64)-1
    H=[0]*(n+1); P=[1]*(n+1)
    for i,c in enumerate(w):
        H[i+1]=((H[i]*B)+(c+1))&M; P[i+1]=(P[i]*B)&M
    def h(i,j): return (H[j]-((H[i]*P[j-i])&M))&M
    table={}
    for i in range(n):
        for j in range(i+1,n+1):
            key=(h(i,j),j-i)
            table.setdefault(key,[]).append(i)
    return table

log=[]
def main():
    res=json.load(open('output/artifacts/results.json')); words=json.load(open('output/artifacts/words1024.json'))
    ok=True
    for which,f in [("RS",rs_prefix),("PF",pf_prefix)]:
        W=words[which+'1024']
        for n in [2,4,8,16,32,64,128,256,512,1024]:
            w=f(n)
            assert ''.join(map(str,w))==W[:n], f"{which}{n} word mismatch"
            D=exact_D_per_length(w)
            tot=sum(D.values())
            log.append(f"{which} n={n} exactTotalD={tot}")
            # hash-group soundness at every n
            hg=hash_groups(w)
            assert len(hg)==tot, f"{which}{n} hash-group count {len(hg)} != exact {tot}"
            # within-group exact-equality spot check (full check for n<=64; sampled for large n)
            cnt=0
            for (hh,ell),S in hg.items():
                if n<=64 or cnt%97==0:
                    base=tuple(w[S[0]:S[0]+ell])
                    for s in S[1:]:
                        assert tuple(w[s:s+ell])==base, f"{which}{n} hash collision"
                cnt+=1
            log.append(f"  hash sound: {len(hg)} groups == exact D; equality checked")
            # per-length LB from EXACT counts
            plb=max((D[ell]+ell-1)//ell for ell in D)
            log.append(f"  exact per-length LB={plb}")
            key=f"{which}{n}"
            if key in res["exact"]:
                e=res["exact"][key]
                assert e["D"]==tot, f"{key} D mismatch"
                c,_ev=exact_covers(w,e["witness"])
                assert c, f"{key} witness fails: {ev}"
                assert e["opt"]>=plb, f"{key} opt below LB"
                log.append(f"  EXACT opt={e['opt']} witness={e['witness']} cover=OK nodes={e['nodes']} proved={e['timeproved']}")
            if key in res["bounds"]:
                b=res["bounds"][key]
                assert b["D"]==tot
                c,ev=exact_covers(w,b["greedy_set"])
                assert c, f"{key} greedy set fails"
                log.append(f"  BOUND UB={b['greedyUB']} set cover=OK disjLB={b['disjointLB']}")
    open('output/artifacts/verify.log','w').write('\n'.join(log)+'\n')
    print('\n'.join(log))
    print("VERIFY ALL OK")

main()
