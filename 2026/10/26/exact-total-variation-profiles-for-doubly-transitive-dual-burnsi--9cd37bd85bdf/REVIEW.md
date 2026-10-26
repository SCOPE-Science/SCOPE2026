# Mathematical review

## Correctness — PASS
The proof reconstructs the dual transition from the two conditional choices, uses the exact factorization \(Q=AB\), proves the doubly transitive primal walk has exactly two eigenvalues, and obtains an identity for every \(t\ge1\), not an approximation. The worst-start coefficient follows from a point-stabilizer support calculation plus Burnside's two-orbit identity. The nondegenerate parameter range, singleton-fixer assumption and two example families are checked. The standalone exact-rational verifier reports 8,370 successful checks over six small groups; no infinite-dimensional claim rests on finite enumeration.

## Originality — PASS, qualified
The general dual-chain factorization, spectral correspondence, stationarity and conjugacy quotient are already established in Feng's paper (arXiv:2510.25202, doi:10.1007/s10959-026-01539-9). The one-step conjugacy-class stationarity for transitive actions is itself a direct consequence of its orbit/conjugacy quotient factorization and is **not** claimed as new. What is not present in the inspected paper is the explicit all-times sharp worst-start total-variation law for general doubly transitive group actions, together with the exact natural symmetric/affine mixing factors and their asymptotic separation. The key extra work is recognizing the universal two-orbit stabilizer reduction and proving that a singleton-fixing element is an exact worst-case start. Published research-index checks identified no equivalent result. Residual risk: this compact specialization might exist in prior group-walk literature or be regarded as already covered by general spectral transfer results.

## Value — PASS
The result is a motivated exact classification of mixing behavior for a natural and broadly defined group-action Markov chain. The separation between uniformly fast symmetric groups and linearly slowing affine groups occurs while the conjugacy-class projection has already equilibrated. This makes the exact law useful for interpreting observables, selecting representative group actions, and identifying diagnostics that can miss slow mixing. Unlike a generic spectral bound, the theorem gives the actual worst-start total variation at every positive integer time.

## Independent verification and scientific limits
The finite verifier is supporting evidence only; full generality rests on the transparent group-theoretic derivation. The result does not characterize worst-case prefactors in every 2-transitive group without singleton fixers. It does not demonstrate broader sampling performance for arbitrary actions.

Self-review: passed. Independent audit: not yet performed.
