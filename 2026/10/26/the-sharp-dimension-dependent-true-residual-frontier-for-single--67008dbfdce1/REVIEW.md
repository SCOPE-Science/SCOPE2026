# Review of the exact DEIM one-row residual frontier

## Correctness — PASS

The proof proceeds from an exact decomposition of the sampled update, establishes \(p/a\le(\kappa-1)/(2\sqrt\kappa)\) by an SPD polynomial, and obtains the sharp finite branch using \(c\ge1/\sqrt n\). A unit rank-one perturbation attains equality. A continuously varying rank-one eigenvector makes the sampled scalar tend to zero without vanishing along the approximating sequence, proving the infinite branch. The exact two-dimensional witness and standalone finite checker were executed; finite tests support but do not replace the proof.

## Originality — PASS, with priority risk

The motivating full text (Bergermann, arXiv:2604.07158) defines the exact algorithm without this finite/infinite dimension-conditioned sharp true-residual formula. The random-embedding bounds of Nakatsukasa–Tropp rely on preserving a two-dimensional residual plane, impossible for one row in the nontrivial case; Güttel–Pearson stabilize by a different outer algorithm. A prior sharp sketched-GMRES true-residual result under a valid two-vector embedding is assumption-inapplicable here. Searches of related mathematical records yielded Kaczmarz, conventional GMRES and Gauss–Seidel results rather than the same theorem. A historical equivalent in interpolatory-oblique projection literature remains possible, and independent priority review has not occurred.

## Mathematical value — PASS

The exact, attained stability frontier separates regimes where single-row DEIM–GMRES must decrease the true residual from regimes where it can amplify it without any finite bound. The dimension dependence and the near-identity SPD blow-up furnish a concrete stability diagnostic for when oversampling or true-residual fallback is needed. The theorem is restricted to an exact-arithmetic one-step sketch without oversampling.

Self-review: passed. Independent audit: not yet performed.
