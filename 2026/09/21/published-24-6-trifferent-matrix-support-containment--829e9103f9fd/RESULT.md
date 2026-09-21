# A support-containment obstruction in the published length-24 ternary trifferent-code witness

## Claim

Bishnoi, D'haeseleer, Gijswijt and Potukuchi (2024) print a `6 x 24` matrix over `F_3` in the proof of their Theorem 1.7 and state that its row space is a `[24,6]_3` trifferent code. The displayed matrix has rank 6, but its row space is **not** trifferent (equivalently, it is not a minimal ternary linear code).

A short exact certificate is obtained from two row combinations. Number the printed rows `r_1,...,r_6` and define

`a = r_2 + r_3`,  `b = r_1 + r_4`  over `F_3`.

For the matrix printed in the paper,

`a = 100112202000102002022001`,

`b = 211221201011101002221122`.

Their supports, with coordinates numbered from 1 to 24, are

`Supp(a) = {1,4,5,6,7,9,13,15,18,20,21,24}`,

`Supp(b) = {1,2,3,4,5,6,7,9,11,12,13,15,18,19,20,21,22,23,24}`.

Hence

`Supp(a) ⊊ Supp(b)`.

This already contradicts minimality. It also gives a direct trifference failure that does not depend on the minimal-code equivalence: the three distinct codewords `a`, `b`, and `-a` have no coordinate containing all three symbols `0,1,2`. If `a_i=0`, then also `(-a)_i=0`; if `a_i!=0`, strict support containment implies `b_i!=0`, while `{a_i,-a_i}={1,2}`. Thus every coordinate of the triple uses at most two symbols.

The matrix does have rank 6: the determinant of its first six columns is `2 mod 3`.

## Consequence for the published construction

The proof of Theorem 1.7 in the published article takes this displayed matrix as the inner `[24,6]_3` trifferent code and then applies concatenation to obtain the stated explicit asymptotic construction. The displayed matrix therefore cannot certify that concatenation argument as written.

This observation **does not** prove that no `[24,6]_3` trifferent code exists, nor that the existence statement of Theorem 1.7 is false. The same paper reports the numerical range `22 <= b_3^*(6,1) <= 24`, and a different or corrected length-24 witness could in principle restore the argument. The result here is specifically a reproducible obstruction to the matrix that is publicly printed and used in the proof.

For context, arXiv versions v1 and v2 gave a weaker explicit rate based on a general strong-blocking-set construction; the final v3/journal version strengthened the explicit rate using the displayed `[24,6]_3` inner code. A later 2026 paper on explicit strong blocking sets cites the 2024 equivalence but does not supply a correction of this particular matrix or the length-24 witness.

## Reproducibility

`artifacts/verify_matrix.py` contains the six printed rows, performs exact arithmetic modulo 3, verifies rank 6 from a nonzero minor, computes the two certificate codewords, checks strict support containment, and checks directly that `(a,b,-a)` has no trifferent coordinate. `artifacts/verification_output.txt` records the verified output.

## References

1. A. Bishnoi, J. D'haeseleer, D. Gijswijt, A. Potukuchi, *Blocking sets, minimal codes and trifferent codes*, Journal of the London Mathematical Society 109(6), e12938 (2024), https://doi.org/10.1112/jlms.12938.
2. A. Bishnoi, J. D'haeseleer, D. Gijswijt, A. Potukuchi, arXiv:2301.09457v1 (2023), https://arxiv.org/abs/2301.09457v1.
3. A. Bishnoi, J. D'haeseleer, D. Gijswijt, A. Potukuchi, arXiv:2301.09457v3 (2024), https://arxiv.org/abs/2301.09457v3.
4. A. Bishnoi, I. Tomon, *Explicit Constructions of Optimal Blocking Sets and Minimal Codes*, Combinatorica 46, 13 (2026), https://doi.org/10.1007/s00493-026-00202-5.
