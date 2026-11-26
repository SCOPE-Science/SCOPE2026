# Independent mathematical audit

## correctness

PASS

The common continuous null gives a uniform word with m ones and n zeros. Reversal preserves R and negates Q=U−mn/2, giving E[Q]=Cov(R,Q)=0. For each adjacency condition T_i=1, one position in the pair is chosen symmetrically and the remaining m−1 positions form a uniform subset of the N−2 other positions. The two choices are independent. With a_j=j−(N+1)/2, their pair sum s_i=2i−N has sum of squares N(N−1)(N−2)/3. Applying the first and second subset-inclusion probabilities to the remaining rank sum gives the mean over i of E[Q²|T_i=1]−E[Q²] as −(mn−1)/6. Multiplying by (N−1)P(T_i=1)=2mn/N gives the claimed covariance. At N=2, R=2 and Q²=1/4 are constant; at N=3, the singleton at an end gives (R,Q²)=(2,1) twice and in the middle gives (3,0) once, yielding −2/9. The Gaussian-binomial expansion using log(sinh(x/2)/(x/2)) supplies κ₂ and κ₄, and Var(Q²)=κ₄+2κ₂². Combining with Var(R), the correlation is negative for mn>1, undefined at m=n=1, and has the stated proportional-sample asymptotic. Separate exact finite corroboration propagated counts of states (m,n,last symbol,runs,inversions): appending a 0 adds m inversions and appending either symbol adds one run exactly when different from the previous symbol or when starting. The resulting moments agreed through N=21 for all 210 sample-size pairs, including both degenerate boundaries. The frozen checker and recorded 818 comparisons were inspected, not executed; the analytic argument, not the finite bound, establishes the full domain.

## originality

PASS

The distinct finite mixed moment under the tie-free two-sample null is supported relative to earlier checked sources. The exact central identity also appears in a distinct later catalogue record. The sign-convention comparison establishes mathematical equivalence; its later displayed date and inspected prior-work section do not establish earlier coverage or independent discovery. Novelty is not assigned to either marginal law or to the reversal symmetry alone.

## value

PASS

The first-order covariance vanishes by reflection, but the squared statistic is a natural two-sided measure and gives a nonzero exact dependence with pooled runs for every nontrivial composition. The formula and distinct limits of standardized covariance and correlation identify a real feature of two canonical statistics that is not available from their exact marginals. It does not establish joint rejection probabilities, a combined-test guarantee, or dependence under ties or alternatives.

The dated certificate retains the supplied scientific assessment, sources and limitations.
