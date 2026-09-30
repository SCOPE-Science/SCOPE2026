# Independent audit — 2026-09-29

Record: `2026/09/14/004`  
Audited source tree: `a15668bbddbd1643db5b48d92092bfcef476e31d`  
Disposition: **repaired**

## Correctness

The Kovacic computation for the normalized equation is correct: r=-2(z^2+1)^2/[9 z^2(z^2-1)^2], all four double-pole coefficients are -2/9, and the admissible-degree tests for Cases 1, 2, and 3 are all negative. Thus the normalized SL-form equation xi''=r xi has differential Galois group SL_2(C) and no Liouvillian solution. The original record, however, incorrectly identified the Picard-Vessiot group of the unnormalized Heun equation itself with SL_2(C). Writing D=z(z^2-1) and a=D^(1/3), the normalization is xi=a y and the original Wronskian is proportional to a^(-2), so the original PV field contains a. Since the normalized SL_2 extension is regular and K(a)/K is cyclic of degree three, the original group is mu_3·SL_2(C)={g in GL_2(C): det(g)^3=1}. The repair makes this distinction while preserving the non-Liouvillian and non-dihedral verdict.

## Originality

Kovacic's algorithm and the algebraic normalization of a second-order equation are standard. The contribution is an exact single-parameter specialization and a compact degree obstruction, not a new differential-Galois classification theorem. The repaired group statement is a direct consequence of the algebraic cubic normalization.

## Scientific value

The repaired record gives a complete exact exclusion of all Liouvillian Kovacic cases at the named Heun point and states the correct full PV group of the original equation. It is useful as a reproducible certificate for this specific operator, with deliberately narrow scope.

## Limitations

- The result is specific to t=-1, gamma=delta=epsilon=2/3, alpha=1/3, beta=2/3, q=0.
- The archived script certifies the normalized Kovacic calculation; the mu_3 extension for the original equation is established by the exact Wronskian/field argument in the repaired text rather than a separate script.
- Arithmetic monodromy and fields of definition beyond C(z) are not addressed.
- The original-vs-normalized Galois-group distinction is substantive and is corrected in RESULT.md, METADATA.json, and SLOGAN.txt.

## Sources checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/14/004
- https://doi.org/10.1016/S0747-7171(86)80010-4
- https://dlmf.nist.gov/31.8
- https://dlmf.nist.gov/31.14
