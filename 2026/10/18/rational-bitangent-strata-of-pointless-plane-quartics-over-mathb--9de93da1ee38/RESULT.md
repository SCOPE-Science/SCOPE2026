# Rational-bitangent strata of pointless plane quartics over \(\mathbf F_7\)

## Finding
For a geometrically smooth plane quartic \(C/\mathbf F_7\) with no \(\mathbf F_7\)-rational point, define \(b(C)\) as the number of rational lines whose scheme-theoretic intersection divisor with \(C\) is even. There are precisely 32 isomorphism classes of such curves. Their complete distribution is

| \(b(C)\) | Isomorphism classes |
| :---: | ---: |
| 0 | 4 |
| 1 | 16 |
| 2 | 7 |
| 4 | 2 |
| 6 | 2 |
| 8 | 1 |

Thus \(b(C)\le 8\), and equality holds for a unique class, represented by
\[C_8:\quad X^4+4X^2Y^2+Y^4+(X^2+Y^2)Z^2+3Z^4=0.\]
Its eight rational bitangent lines \(aX+bY+cZ=0\), with \((a,b,c)\) normalized to first nonzero coordinate one, have normals
```
(1,1,1) (1,1,6) (1,2,0) (1,3,0)
(1,4,0) (1,5,0) (1,6,1) (1,6,6)
```

**The rational-bitangent count is not determined by either the Weil polynomial or the rational automorphism-group isomorphism type, even jointly.** The nonisomorphic curve
\[C_4:\quad X^4+Y^4+5(X^2+Y^2)Z^2+3Z^4=0\]
has only four rational bitangents, with normals
```
(1,1,2) (1,1,5) (1,6,2) (1,6,5)
```
but both curves have the same real Weil polynomial \(h(T)=T^3-8T^2+16T\), and the original classified catalog gives rational automorphism group \(D_4\) for each. Consequently their Jacobians are isogenous over \(\mathbf F_7\). The shared Weil numerator is
\[L_C(U)=(1+7U^2)(1-4U+7U^2)^2.\]

## Assumptions and scope
We work over the finite field \(\mathbf F_7\). A *rational bitangent* is a line defined over that field whose intersection with a smooth quartic over the algebraic closure is an effective divisor divisible by two. A fourth-order contact is included, although on a rational line of a pointless quartic the contact divisor is necessarily twice a closed point of degree two: an odd-degree closed point would imply a rational point only in the degree-one case, and a degree-four hypercontact point would give intersection degree at least eight. The 32 isomorphism-class representatives come from the explicit classified catalog of Faber--Grantham--Howe. We count lines, not ordered contact points, and isomorphism classes, not coefficient equations.

## Proof
**Exhaustive class coverage.** Faber--Grantham--Howe classify all 215 genus-three gonality-four (equivalently, pointless smooth plane quartic) classes over finite fields; the \(\mathbf F_7\) section of their original machine-readable catalog contains exactly 32 pairwise nonisomorphic forms. The complete 32-row polynomial input is reproduced as a short mathematical data table in `data/q7_models.txt`, with the original classification explicitly attributed. The scripts independently test rational pointless-ness and geometric smoothness of all 32 representatives.

**Algebraic bitangency criterion.** If \(L/\mathbf F_7\) is rational, choose independent \(A,B\in\mathbf F_7^3\) spanning its two-dimensional vector subspace and restrict the homogeneous quartic \(F\) to \(f(U,V)=F(UA+VB)\). As \(\operatorname{char}\mathbf F_7\ne2\), every geometric zero of \(f\) has even multiplicity if and only if \(f=\lambda Q^2\) for some \(\lambda\in\mathbf F_7^\times\) and binary quadratic \(Q\in\mathbf F_7[U,V]\). For sufficiency this is immediate. Conversely the even geometric factorization makes \(f\) a scalar square over the algebraic closure; uniqueness of its normalized square root and Galois invariance descend it over \(\mathbf F_7\) up to a field scalar. Thus it is enough to test the square criterion on each of the \(7^2+7+1=57\) rational lines.

