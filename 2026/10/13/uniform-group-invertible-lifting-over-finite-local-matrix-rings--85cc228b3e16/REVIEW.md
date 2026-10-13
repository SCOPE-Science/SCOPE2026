# Self-review

## Correctness
**PASS.** For a group-invertible matrix \(A\), the idempotent \(e=AA^\#=A^\#A\) identifies \(\operatorname{im}A=\operatorname{im}e\) and \(\ker A=\ker e\), so \(R^n\) splits as image plus kernel and \(A\) is invertible on its image. Conversely every automorphism on one summand, extended by zero on a complementary summand, is group invertible. Over a commutative local ring the summands are free. Orbit-stabilizer gives \(|\operatorname{GL}_n(R)|/|\operatorname{GL}_{n-r}(R)|\), and reduction modulo the maximal ideal gives the residue-field formula. The fixed-residue fiber count follows by separately lifting the ordered decomposition and invertible restriction. Exhaustive direct checks over \(\mathbb Z/4\mathbb Z\) and \(\mathbb F_2[\varepsilon]/(\varepsilon^2)\) verify all \(2\times2\) cases from the defining group-inverse equations.

## Originality
**PASS.** The 2013 block-matrix paper gives group-inverse existence and formulas for particular block forms over rings, not a full-matrix finite-local enumeration. The 2022 dual-number paper gives an existence criterion for dual matrices; its square-zero specialization is consistent with one case of the lift theorem but does not cover arbitrary finite local rings or state the uniform fiber law. The 2021 finite-ring enumeration concerns idempotents, not group-invertible matrices. Targeted database searches under group-inverse, finite-local-ring, lift, nullity, residue-field, and exact-count formulations found no statement implying the displayed spectrum. The remaining risk is an older result indexed under semigroup terminology rather than generalized-inverse terminology.

## Value
**PASS.** Group invertibility is the Drazin-index-one stratum and is a natural singular analogue of invertibility. The result gives a complete rank-by-rank census over every finite commutative local ring and, more structurally, an exact lifting probability controlled only by residue nullity. Nonisomorphic local rings with the same residue-field and radical sizes therefore have identical group-invertible matrix spectra, a universality phenomenon rather than a one-off small-ring count.

The closest literature concerns qualitative group-inverse criteria, dual-number existence conditions, and finite-local idempotent counts. The theorem does not address nonlocal rank vectors or higher Drazin index.

Self-review: passed. Independent audit: not yet performed.
