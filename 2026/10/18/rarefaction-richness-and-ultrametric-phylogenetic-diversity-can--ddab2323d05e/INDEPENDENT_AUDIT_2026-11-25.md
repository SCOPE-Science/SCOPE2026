# Independent mathematical audit

## correctness

PASS

RESULT.md lines 28–42 handle the protected depths without an independence assumption: at 1 and N richness is constant; at 2 the distinct-species indicator changes PD from the fixed one-tip height H to at least H; at N-1 the singleton-omission indicator supports a nonnegative PD loss. In the remaining range the singleton clade is always hit. For the unique doubleton let X be its sample count, p_i=P(X=i). Conditioning on X=2 gives E[P_m|X=2]-E[P_m]=Hp_0-2ε(1-m/N); multiplying by -p_2 gives the covariance, since K_m=m-1_{X=2}. The hypergeometric p_0 and p_2 give the displayed formula, strict cutoff, common length ratio and N=5 witness -3/200. Binary refinement with positive, sufficiently short internal edges works by linearity/continuity and finitely many inequalities. Inspected the frozen verifier without executing it. Independently enumerated combinations(range(N),m) for N=5,6,8, every interior m and ε=1/32,1/8,3/4 at H=1: map labels 0 and 1 to the doubleton tip and each other label to its own tip, union the detected root paths, and compare exact rational E[KP]-E[K]E[P] with the formula. The sums agreed; this is only a finite cross-check.

## originality

PASS

Pass the all-depth universal-versus-attainable sign boundary and common counterexample with its exact length threshold, not the generic calculation of occupancy moments or the broader observation that some diversity indices can anticorrelate. The closest indexed result has a different diversity functional and opposite behavior at the two relevant depths of its five-individual witness. The contemporaneous publication dates do not determine priority.

## value

PASS

Richness and rooted diversity are natural joint statistics on the same rarefied set. The theorem identifies every protected depth, including the near-census depth, and uses a single abundance profile and tree to separate all other depths simultaneously. The sharp onset at N=5 and the positive-edge phase boundary give genuine constraints on when fixed-depth co-fluctuation can reverse; they are not claims about across-community correlations or a most-negative possible covariance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
