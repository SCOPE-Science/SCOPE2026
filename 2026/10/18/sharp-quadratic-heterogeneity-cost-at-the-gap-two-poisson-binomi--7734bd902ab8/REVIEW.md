# Scientific assessment

## Correctness: PASS

The theorem works with \(k\ge1\), \(m=k+d_k\), and the unique binomial boundary tie from Kleiner's Theorem 1 and Proposition 7 (arXiv:2610.10664v1, Sections 5–6). Those premises are verified in the primary full text, including the special failure of rigidity for \(k=0\). The coefficient of the product of two Bernoulli parameters is obtained directly from a generating polynomial. Fixing the pair sum converts it into an exact negative square, and the existing uniqueness theorem proves strict positivity of its coefficient. At the homogeneous point all off-diagonal second derivatives agree and all pure second derivatives vanish; imposing a zero-sum perturbation gives the claimed isotropic Hessian. Differentiating the exact binomial adjacent ratio verifies the positive mean derivative, so the implicit-function expansion and exact compensation coefficient follow. Factorial-ratio algebra independently verifies the closed coefficient formula. The staircase \(d_k\sim\sqrt{k/8}\) and a two-term square-root expansion show \(B_k\to4\), establishing the constant \(2\sqrt2\). The attached checker passes 438 high-precision arithmetic assertions. A numerical test does not replace the universal proof.

## Originality: PASS, qualified

The closest source, Kleiner (2026), proves the threshold and uniqueness, but does not give the exact full-range opposite-pair penalty, the constrained Hessian or the asymptotic compensation scale. Its qualitative rigidity is an essential prior premise and is explicitly credited rather than repackaged. Gnedin (2024), Section 7, optimizes the cost of *adding* independent Bernoulli increments to a fixed base law; it does not compute parameter-heterogeneity curvature about Kleiner's sharp all-active optimum. Classical Poisson–binomial and real-rooted-polynomial comparisons (Pitman, Hoeffding) could potentially encode a similar derivative, but no directly covering quantitative statement was verified. The published-claim database was queried with multiple equivalent terms, including two-point and heterogeneous-mean perturbations; the closest returned Bernoulli claim concerns cumulant effective-trial numbers, not the pairwise atom difference. Novelty is not proven by unsuccessful searches and is subject to unindexed-classical-literature risk.

## Value: PASS

The exact threshold describes where the direction of an inequality first changes but does not quantify the cost of unequal success probabilities. For practical Bernoulli arrays the coordinates are rarely identical; the complete finite pair identity measures the loss without small-parameter assumptions, while the isotropic Hessian gives an invariant local sensitivity for *every* fixed heterogeneity direction. The scale \(2\sqrt{2/k}\) quantifies the additional expected successes needed to recover the boundary tie at large levels and requires cancellation not visible from the qualitative uniqueness theorem. This is a motivated robustness question for a sharp extremal boundary, not an arbitrary sample of parameters. It does not claim a global variance-constrained optimizer or a new universal threshold.

## Relationship and risks

Exact prior anchor: I. Kleiner, arXiv:2610.10664v1, Theorem 1 and Proposition 7. Other inspected comparison: A. Gnedin, arXiv:2408.06477v1, Section 7. Relevant classical background: J. Pitman (1997), coefficient bounds for real-rooted polynomials; no exhaustive verification of that paper's complete text was obtained. Residual risks concern classical equivalent derivative statements and the reliance on the already published uniqueness theorem. No external independent check is implied.

Self-review: passed. Independent audit: not yet performed.
