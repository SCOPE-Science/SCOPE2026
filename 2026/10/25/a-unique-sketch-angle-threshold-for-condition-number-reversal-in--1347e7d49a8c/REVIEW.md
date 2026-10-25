# Scientific review

## Correctness — PASS
The proof uses the rank-two projector representation \(H=A^{1/2}\Pi A^{1/2}\), rotates the repeated eigenspace to identify the complete one-parameter sketch family, and calculates the exact positive generalized eigenvalues. The strictly monotone comparison function \(r+2+r^{-1}\) converts condition-number comparison into a cubic sign test. Its transformed cubic has a unique positive root since it is initially negative and strictly convex with eventually positive derivative. The symbolic checker verifies the exact rational identities, the finite example, and the asymptotic limit, and independent direct Nyström/sketched generalized eigensolves agree across 500 random inputs. No finite experiment is treated as a proof of the universal signs.

## Originality — PASS, subject to publication priority
Frangella–Tropp–Udell (arXiv:2110.02820, §§1.1, 2.1, 5.1–5.2) define this normalized preconditioner and establish a large-sketch expected condition-number bound and exact-eigenspace optimality, not a rank-two per-sketch comparison with the unpreconditioned condition number. Daužickaitė–Lawless–Scott (doi:10.1002/qj.4151, §§3, 4, 5.1) report loss of lower spectral nonexpansiveness for a different randomized limited-memory preconditioner, without the exact threshold for this normalization. Dereziński–Musco–Yang (arXiv:2405.05865) employ a different multilevel preconditioner; its abstract was inspected, but full text was not accessible in this comparison. Targeted published-literature and mathematical-result searches did not surface an exact equivalent or broader theorem with this implication. An unobserved equivalent small-dimensional preconditioning calculation remains possible.

## Mathematical value — PASS
Whether preconditioning is guaranteed to reduce a condition number is a natural safety question for PCG. Here the exact crossover divides all possible two-column sketches on a natural SPD spike family; failure has positive probability for every spike and every regularization. The smallest dimension is identified, an exact rational deterioration certificate is supplied, and an asymptotic family gives a concrete \(32/27\) relative deterioration. These are stronger than a one-off numerical failure or a routine normalization observation. The theorem does not claim a corresponding iteration-count increase, a global deterioration maximum, or a failure of the original large-sketch expected bound.

## Closest literature and limitations
The closest identical algorithm is arXiv:2110.02820; nearby random-spectral limited-memory and multilevel methods use different preconditioner matrices. Exact arithmetic, a three-state diagonal spike and rank-two sketches are assumed. Priority remains subject to independent literature review, and the finite-precision stabilization used in implementations is outside the theorem.

Self-review: passed. Independent audit: not yet performed.
