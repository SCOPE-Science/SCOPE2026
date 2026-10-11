# Same-model review

## Correctness
PASS. The proof works with the exact max-of-two-quadratics representation of the Banaś–Frączek norm, so no unjustified differentiation at the nonsmooth junction is needed. Equal active-branch choices cancel at first order. Mixed choices reduce to the sharp constrained maximization
\[
\max_{0\le t\le\lambda^{-1}}
\left((\lambda-\lambda^{-1})t+\sqrt{1-\lambda^{-2}}\sqrt{1-t^2}\right).
\]
Its unconstrained maximizer is \(t=\sqrt{1-\lambda^{-2}}\); this lies inside the allowed interval exactly for \(\lambda\le\sqrt2\). The resulting two exact branches give the lower derivative of \(\mathcal S_\lambda^2\), and strict mixed-branch unit vectors approaching the relevant boundary give matching upper asymptotics. Taking a square root yields the claimed derivative.

## Originality
PASS. The focal preprint computes this exact infimal invariant for the same plane only on \(\sqrt{1-\lambda^{-2}}\le\tau\le1\) and gives general parameter-Lipschitz bounds; it does not state the endpoint derivative at zero. The inspected 2016 Banaś–Frączek paper treats the classical James-type supremum at the symmetric parameter. A 2025 same-space paper treats a supremal Euler–Lagrange constant according to its abstract. Exact searches for the derivative, asymptotic expansion, source identifier, same-space aliases, and the \(\sqrt2\) transition did not locate an implication-equivalent statement. Residual risks from recent indexing and the inaccessible full text of the 2025 comparison are retained.

## Value
PASS. The result determines the natural first-order sensitivity at the endpoint omitted by the focal example and exposes a geometric phase transition at \(\lambda=\sqrt2\): below it the unconstrained mixed-branch optimum lies on the round arc, while above it the strip constraint becomes active. This is a structural boundary law for the new invariant, not a routine substitution or a tiny numerical improvement.

## Closest literature and limitations
The closest source is arXiv:2610.03050v1, especially Proposition 2.1 and Example 3.5. DOI:10.7153/jmi-10-43 is the older full-text same-space James-type comparison. DOI:10.1007/s12215-025-01277-7 is a recent same-space Euler–Lagrange comparison available only at abstract level here. The result is first-order only and does not determine the full small-skew profile or positive-skew minimizers.

Same-model review: passed. Independent audit: not yet performed.
