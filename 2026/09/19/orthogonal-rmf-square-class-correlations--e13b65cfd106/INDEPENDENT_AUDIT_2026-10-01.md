# Independent audit — 2026-10-01

## Final claim

For every nontrivial irreducible orthogonal compact-group model, same-parity symmetric powers have a universal Hom-space overlap that yields the stated square-class covariance floor, square bias, x log x second-moment lower bound in dimension at least two, the exact one-dimensional square-class law, and the stated low-moment obstruction for q at least one-half.

## Correctness — PASS

The proof reconstructs from definitions. Orthogonal Frobenius--Schur type supplies a nonzero invariant quadratic tensor Q in Sym^2(V). Multiplication by Q is injective in the symmetric algebra, and compact-group complete reducibility gives Sym^j(V) as Sym^(j-2)(V) plus a complement of positive dimension for dim(V)>=2. Iterating yields at least floor(min(k,l)/2)+1 common nonzero summands for same-parity symmetric powers, hence the claimed Hom-space covariance floor. Prime independence then gives the tau(gcd(u,v)) square-class bound. Reindexing t=r a^2 is exact and gives the x log x + O(x) second-moment lower bound. In dimension one the parity covariance is exact. Invariant powers Q^a give nonnegative square means, and Jensen is used only where 2q>=1. The full source paper was checked: its Section 7 proves only the symmetric-square orthogonal example exactly, not this universal result.

## Originality — PASS

Best-of-knowledge originality passes. The directly relevant primary paper classifies orthogonal type as exactly the failure of the prime-square centering condition and computes the symmetric-square Sato--Tate model, but its full Section 7 does not state the universal same-parity Hom-space floor, square-class covariance lower bound, or all-orthogonal second-moment theorem.

### Equivalent formulations

Searches: Published-record semantic search for orthogonal compact-group random multiplicative functions and square-class covariance; Full-text inspection of arXiv:2609.20460v1, especially Section 7

Evidence: The exact semantic hit was the assigned finding; no distinct earlier published record with the universal theorem was returned. Leung Proposition 7.1 is the symmetric-square example only.

Reasoning: The relevant aliases are invariant quadratic tensor/Frobenius--Schur orthogonal type, same-parity symmetric-power overlap, squarefree-kernel covariance and square-class correlation.

### Broader coverage

Searches: Leung 2026 full text; Classical Fischer/harmonic decomposition searches

Evidence: Leung covers the centered unitary/symplectic theorem and one orthogonal example; classical decomposition supplies representation-theoretic ingredients, not the random-multiplicative global statement.

Reasoning: No inspected stronger theorem mechanically supplied the universal global covariance and moment lower bounds for arbitrary irreducible orthogonal compact-group models.

### Exact database or table

Searches: Semantic search for exact tau(gcd(u,v)) covariance and x log x all-orthogonal lower bound

Evidence: No distinct earlier exact database/table entry was located.

Reasoning: Search absence is treated only as best-of-knowledge evidence, not proof of novelty.

### Claim versus prior implication

Searches: Leung Section 7 Proposition 7.1 and compact-group discussion

Evidence: The source establishes E[h_2]=1 in orthogonal type and the exact symmetric-square example, but does not imply the stated universal Hom multiplicity lower bound without the additional invariant-tensor ladder argument.

Reasoning: The new final claim is not a stated corollary of the source theorem; it requires a separate representation-theoretic construction and global multiplicative reindexing.

### Source inspections

- **Low moments of automorphic random multiplicative function sums** — Highly relevant but not covering the universal theorem; it gives the orthogonal criterion and a symmetric-square example. Material read: Complete 19-page paper, including Section 7 and Proposition 7.1. Evidence: Section 7 states E[h_2]=1 for orthogonal type and Proposition 7.1 computes the symmetric-square model.

Checked sources: Sun-Kai Leung, Low moments of automorphic random multiplicative function sums, arXiv:2609.20460v1 (2026), full text inspected; Adam J. Harper, Moments of random multiplicative functions, I, Forum of Mathematics, Pi 8 (2020); Classical Frobenius--Schur trichotomy and complete reducibility for compact-group representations; Published-record semantic search for orthogonal compact-group RMF square-class correlations

Residual risks: The universal all-orthogonal lower bounds are best-of-knowledge; very recent or unindexed contemporaneous work may overlap. The theorem is a lower-bound mechanism, not a general asymptotic or a determination of moments below order one-half.

## Scientific value — PASS

The claim gives a structural mechanism for the entire orthogonal Frobenius--Schur class, rather than another isolated example. It explains why prime-square centering is necessary across a natural family, produces an explicit local-to-global square-class covariance floor, and covers all even symmetric-power Sato--Tate models. This is a motivated boundary theorem attached to a current low-moment result.

## Conclusion

The unchanged final claim passes correctness, originality and scientific value.
