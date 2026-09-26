# Independent audit — 2026/09/09/088

Date: 2026-09-26. Disposition: retain accepted, with a parameter transcription correction.

## Correctness — PASS for the certified chart solutions

The exact parameter file has group 3 (zero-indexed) (6/25,13/50,7/25,3/10), group 4 (1/25,4/25,11/25,3/5), and group 5 starting 61/100. These produce the claimed one nested interval overlap while all 32 parameter values are distinct. RESULT.md's parenthetical “i.e.” attaches group-3 fractions to group 4 and its group-number description is off by one; the committed file resolves the ambiguity. I independently rebuilt the eight rational determinant equations, reran the seed-777 solve, and found 14 separated chart roots, 12 nearly real plus a conjugate pair with imaginary coordinate magnitude ≈0.23003. I then generated fresh roots and reran exact-Fraction Krawczyk box tests: 12/12 real roots in B and 14/14 in A pass with radius 10⁻⁶ and nonzero real Jacobian determinants. The committed alpha_narrow_v2 certificate reports maxima 0.01177<0.157671 and nonzero exact Q(i) Jacobian tests for all 14 B centers; its code was inspected, but I did not re-execute that complex rational calculation. These support 14 simple separated roots and the reality drop in the affine chart. The record explicitly limits global chart-completeness; its 800–2000 random starts alone would not prove absence elsewhere.

## Originality — PASS

García-Puente et al., arXiv:1010.0665, already computed extensive Gr(2,6) real-solution statistics, but the consulted text does not specify this exact rational nested-overlap pair with rational-box certificates. The contribution is a concrete reproducible instance rather than the general secant conjecture.

## Scientific value — PASS

An explicit 14-real/12-real-plus-pair deformation illustrates why disjointness matters and provides test data for certified Schubert computations. The finite chart and conditional global scope are clearly marked.

Sources: https://arxiv.org/pdf/1010.0665 ; https://arxiv.org/abs/1406.0864 . Open preprints sufficed.
