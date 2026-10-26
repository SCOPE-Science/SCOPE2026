# Scientific review: universal torus saturation of rational Nevanlinna extremals

## Correctness — PASS

The claim uses the exact extreme-point family proved in Fagrell–Luger, Theorem 3.1. The new projective calculation is independent: for coprime binary forms \(A,B\) of degree \(m\), the reduced forms are \(P=-AW_0W_1\) and \(Q=A(W_1^2-W_0^2)+BW_0W_1\). They share precisely two projective points over each simple real pole of \(\varphi=B/A\). Local implicit-function expansions at both points show intersection multiplicity two. The formal quadratic Sylvester determinant equals \(-A^4\); an executable SymPy calculation confirms this exact identity. Coordinatewise Cayley transformations and invertible combinations of \(P,Q\) preserve common-zero schemes. A separate normalization removes the real constant \(\operatorname{Re}h(i,i)\) before passing to the bidisk, so no zero-real-part assumption is needed. The resulting rational-inner numerator and denominator are coprime and have bidegree \((m,2)\). The theorem counts the entire projective base locus, not only observed finite affine intersections.

## Originality — PASS (self-review; priority risk remains)

Knese, *Extreme points and saturated polynomials* (arXiv:1703.00094), defines saturation, proves the saturated-plus-irreducible sufficient condition, and conjectures both conditions necessary for normalized rational extremals. Fagrell and Luger, *Real rational Herglotz-Nevanlinna functions in two variables and a class of extremals* (arXiv:2610.02476v1), establish this entire extremal family and exhibit saturation for one special degree-two example, but their Sections 4.1–4.2 concentrate on reducibility and do not prove a general saturation law. The new statement proves saturation for all rational inputs, whether reducible or irreducible, supplies exact pole-indexed intersection multiplicities, and identifies the universal projective resultant. Targeted published mathematical-index searches for these objects and their equivalent pole/resultant formulations found no dominating assertion. Since an algebraic-geometric argument may have appeared in unindexed work, historical priority remains subject to external confirmation.

## Value — PASS

The claim establishes a full-family case of the still-relevant saturation component of Knese's proposed necessary conditions, including infinitely many counterexamples to its *other* (irreducibility) component. It determines the precise boundary-zero divisor of a natural extremal family and shows that the divisor depends only on one-variable pole locations, not on their residues or regular part. The universal saturation property is meaningful beyond an isolated example, and the exact multiplicity structure makes the result useful in stability, intersection, and rational-inner realization questions. It does not resolve the general necessary-condition conjecture.

## Closest sources and scientific limitations

Primary literature examined: Fagrell–Luger (2026), Theorem 3.1 and Sections 4.1–4.2; Knese (2017 preprint, 2019 publication), Definition 1.4, Theorem 1.5, Conjecture 1.7. Supporting pole structure follows the standard one-variable rational Nevanlinna representation. Residual risks are unindexed priority overlap and the possibility of general algebraic-geometry formulations implying the projective resultant without expressly treating these extreme functions. No independent mathematical audit has yet been performed.

Self-review: passed. Independent audit: not yet performed.
