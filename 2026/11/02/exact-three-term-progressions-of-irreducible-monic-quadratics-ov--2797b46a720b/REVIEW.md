# Self-review

## Correctness — PASS
The statement concerns precisely odd prime powers and nonzero-slope affine steps. The map from the two quadratic coefficients to the first two discriminants is invertible because \(2u\ne0\); the third discriminant is their affine combination plus \(2u^2\). Quadratic irreducibility is equivalent to nonsquare discriminant. The proof evaluates the cubic quadratic-character correlation with the standard quadratic-sum identity, then subtracts the three discriminant-zero lines by weighted inclusion–exclusion, which is necessary since \(\chi(0)=0\). The resulting exact value is \((q-1)(q-3)/8\). Finite-field exhaustive verification passed 2322 affine steps for ten odd prime powers, including nonprime fields. The computation does not imply the universal claim; the proof does.

## Originality — PASS with residual risk
Bary-Soroker (arXiv:1206.3930, Theorem 1.1) counts this general type of irreducible polynomial tuple, but only up to an asymptotic error. The exact degree-two, three-linear-shift count and sharp existence cutoff are not implied by its stated estimate. The inspected 2015 consecutive-polynomial paper (arXiv:1509.01936, introduction and Section 5) counts growing-degree coefficient-prefix sequences rather than simultaneous translates of a fixed monic quadratic. Bender–Pollack (arXiv:0912.1702) treats asymptotic twin irreducibles, not exact three-term formulas. Published-result semantic comparisons and accessible prior claims revealed no dominating statement. The 2002 Effinger–Hicks–Mullen chapter remains inaccessible and represents a concrete risk of unlocated equivalent coverage. This is not a proof of uniqueness.

## Mathematical value — PASS
This is a complete natural three-prime-polynomial correlation, for every nonconstant affine step over every odd finite field. It computes the non-asymptotic term omitted by the general Hardy–Littlewood estimate, reveals exact uniformity in step coefficients, and gives the sharp existence cutoff, including the small-field obstruction at \(q=3\). Its object is arithmetically motivated by prime tuples rather than chosen as an arbitrary finite slice.

## Scientific scope and risks
Characteristic two collapses the third progression term to the first; constant shifts, nonlinear steps and four-term correlations are excluded. Unlocated historical coverage may reproduce the elementary character-sum identity or this specific formula. Independent validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
