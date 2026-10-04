# Review of Finite-corner Calderón commutators have no polynomial-in-order loss

## Correctness

PASS. Decomposing \(L^2(\mathbb R)\) by the finitely many affine intervals produces a finite operator matrix. A diagonal block is exactly a restricted Hilbert transform times the \(n\)-th power of the local slope, hence has norm at most \(\pi L^n\). An off-diagonal block has kernel bounded in modulus by \(L^n/|x-y|\). Since two distinct intervals are ordered, translating a point between them converts this positive majorant to a restriction of the Carleman kernel \((u+v)^{-1}\). The weighted Schur identity with weight \(u^{-1/2}\) gives norm \(\pi\). The \(N\times N\) block matrix therefore has norm at most \(\pi N L^n\). The principal-value issue occurs only on diagonal blocks, where it is precisely the standard Hilbert transform.

## Originality

PASS. The full recent primary source was inspected through its general linear-in-order theorem, its explicit discussion of whether that factor is sharp, the refined Dini and logarithmic-Besov estimates, and the bounded-variation inclusion. It contains no piecewise-affine or finite-corner decomposition theorem; searches within the full text returned no occurrence of “piecewise” or “tent”. Its current refined result only gives a \(\sqrt n\)-type factor for compactly supported bounded-variation profiles.

Targeted published-finding searches using piecewise-affine, piecewise-linear, finite-breakpoint, uniform-in-order, Carleman, and source-identifier formulations returned no implication-equivalent result. Web literature searches likewise returned general Calderón-commutator papers rather than the finite-corner bound.

The closest older reduction theorem of Muhly--Xia assumes derivatives in \(\mathrm{VMO}\). A piecewise-affine function with a genuine slope jump generally fails that assumption, so the theorem is specifically inapplicable to the main finite-corner case here. It also does not state a uniform-in-order quantitative bound for jump profiles.

## Value

PASS. The motivating paper explicitly identifies polynomial dependence on the commutator order as an unresolved sharpness issue and observes that existing examples fail to exhibit such growth. The finding rules out an entire natural candidate class: no fixed polygonal Lipschitz profile can witness even a square-root polynomial factor. This gives a concrete structural obstruction and shows that any eventual polynomial-growth mechanism must use slope geometry of unbounded complexity rather than finitely many corners.

Same-model review: passed. Independent audit: not yet performed.
