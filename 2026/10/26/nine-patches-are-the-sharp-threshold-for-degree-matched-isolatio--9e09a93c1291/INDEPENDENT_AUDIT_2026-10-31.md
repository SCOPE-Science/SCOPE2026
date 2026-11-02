# Independent mathematical audit

## correctness

PASS

PASS. For a fixed tree, indicator Y_v of a surviving vertex with no surviving neighbors satisfies E[Y_v]=p q^{d_v}; for nonadjacent distinct u,v, E[Y_u Y_v]=p² q^{d_u+d_v−1_{dist=2}}; adjacent pairs cannot both be isolates. Thus Var(I_T)=mu-mu²+2p²F_T(q). Identical degree multisets force the same mu, so variance ordering is exactly the sign of the polynomial F_T−F_H. Inspected explicit complete certificate and finite exhaustive algorithm: 1,1,2,3,6,11,23,47 unlabelled tree types for n=2..9; degree-matched pairs 0,0,0,0,1,5,23,96 and reversal pairs 0,0,0,0,0,0,0,3, with one identical-variance pair at n=9. Independently generated the unlabeled tree families and exact integer F-polynomials with SymPy rational Sturm interval root counts, confirming all counts and the witness F_T−F_H=−q(1−q)^2(2q²+2q−1). The resulting variance difference −2p^4(1−p)(2p²−6p+3) switches precisely at p=(3−sqrt(3))/2; independent 512-survival-state enumeration for the witness checks rational p=1/2 and 4/5. This is an exhaustive finite cutoff through 9, NOT a claim for all larger trees.

## originality

PASS

PASS, qualified best-of-knowledge. Standard site-percolation robustness and connected-cluster formulas do not give the fixed-tree degree-matched *variance ordering* or the minimum number of vertices at which it can reverse. Ecological connectivity literature motivates patch isolation but does not have this finite exact Sturm census. Semantically queried the published mathematical records for singleton-component variance and exact 9-tree first crossing; nearest returned results address other graph invariants. Could be an overlooked graph-reliability or percolation statistic formula under different terms; no priority guarantee.

## value

PASS

PASS. The object (number of isolated surviving patches) is a canonical singleton-component statistic in network reliability. Equal degree sequences force equal expected isolation while failing to determine risk dispersion. The sharp first order n=9 and exactly three crossing pairs give a natural and complete minimal counterexample classification, with an explicit probability threshold that demonstrates practical limits of mean/degree-only comparisons. Finite exact data is substantively motivated, not an arbitrary slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
