# Self-review

## Correctness — PASS
The integer matrix is exactly Higgins's multiplicity-counted deletion matrix. With monomials orthonormal, differentiation gives the deletion matrix and its transpose is the raising map. The commutator \(DU-UD=(2k+m)I\) is checked monomial-by-monomial, implies raising injectivity, and produces harmonic spaces of the claimed binomial dimensions. Its eigenvalue calculation proves all ranks, including the separate one-dimensional top-rank endpoint. The finite verifier checked 54 matrices for all ranks through \(n=10\); numeric eigenvalue checks supplement, not prove, the identity.

## Originality — PASS, qualified
Higgins (2026, Definition 3.4, Lemma 3.5, Corollary 3.7) gives the weighting and its constant margins but not the remaining singular spectrum or exact condition numbers. Fomin (1994) supplies general graded up/down-operator methods, not an identified exact solution for this semigroup-specific matrix. Searches included weak-composition lowering, multiset deletion, symmetric powers, and exact eigenvalue forms; no specific covering claim was found in accessible material. **Risk:** a broader classical representation-theoretic spectral result may implicitly imply the theorem; Fomin's full article was not exhaustively inspected. This is an originality judgement with residual risk, not absolute priority proof.

## Mathematical value — PASS
The exact finite-rank spectral invariant is motivated directly by a new canonical balanced weighting at the heart of the order-preserving-transformation matching construction. Constant margins determine only the top singular mode. The theorem determines every remaining singular mode, their multiplicities, full row rank and the exact sharp conditioning across all semigroup ranks. This is an all-parameter structural evaluation of a natural matrix, not an arbitrary cutoff or table recomputation.

## Limits
The claim does not concern the unweighted incidence matrix, arbitrary semigroups, construction of a particular matching, or independent validation. Residual older-literature priority risk is acknowledged.

Self-review: passed. Independent audit: not yet performed.