**Finite exhaustive computation.** `code/q7_survey.py` enumerates all 57 projective line normals and all scalar-square binary quartic restrictions; evaluation at five distinct points \(U/V=0,1,2,3,4\) uniquely determines the restricted quartic since its degree is at most four. The program counts the 32 values and outputs the stated histogram. A separate implementation `code/q7_independent.py` restricts each form to all 57 lines in an independently constructed line basis; it factors the dehomogenized polynomial over \(\mathbf F_7\) and requires even exponents for all irreducible factors **and** even multiplicity at infinity. These logically equivalent, differently implemented tests agree on all 32 class counts and on the exact rational bitangent line lists. The latter program also computes Gröbner bases for the Jacobian ideal on all three projective affine charts; each is the unit ideal, excluding geometric singularities on every chart, including over extension fields.

**Coarse invariants fail to separate.** The two displayed \(D_4\)-labeled representatives occur as catalog rows 30 and 31. Their bitangent line lists above differ in size. Independently, `code/weil_pair_check.py` counts rational points on both curves over \(\mathbf F_7\), \(\mathbf F_{49}\), and \(\mathbf F_{343}\), obtaining respectively \((0,60,384)\) for each. For a genus-three curve, the first three extension point counts determine the numerator of its zeta function by Newton identities and the functional equation. The Frobenius power sums are \((8,-10,-40)\). The resulting real Weil polynomial is \(T^3-8T^2+16T=T(T-4)^2\), which yields exactly \(L_C(U)=(1+7U^2)(1-4U+7U^2)^2\). Tate's isogeny theorem gives isogenous Jacobians. The original catalog identifies the full rational automorphism group as \(D_4\) for both models; this group assignment is sourced to that catalog rather than recalculated from scratch.

## Verification
Run `python code/q7_survey.py`, `python code/q7_independent.py`, and `python code/weil_pair_check.py` from an unpacked copy of the accompanying files in any working directory with Python 3 and SymPy installed. The scripts find their input via paths relative to their own locations. Compare outputs to `data/survey_output.txt`, `data/independent_output.txt`, and `data/weil_output.txt` (SymPy may emit a harmless deprecation warning to standard error). Both bitangent implementations return the histogram \((4,16,7,2,2,1)\) for bitangent values \((0,1,2,4,6,8)\) and the independent Weil check returns \((0,60,384)\) for both specified models. Exact geometric-smoothness checks on all three charts are included in the factorization script, not inferred from rational smoothness.

## Relationship to prior work
Faber--Grantham--Howe prove and publicly provide the underlying 32-class \(\mathbf F_7\) input; neither their stated theorem nor the inspected catalog's stored invariants (real Weil polynomial and automorphism label) tabulates the rational-bitangent counts. These input classifications are not claimed as new. Bethea--Brazelton study group actions on the 28 geometric bitangents of symmetric quartics over the complex numbers. Such abstract group action data does not determine which geometric bitangents are fixed by finite-field Frobenius: the two curves above have the same rational abstract automorphism group but different rational-bitangent counts. Related classical odd-theta-characteristic theory establishes the significance of bitangents but not this exact 32-class Frobenius-fixed census. This result computes the arithmetic refinement, rather than a new abstract classification of plane quartics or their automorphism groups.

## Limitations
This is a classification for the fixed field \(\mathbf F_7\) and the 32 already classified pointless isomorphism classes; it is not a formula for other fields or all smooth quartics. The result does not reprove the published completeness and pairwise nonisomorphism of the external 32-class catalog, though every supplied model is checked directly for smoothness and rational-pointlessness. The automorphism labels are those verified in the source catalog, not independently enumerated. The count is exact conditional on the published class census and reproducible finite arithmetic. An unindexed earlier rational-bitangent table or a hidden implication of earlier arithmetic theta-characteristic classification remains a possible priority risk; searches cannot establish universal novelty. No independent expert audit has been performed.

## References
1. X. Faber, J. Grantham, and E. W. Howe, *On the Maximum Gonality of a Curve over a Finite Field*, arXiv:2207.14307, first submitted July 28, 2022. Full-paper claim and publicly released equations at https://arxiv.org/abs/2207.14307.
2. X. Faber, J. Grantham, and E. W. Howe, supplementary source `scripts/AllGenus3.magma`, original 2022 version, https://github.com/RationalPoint/excessive/blob/main/scripts/AllGenus3.magma. The \(q=7\) portion supplies the 32 exact equations and the original real-Weil/automorphism labels.
3. C. Bethea and T. Brazelton, *Bitangents to symmetric quartics*, arXiv:2410.09242, first submitted October 11, 2024, https://arxiv.org/abs/2410.09242.
