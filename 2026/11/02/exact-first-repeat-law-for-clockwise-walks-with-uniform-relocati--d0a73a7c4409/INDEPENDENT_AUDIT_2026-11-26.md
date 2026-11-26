# Independent mathematical audit

## correctness

PASS

Condition on the ordered pattern of the first t transition types, not on the positions. Its k relocations generate k independent uniform starts for k+1 labelled clockwise arcs totaling t+1 sites, with the first arc anchored. For t<n, disjoint placements are in bijection with the k! orders of the other labels and weak compositions of the n-t-1 unused sites over k+1 gaps; this gives the proposed rising factorial, independent of the arc lengths. The ratio for k to k+1 is (n-t+k)/n<1 for k<t; monotone coupling of the binomial counts gives strictness for t>=1, including comparison with q=0 and q=1. For t=n the pigeonhole bound applies, not the arc count. For t=floor(nx) and finite nq, tight binomial-to-Poisson mixing yields exp(-lambda x^2) for x<1, including lambda=0. For t=n-1 the conditional factor is k!/n^k, so the mass at T=n tends to exp(-lambda). Support in [0,1] justifies convergence of the mean in this window. On t=floor(x sqrt(n/q)), x>0 and nq diverging, K/(tq) tends to one and t/n tends to zero. Summing log(1-(t-j)/n) over 0<=j<K gives -Kt/n+K(K-1)/(2n) with error O(K t^2/n^2)=o_P(1). The two terms tend to -x^2 and q_infty x^2/2, including the q_infty=0 and 1 regimes. The conditional survival factors are bounded by one, permitting averaging. x=0 is exact. This is an analytical proof; VERIFICATION.md's recorded 438 finite comparisons from checker.py were inspected as supporting evidence, not rerun or used as the limit proof. No expectation convergence in the many-relocation window is asserted.

## originality

PASS

The scoped contribution is the exact first-repeat law for this directed walk, including the coupling of the relocation probability to the endpoint atom and the Rayleigh coefficient, not the classical arc placement count, the birthday scale, or first-passage analysis in general.

## value

PASS

First repetition measures how much of the cycle is explored without a collision. The exact finite law and its two scaling limits distinguish the survival of a full traversal with positive limiting probability from the birthday-scale cutoff. The atom and the continuous interpolation of the many-relocation coefficient are quantitative information beyond a collision-order estimate or either deterministic/independent endpoint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
