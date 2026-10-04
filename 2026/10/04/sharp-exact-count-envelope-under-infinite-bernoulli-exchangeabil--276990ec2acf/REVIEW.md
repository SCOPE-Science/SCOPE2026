# Review

## Correctness

PASS. De Finetti reduces the problem exactly to maximizing or minimizing
\[
\mathbb E f_{n,k}(P)
\]
over probability laws on \([0,1]\) with fixed mean. The proof identifies the
two tangent points by maximizing \(f(p)/p\) and \(f(p)/(1-p)\), proves
concavity on the central interval through the explicit second-derivative
quadratic, and proves minimality of the resulting concave majorant. The lower
envelope is exactly zero because the point-mass curve vanishes at both
endpoints. Explicit one- and two-atom directing measures attain every boundary
piece, and convex mixing fills the interval.

## Originality

PASS, with a residual older-mixture-literature risk. The full Misra--Singh--
Harner paper was inspected at its mixed-binomial definition and its equal-mean
Theorem 4.3. It proves variability and convex-order comparisons, not a sharp
single-cell probability envelope. The full Zaigraev--Kaniovski preprint was
inspected at its linear-programming formulation and main theorem; it treats
finite exchangeability and monotone at-least-\(k\) events.

The closest published semantic record on infinitely extendible Bernoulli
trials was read in full. It solves tail events by a one-moment concave-envelope
method. The point-mass curve has a different two-tangent geometry, and the
record does not state the breakpoints \((k-1)/(n-1)\) and \(k/(n-1)\), the
three-regime extremizer, or the complete interval for exactly \(k\) successes.

Targeted searches in binomial-mixture, exchangeability, exact-count,
point-mass, and fixed-mean terminology did not locate an equivalent theorem.

## Value

PASS. Exact-count probabilities are basic local concentration statistics for
exchangeable binary data and binomial mixtures. The theorem gives a complete
finite-sample classification, identifies precisely when iid sampling is
already extremal, and quantifies when latent heterogeneity can increase a
particular count probability. The explicit transition window has width
\(1/(n-1)\), so the phenomenon becomes increasingly localized as the sample
size grows.

Same-model review: passed. Independent audit: not yet performed.


Exact-rational replay: `VERIFY_OK tangent_checks=3422 majorant_checks=178770 concavity_checks=143370 construction_checks=357540 two_atom_checks=30030`.
