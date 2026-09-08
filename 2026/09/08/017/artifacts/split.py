import sys, math, json
import mn
sys.path.insert(0, "output/artifacts")
from mn import *

def full_split_for_lambda(n, parts, T, li):
    fn=math.factorial(n)
    cs=[class_size(n,mu) for mu in parts]
    sq=[square_type(mu,n) for mu in parts]
    sqidx=[parts.index(t) for t in sq]
    idx1n=parts.index(tuple([1]*n))
    dimlam=T[li][idx1n]
    rows=[]
    for nu in range(len(parts)):
        g=sum(cs[k]*T[li][k]*T[li][k]*T[nu][k] for k in range(len(parts)))
        m=sum(cs[k]*T[li][sqidx[k]]*T[nu][k] for k in range(len(parts)))
        assert g%fn==0 and m%fn==0
        g//=fn; m//=fn
        s=(g+m)//2; a=(g-m)//2
        assert s+a==g and s-a==m and s>=0 and a>=0, (n,li,nu,g,m)
        rows.append((nu,g,m,s,a))
    dims=[T[i][idx1n] for i in range(len(parts))]
    tot_sym=sum(rows[nu][3]*dims[nu] for nu in range(len(parts)))
    tot_alt=sum(rows[nu][4]*dims[nu] for nu in range(len(parts)))
    assert tot_sym==dimlam*(dimlam+1)//2, (n,li,tot_sym,dimlam)
    assert tot_alt==dimlam*(dimlam-1)//2, (n,li,tot_alt,dimlam)
    return rows

if __name__=="__main__":
    out={}
    for n in [8,9,10,11,12]:
        mn._chi_cache.clear()
        parts,T=char_table(n)
        # self-check orth already done; recompute all lambda splits
        best=None  # (gap, li, nu, s, a, g)
        top=[]
        per_lam_best={}
        for li in range(len(parts)):
            rows=full_split_for_lambda(n,parts,T,li)
            for (nu,g,m,s,a) in rows:
                gap=abs(m)
                e=(gap,li,nu,g,m,s,a)
                if best is None or gap>best[0] or (gap==best[0] and (li,nu)<(best[1],best[2])):
                    best=e
                top.append(e)
            per_lam_best[li]=max(abs(r[2]) for r in rows)
        top_sorted=sorted(top, key=lambda e:(-e[0],e[1],e[2]))[:5]
        out[n]={"parts":[list(p) for p in parts],
                "max_gap":{"gap":best[0],"lam":list(parts[best[1]]),"nu":list(parts[best[2]]),
                           "g":best[3],"m":best[4],"s":best[5],"a":best[6]},
                "top5":[{"gap":e[0],"lam":list(parts[e[1]]),"nu":list(parts[e[2]]),
                         "g":e[3],"m":e[4],"s":e[5],"a":e[6]} for e in top_sorted]}
        print(f"n={n} maxgap={best[0]} lam={parts[best[1]]} nu={parts[best[2]]} g={best[3]} m={best[4]} s={best[5]} a={best[6]}", flush=True)
        for e in top_sorted:
            print(f"   gap={e[0]} lam={parts[e[1]]} nu={parts[e[2]]} s={e[5]} a={e[6]}", flush=True)
    json.dump(out, open("output/artifacts/gap_summary.json","w"), indent=1)
    # rho4 full table
    mn._chi_cache.clear()
    n=10
    parts,T=char_table(n)
    li=parts.index((4,3,2,1))
    rows=full_split_for_lambda(n,parts,T,li)
    table=[]
    for (nu,g,m,s,a) in rows:
        table.append({"nu":list(parts[nu]),"g":g,"m":m,"s":s,"a":a})
    json.dump({"lam":[4,3,2,1],"n":10,"rows":table}, open("output/artifacts/rho4_split.json","w"), indent=1)
    # positivity census for rho4
    sympos=sum(1 for r in table if r["s"]>0)
    altpos=sum(1 for r in table if r["a"]>0)
    both=sum(1 for r in table if r["s"]>0 and r["a"]>0)
    print(f"rho4: sym-pos {sympos}/42 alt-pos {altpos}/42 both {both}/42")
    # saxl containment: unsplit g>0 count
    print("rho4 unsplit positive:", sum(1 for r in table if r["g"]>0), "/42")
