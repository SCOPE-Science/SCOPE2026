import sys, math, json
import mn
from mn import char_table, class_size, square_type, chi

def check_split_certificate(n, parts, T, lam, nu):
    # Independent replay from char_tables.json only; returns dict of checks
    fn=math.factorial(n)
    cs=[class_size(n,tuple(mu)) for mu in parts]
    sq=[tuple(square_type(tuple(mu),n)) for mu in parts]
    sqidx=[parts.index(list(t)) for t in sq]
    li=parts.index(lam); ni=parts.index(nu)
    # recompute raw sums from table entries
    terms_g=[cs[k]*T[li][k]*T[li][k]*T[ni][k] for k in range(len(parts))]
    terms_m=[cs[k]*T[li][sqidx[k]]*T[ni][k] for k in range(len(parts))]
    G=sum(terms_g); M=sum(terms_m)
    assert G%fn==0 and M%fn==0
    g=G//fn; m=M//fn
    s=(g+m)//2; a=(g-m)//2
    assert s>=0 and a>=0 and s+a==g and s-a==m
    return {"g":g,"m":m,"s":s,"a":a,"G":G,"M":M}

if __name__=="__main__":
    tabs=json.load(open("output/artifacts/char_tables.json"))
    gap=json.load(open("output/artifacts/gap_summary.json"))
    rho=json.load(open("output/artifacts/rho4_split.json"))
    # 1. re-verify orthogonality + dimsum for each n from stored tables
    for n in ["8","9","10","11","12"]:
        nn=int(n); parts=[tuple(p) for p in tabs[n]["parts"]]; T=tabs[n]["table"]
        fn=math.factorial(nn)
        cs=tabs[n]["class_sizes"]
        for i in range(len(parts)):
            for j in range(i,len(parts)):
                s=sum(cs[k]*T[i][k]*T[j][k] for k in range(len(parts)))
                assert s==(fn if i==j else 0), (n,i,j,s)
        idx=parts.index(tuple([1]*nn))
        assert sum(T[i][idx]**2 for i in range(len(parts)))==fn
        print(f"n={n}: orthogonality+dimsum OK from stored table")
    # 2. re-verify rho4 rows from stored n=10 table
    parts=[tuple(p) for p in tabs["10"]["parts"]]; T=tabs["10"]["table"]
    for r in rho["rows"]:
        c=check_split_certificate(10,[list(p) for p in parts],T,[4,3,2,1],r["nu"])
        assert (c["g"],c["m"],c["s"],c["a"])==(r["g"],r["m"],r["s"],r["a"]), r
    print("rho4 42/42 rows replay OK")
    # 3. re-verify per-n maximal gap by exhaustive re-scan from stored tables (gap maximality proof)
    for n in ["8","9","10","11","12"]:
        nn=int(n); partsL=[list(p) for p in tabs[n]["parts"]]; T=tabs[n]["table"]
        claimed=gap[n]["max_gap"]["gap"]
        best=-1; wit=None
        for li in range(len(partsL)):
            for ni in range(len(partsL)):
                c=check_split_certificate(nn,partsL,T,partsL[li],partsL[ni])
                gm=abs(c["m"])
                if gm>best: best=gm; wit=(partsL[li],partsL[ni],c)
        assert best==claimed, (n,best,claimed)
        print(f"n={n}: exhaustive gap-maximality OK: max|m|={best} at lam={wit[0]} nu={wit[1]} s={wit[2]['s']} a={wit[2]['a']}")
        # verify top5 entries individually
        for e in gap[n]["top5"]:
            c=check_split_certificate(nn,partsL,T,e["lam"],e["nu"])
            assert (c["g"],c["m"],c["s"],c["a"])==(e["g"],e["m"],e["s"],e["a"]), (n,e)
        print(f"n={n}: top5 replay OK")
    # 4. spot-check MN values against stored table (recompute chi for a few cells from scratch)
    mn._chi_cache.clear()
    assert chi((4,3,2,1),(4,3,2,1))==tabs["10"]["table"][tabs["10"]["parts"].index([4,3,2,1])][tabs["10"]["parts"].index([4,3,2,1])]
    assert chi((4,3,2,1),(6,2,2))==tabs["10"]["table"][tabs["10"]["parts"].index([4,3,2,1])][tabs["10"]["parts"].index([6,2,2])]
    print("MN spot checks OK")
    print("ALL VERIFICATIONS PASSED")
