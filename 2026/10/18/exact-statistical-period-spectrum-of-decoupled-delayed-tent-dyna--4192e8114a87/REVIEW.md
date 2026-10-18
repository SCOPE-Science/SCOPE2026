# Scientific review: delayed-tent phase-period spectrum

## Correctness
PASS. The one-dimensional \(2^n\)-band exact-return property is an explicit published premise, not a new asserted lemma. The new proof derives the exact phase map \(R\), demonstrates component completeness using product exactness and the \(dp\)-th iterate, counts fixed phase cells for every iterate by summing carry increments, and applies Burnside and Möbius inversion. Domain, null-set convention, endpoints, and the distinction between the invariant stationary measure and a statistical density cycle are specified. The attached standard-library verifier exhausts 18 finite parameter pairs, with 230 fixed-point tests and four exact rational band-image checks.

## Originality
PASS, subject to independent historical priority checks. The closest primary Nakamura–Mackey work supplies the map and the classical scalar band law and reports visible regions at zero coupling, but does not give the affine-carry phase permutation and full all-delay ergodic period histogram. The related Losson–Mackey paper's zero-coupling map updates both coordinates simultaneously, rather than shifting one coordinate before tent iteration; its observations of product cycling do not by themselves yield the claimed delay-specific arithmetic. The number-theoretic counting tools are standard, so only the delayed-system exact classification is asserted as the contribution. A previously unindexed derivation or a general theorem with equivalent coverage remains a priority risk.

## Value
PASS. This is a natural and complete classification for the uncoupled slice of the delay model that motivated the source's statistical periodicity experiments. It separates three invariants previously liable to confusion: the number of visible band rectangles, the number of ergodic stationary sectors, and each sector's statistical period. It proves mixed periods in three-coordinate delay, and supplies an all-dimension exact finite formula without a numerical census assumption. The zero-coupling boundary is substantive but no stability under added coupling is claimed.

## Primary evidence and limits
Primary: Nakamura–Mackey, arXiv:2011.10689, Section 4, Eq. (28), Figure 1 and the quoted one-dimensional period windows. Prior one-dimensional input: Provatas–Mackey, Physica D 53 (1991), especially the spectral-period and band discussion. Related synchronous-coupling context: Losson–Mackey, Physica D 75 (1994), Section 3 and Appendix B. The phase-count calculation is new here, but the original source's numerical image alone cannot prove or disprove the ergodic-cycle count. The verifier certifies finite algebra only; the unbounded assertions rely on the written proof. Independent mathematical audit and definitive literature priority validation have not been performed.

Self-review: passed. Independent audit: not yet performed.
