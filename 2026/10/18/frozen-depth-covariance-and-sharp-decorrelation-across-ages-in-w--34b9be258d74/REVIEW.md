# Review of fixed-label depth dependence in weighted recursive trees

## Correctness: PASS

The result specifies positive deterministic weights, a fixed earlier label \(i\ge3\), independent parent choices and precisely which later labels and asymptotic regimes are covered. The marked generating-function recurrence gives an **exact joint-law** Bernoulli convolution, not merely matching first moments. The weighted-mean martingale difference expansion proves strictly positive, later-label-invariant covariance. Fourier inversion bounds the maximum of the convolution kernel, and the local central limit theorem for a sum of independent, nonidentical Bernoulli variables is justified by a characteristic-function expansion plus a uniform Gaussian bound. A bounded threshold test transfers nonzero covariance into a matching total-variation lower bound; an explicit shift coupling gives the upper bound. Summability of the Bernoulli probabilities implies convergence in total variation but not independence. These steps establish each regime analytically. The standalone Python test passed 120 exact-rational assertions for all applicable tagged-label pairs in four finite, heterogeneous seven-vertex models. Such finite checks support, but do not prove, the asymptotic theorem.

## Originality: PASS (qualified)

The motivating full text, Gałązka and Wdowicka, *Total Path Length in Power-Weight Recursive Trees* (arXiv:2610.00614v1), supplies the previously known one-vertex Bernoulli law and martingale innovations, and proves global path-length fluctuation results; it does not state the exact marked pair factorization, frozen *two-label* covariance or sharp total-variation rates. The full-text comparison with Lodewijks's joint vertex-depth study (arXiv:2204.09032) concerns a different regime of uniform recursive trees, particularly diverging marked labels, without the deterministic-weight fixed-old-label phase diagram. Relevant records about root degree versus leaves, root attachment versus total path length, and Cayley-tree endpoint degree versus distance concern different observables. None of the inspected statements directly dominates the present finding. The originality assessment remains qualified: antecedent ancestral-indicator representation and abstract smoothing results could make parts implicit in older work, and searches cannot prove uniqueness.

## Mathematical value: PASS

The motivating gap is precisely the dependence between early and late insertion costs, which one-vertex depth laws and global path-length variance do not determine. The result identifies a strict nonzero covariance at all separations while giving matching upper and lower dependence rates in the stronger total-variation topology. The sharp \(\alpha=-1\) transition separates disappearing dependence from a positive dependence limit. Its exact bivariate convolution provides a reusable formula for probabilities and moments, but the contribution is not merely the routine one-vertex generating-function recurrence: it includes a process-specific covariance invariant, a distribution-level phase diagram and a local-limit lower bound establishing rate optimality.

## Remaining risks and boundaries

This is a fixed-\(i\) theorem, not uniform in growing labels. The total-variation prefactor is bounded but not identified exactly. Arbitrary positive weight sequences with bounded Bernoulli variance are not exhaustively classified. An equivalent older formulation using weighted ancestors or generic Poisson-binomial smoothing remains possible; independent scholarly scrutiny is desirable.

Self-review: passed. Independent audit: not yet performed.
