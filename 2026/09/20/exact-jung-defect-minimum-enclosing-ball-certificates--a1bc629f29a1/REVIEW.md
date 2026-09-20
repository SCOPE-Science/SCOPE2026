# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The central identity is an exact algebraic consequence of the minimum
enclosing-ball optimality condition.

For an inclusion-minimal contact certificate
\(x_1,\ldots,x_m\) with positive barycentric weights \(\lambda_i\),
write \(q_i=x_i-c\). Since \(\|q_i\|=R\) and
\(\sum_i\lambda_iq_i=0\),
\[
R^2=\sum_{i<j}\lambda_i\lambda_j\|q_i-q_j\|^2.
\]
Combining this with
\[
\sum_{i<j}\lambda_i\lambda_j
=\frac12(1-\sum_i\lambda_i^2)
\]
and
\[
\sum_i\lambda_i^2
=\frac1m+\sum_i(\lambda_i-1/m)^2
\]
gives the displayed three-term Jung-defect decomposition exactly.
Each term is nonnegative because \(m\le n+1\) and every contact-edge
length is at most the global diameter.

The support-cardinality thresholds follow by retaining only the first
term. Their sharpness is witnessed by regular \((k-1)\)-simplices
embedded in \(\mathbb R^n\), which have
\(R^2/D^2=(k-1)/(2k)\).

Under the full-support threshold, the weight estimate follows from the
second term. For a deviation \(\delta_i=\lambda_i-1/(n+1)\) with
\(\sum_i\delta_i=0\),
\[
\sum_j\delta_j^2\ge \delta_i^2+\frac{\delta_i^2}{n},
\]
which yields the stated pointwise weight bound. The third term then
bounds each squared edge shortfall using
\(\lambda_i\lambda_j\ge a_n(\varepsilon)^2\).

For the volume corollary, the edge Gram matrix differs entrywise from
the regular-simplex Gram matrix by at most \(\eta D^2\). Hence the
operator-norm perturbation is at most \(n\eta D^2\). The regular Gram
matrix has eigenvalues \(D^2/2\) with multiplicity \(n-1\) and
\(D^2(n+1)/2\) once. Weyl's inequality and the determinant formula give
the claimed volume ratio when \(\eta<1/(2n)\).

The Rips--Cech interpretation uses explicitly defined scale
conventions, so no hidden factor-of-two convention is required.

## Originality — PASS (to the best of our knowledge)

The closest directly relevant ingredients were checked separately.

Jung's classical theorem supplies the sharp ambient radius/diameter
constant and regular-simplex equality case. Fischer--Gärtner--Kutz
record the standard minimum-enclosing-ball support-set criterion:
boundary points determine the ball exactly when its center lies in their
convex hull. Lim--McCann prove a sharp isodiametric variance theorem
whose equality case is the uniform measure on a regular simplex and use
it to reprove Jung's theorem. Finite Jung constants explicitly study
cardinality-dependent radius/diameter behavior, so the
\(m\)-point Jung constant itself is not new and is not claimed as such.

Schneider's stability paper treats different affine/Minkowski covering
inequalities and gives simplex-stability conclusions in that setting.
Vrahatis's 2024 survey records classical minimum-enclosing-ball and Jung
results and later generalizations. Rips--Cech literature records the
standard filtration comparisons. None of the checked sources stated the
exact decomposition into cardinality, weight-imbalance, and edge-slack
terms, nor the resulting combined sharp support thresholds and explicit
all-edge/weight estimates for a minimum-enclosing-ball certificate.

The weighted pairwise-variance identity underlying the calculation is
standard, and the proof is elementary. For that reason the principal
residual originality risk is an equivalent formula appearing under
different terminology in computational geometry, convex optimization,
or variance-inequality literature. The originality claim is therefore
strictly “to the best of our knowledge.”

## Value — PASS

The formula refines a one-number extremal inequality into a certificate
that diagnoses *why* a set falls short of the Euclidean Jung optimum.
It separates three independent mechanisms and immediately yields a
sharp hierarchy of active-support transitions. In the genuinely
near-extremal regime it forces a full \(n\)-simplex whose barycentric
weights and all pairwise edge lengths are quantitatively close to those
of the regular simplex.

This also gives a direct geometric reading of near-worst simplexwise
Rips--Cech birth ratios: the Cech birth must be controlled by a
full-dimensional near-regular minimum-enclosing-ball support face.

## Scientific limitations

1. The estimates constrain the active contact simplex, not every point
   of the original compact set.
2. The support-cardinality thresholds are sharp, but the per-edge and
   volume constants are not claimed optimal.
3. The Rips--Cech consequence is simplexwise and does not constitute a
   new global persistence-stability theorem.
4. The elementary nature of the identity leaves residual originality
   risk from differently phrased or unindexed sources.
