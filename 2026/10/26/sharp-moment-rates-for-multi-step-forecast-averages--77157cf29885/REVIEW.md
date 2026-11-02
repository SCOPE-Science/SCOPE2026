# Independent mathematical audit

## correctness

PASS

D_{N,n}=Y_{N,n}-E[Y_{N,n}|F_{N,n-K_N}] is F_{N,n}-measurable and conditioned mean zero at lag K_N. For each residue r mod K_N, the terms D_{N,r+jK_N} are martingale differences along the subsequence filtration. Conditional Jensen gives uniform ||D||_p<=2M^(1/p), martingale p inequalities give O(m_r^(1/p)) for 1<p<=2 and O(m_r^(1/2)) for p>=2; Minkowski across K_N classes yields (K_N/N)^min(1-1/p,1/2). Clipping UI Y at B, applying bounded-variable result then taking N->infinity followed by B->infinity yields L1 convergence. For N=mK_N, shared independent block values X_j yield T_N=m^-1 sum X_j: sparse ±m^(1/p) with probability 1/m attain p<2 rate, Rademachers p>=2 rate, ±m sparse spikes contradict convergence with only first-moment bounds. Each construction can be checked analytically; no computation is invoked as an infinite proof.

## originality

PASS

Vovk arXiv:2508.17507 Theorem 1 requires uniformly bounded Y and §5 specifically raises removing that assumption. Vovk's residue-class method is credited. Classical Burkholder/Rosenthal p-moment inequalities give method but do not state the forecast-specific combined UI law and matching sharp p-regime examples in the inspected sources. Directly covered bounded result is excluded from novelty.

## value

PASS

The primary source itself identifies removal of boundedness as a useful open direction. Uniform integrability supplies a robust unbounded-variable LLN, while the optimal moment-dependent exponents and explicit heavy-tail boundary counterexample characterize a natural predictive sharpness threshold. This is a substantive quantified extension, even though standard martingale tools are used.

The dated certificate retains the supplied scientific assessment, sources and limitations.
