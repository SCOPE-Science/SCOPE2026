# Independent mathematical audit

## correctness

PASS

For crown Cr_n=K_{n,n} with matching ai-bi removed, n>=4, every selected vertex has required internal degree h=ceil((n-1)/2). Selecting index sets I,J on the two shores, a=|I|,b=|J|,c=|I∩J| gives internal degrees b-1_{i∈J} for ai and a-1_{j∈I} for bj. Thus feasibility exactly c=0 with a,b>=h or c>0 with a,b>=h+1. These selections induce connected graphs for n>=4 (complete bipartite or missing a matching with sufficiently large shore sizes). Enumerating disjoint residuals gives even n=2m polynomial Q_n(x)^2+C(n,m)x^(2m), where Q_n=Σ_{k=m+1}^n C(n,k)x^k; odd n=2m+1 polynomial Q_n(x)^2+(m+1)C(n,m)x^(2m)+2C(n,m)x^(2m+1). Minimum exponent is n even, n-1 odd, with coefficients C(n,n/2) and ((n+1)/2)C(n,(n-1)/2). Read actual artifacts/verify_strong_alliance_crown.py and wrote separate adjacency/connectivity enumeration for all 2^(2n) subsets n=4..8; coefficients and minimum counts matched. C6=n3 is correctly excluded, which has distinct connectivity boundary.

## originality

PASS

Carballosa et al. primary 2015/2016 strong alliance polynomial supplies complete bipartite K_n,m but not this matching-deleted crown, whose feasibility depends on overlap I∩J. Ibrahim 2018 bivariate defensive alliance polynomial is a genuine stronger invariant in principle; inspected its full article, including Prop.30 on complete bipartite graphs and graph-class table, and found no crown specialization. Resultary complete multipartite polynomial cannot simply be specialized because crown is not complete multipartite (for n>=3). Therefore best-of-knowledge novelty of the parity-sensitive all-coefficient crown enumerator survives, subject to possible older equivalent terminology.

## value

PASS

A perfect-matching deletion is a canonical minimal perturbation of K_n,n that profoundly changes alliance minima and counts, with opposite parity behavior and explicit all-cardinality polynomial. A complete classification of all strong defensive alliance subsets on this natural family is useful beyond a scalar domination number. It is not merely a known complete-bipartite substitution because the matching-index overlap matters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
