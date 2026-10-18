# Scientific review: zeta function of the one-point Hermitian-relative class

## Correctness — PASS

The theorem quantifies over all primes \(p\), integers \(r\geq1\), coefficients \(\eta\in\mathbb F_{p^{2r}}\setminus\mathbb F_{p^r}\), and extension degrees \(n\geq1\). Smoothness and genus follow directly from the displayed derivatives and degree. The coordinate shift is checked symbolically by substitution; its \(q\)-Frobenius cocycle is the nonzero trace-zero element \(\eta-\eta^s\). The translation quotient has genus zero, and the norm-scaling automorphisms act transitively on all nontrivial characters; therefore their common cohomological multiplicity is \(s\). The Hermitian curve's maximal rational-point count forces eigenvalue \(-s\) on each first-cohomology eigenline. The twisted eigenvalue product and additive-character orthogonality then prove the displayed polynomial and every extension count. Exact small-field counts in `verify.py` agree, including characteristic two and non-prime \(s\). Their finite scope is not confused with an infinite proof.

## Originality — PASS (subject to literature risk)

Homma--Kim (2026, Theorem 7 / WCC Theorem 1.1) determine the one-point class, its explicit equation and the base-field count, but not the complete all-extension zeta polynomial. Their May 2026 projective-equivalence chapter classifies equivalence classes, according to its accessible abstract, not Frobenius spectra; the full chapter was not accessed. The earlier *Relatives of the Hermitian curve* does not establish the newly treated type's extension-count formula. The closest full-text zeta paper, Bouw--Ho--Malmskog--Scheidler--Srinivasan--Vincent (arXiv:1410.7031), computes related Artin--Schreier zeta functions over splitting fields but does not apply its displayed theorem to the nontrivial additive Hermitian twist. The general cohomological twist formalism itself is classical and is not claimed as new. Published-record semantic queries for the exact family, spectrum, twist, equivalent Artin--Schreier form, and characteristic-dependent extension counts returned unrelated records; those searches are overlap evidence only and are not regarded as a proof of novelty. No accessible preceding claim implies the full parameter-uniform polynomial. An inaccessible related chapter and unindexed general twist tables are residual risks.

## Value — PASS

The recent classification singles out the natural extreme \(N_q=1\) equivalence class without determining its arithmetic over extensions. The exact polynomial answers the natural next question completely for all square finite fields, all coefficients in the class, and all extension degrees. The trace-periodicity dichotomy and the order-\(p\) Hermitian descent are structural, not a random small-field computation or routine parameter renaming. No separate supersingularity or geometric-isomorphism discovery is claimed.

## Verification boundaries

The finite checker enumerates specified finite fields and tests independent point counts but does not enumerate all prime powers or prove the character-decomposition lemma. The proof supplies that missing infinite step. The Springer WAIFI chapter's full text was not available for a definitive whole-document negative-coverage conclusion. Independent validation is not claimed.

Self-review: passed. Independent audit: not yet performed.
