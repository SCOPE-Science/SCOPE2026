# Review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The proof reduces to identities and inequalities already available in the profile-measure proof of the bodies-of-revolution case, followed by standard information-theoretic identities.

For the centrally symmetric normalized body, Proposition 5.3 of Mielke-Sulz gives the lower bound by the diagonal multilinear profile functional. Because the reference transform is constant, the normalized diagonal ratio is exactly the \((n-1)\)-st moment of \(X_K\) under the probability weight proportional to \(t^n(1-t^2)^{-1/2}dt\). Equation (30) of that paper identifies the first moment of \(X_K\) with the normalized volume. Dividing therefore gives exactly the \((n-1)\)-st moment of the density \(Y_K=X_K/\mathbb EX_K\), which is the exponential of \((n-2)D_{n-1}\).

For general bodies of revolution, the normalized Blaschke symmetral satisfies \(\Pi K^{\mathrm B}=\Pi K\), so the factorization
\[
Q(K)=\bigl(V(K^{\mathrm B})/V(K)\bigr)^{n-1}Q(K^{\mathrm B})
\]
is exact. Rényi monotonicity, the identity \(D_2=\log(1+\mathrm{CV}^2)\), and Pinsker's inequality give the stated corollaries.

The cylinder check is independent of the abstract argument. Its profile measure is a single atom at 1, giving \(A_\rho(t)=2\kappa_{n-2}h/t\). Its brightness function is the support function of a Euclidean cylinder, so its projection-body volume is explicit. The resulting quotient agrees with the transformed \((n-1)\)-moment by beta-gamma identities. In dimension three the exact value is \(32/(3\pi^2)\).

No hidden regularity assumption is introduced: the profile-measure formulation used is specifically the nonsmooth extension and includes cylindrical boundary parts.

## Originality

**PASS, to the best of our knowledge.** The main source was inspected at the theorem, profile-measure, transform, Hölder, and equality-case statements. Its current v1 proves the qualitative inequality and equality characterization but does not state a quantitative deficit, Rényi/entropy formulation, variance bound, total-variation bound, or cylinder sharpness of the refined profile estimate. Direct full-text searches for “stability”, “deficit”, “variance”, “quantitative”, “entropy”, and “Rényi” in the current version returned no corresponding statement.

Targeted external searches combined Petty's conjecture with stability, deficit, coefficient of variation, relative entropy, Rényi divergence, and Hölder deficit. They did not locate an equivalent result. Saroglou's earlier work concerns lower bounds for the same quotient and an almost optimal high-dimensional estimate for bodies of revolution, not this quantitative profile-transform decomposition. Papers on the classical “Petty projection inequality” generally concern the distinct polar projection-body inequality and were not treated as coverage of this claim.

The public note by Felix Dorrek reports an independent proof of the same qualitative bodies-of-revolution theorem, but no technical quantitative proof of this refinement was available there. This remains a residual unpublished-overlap risk. The motivating preprint is very recent, so later revisions or unindexed parallel observations remain possible.

Current SCOPE records and recent commits were searched for Petty, projection-body, profile-measure, Rényi-divergence, and equivalent terminology; no overlapping finding was located before publication.

## Value

**PASS.** The result does more than append a small parameter improvement to the new qualitative theorem. It identifies a natural probability measure canonically encoded by the profile transform and converts the proof into an explicit information-theoretic stability statement. The logarithmic deficit separates two mechanisms that are conflated in the qualitative equality proof: failure of central symmetry and failure of the symmetric profile to be ellipsoidal.

The hierarchy provides immediately usable quantitative estimates in Rényi divergence, relative entropy, coefficient of variation, and total variation. The cylinder calculation shows that the strongest divergence refinement can be exact far from the ellipsoidal equality locus, so the refinement records genuine structure of the projection-volume functional rather than only a local Taylor expansion around the ball.

## Limitations

The controlled distance is a transformed one-dimensional profile distance, not a standard geometric distance between convex bodies. No explicit modulus for inverting the profile transform is proved. For nonsymmetric bodies, the Rényi term is attached to the Blaschke symmetral and does not by itself control the original asymmetry. The result is restricted to bodies of revolution and does not advance the unresolved general Petty conjecture beyond that class.
