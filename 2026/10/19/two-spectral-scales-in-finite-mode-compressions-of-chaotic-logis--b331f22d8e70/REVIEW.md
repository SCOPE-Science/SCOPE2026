# Scientific review

## Correctness — PASS

The scalar conjugacy \(f^{\circ n}((1-\cos\theta)/2)=(1-\cos(2^n\theta))/2\) is exact, including endpoints. Integration by parts with an even cosine frequency yields the endpoint expansion (1); the remainder follows from the Riemann–Lebesgue lemma and the stipulated smoothness. The matrix leading term is a sum of two endpoint-evaluation outer products. For the secondary scale, the block expansion (5) is checked using values and first derivatives of products of endpoint-null polynomials. The Schur complement subtracts \(9/16\) from the direct \(15/8\), leaving \(21/16\); the derivative-evaluation rank is \(\min(2,d-1)\). A finite determinant/root analysis gives precisely the stated two eigenvalue scales without supposing positivity of all remaining eigenvalues. The included standalone program performs 115 exact-rational checks using independent integration constructions. Finite checks are supplemental, not a substitute for the analytical proof.

## Originality — PASS

The closest inspected source is Janowicz and Orłowski, arXiv:2607.19159v1, Section 4.2, Theorem 2. Its exact Chebyshev-moment expression determines each fixed Legendre matrix entry, and its proved estimate is \(O(4^{-n})\) at fixed indices. Those ingredients are acknowledged as already established. The present claim is more specific and structurally distinct: all-smooth-test endpoint asymptotics and a two-tier eigenvalue limit for every fixed finite-dimensional compression. In particular, the secondary eigenvalue scale \(64^{-n}\), its exact multiplicity, the coefficient \(21/16\), and the \(d=2\) coefficient \(315/4\) do not appear in the inspected source. The classical angle-doubling conjugacy is also acknowledged. Exact-entry information permits derivation of these consequences, so the result is a refinement, not an independent dynamical mechanism. An equivalent spectral extraction in unindexed literature remains a priority risk.

## Mathematical value — PASS

The source's fixed-entry decay estimate does not distinguish eigenvalue scales. The rank-two leading limit might suggest all other modes are merely of smaller, unspecified order; the proved Schur cancellation shows that those modes first appear two full powers of the squared frequency later, and determines their multiplicities and coefficients. This is a structural asymptotic classification of natural finite Galerkin sections of a classical chaotic observable. The derivative-jet formulation also explains how mode cancellation produces spectral scale separation and allows sharp finite-order predictions. This is not a claim of operator-norm convergence or a new logistic-map conjugacy.

## Closest literature and limitations

Janowicz–Orłowski's Theorem 2 (arXiv:2607.19159v1) is closest; its entire relevant Section 4.2, theorem, derivation, and stated restrictions were inspected in the publicly accessible manuscript text. MathWorld's account of the logistic map at parameter four supplies the classical conjugacy. Theorems here concern fixed finite cutoffs, not any growing-dimensional regime, not projected nonlinear dynamics, and not operator-norm convergence. Independent priority and scientific validation have not been performed.

Self-review: passed. Independent audit: not yet performed.
