# Independent audit — 2026-09-30 UTC

Record: `2026/09/21/murray-frobenius-norm-conjecture-characteristic-two--780b8c8c93a5`  
Assigned and audited source tree: `cc0b6191b9b97a2b512f9b9d416cad1fc5f903d5`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `fdc17b16e611231c405acaa8e3ebcb6141e8c4b5`  
Disposition: **passed**

## Correctness

**independently_supported**. The counterexample is valid. For R_d=k[t]/(t^{2d}) with lambda the t^{2d-1} coefficient, B(r,s)=lambda(rs) has reverse-identity Gram matrix and is a symmetric Frobenius form. Its Nakayama automorphism is the identity, so Murray's norm of u=1+t is u itself and is central. In characteristic two, r^2 contains only even powers of t, hence B(r,r)=0 for all r. But B_u(t^{d-1},t^{d-1})=lambda(t^{2d-2}(1+t))=1, so B_u is nonalternating. Alternation is invariant under Murray's homothety C'(r,s)=alpha C(Vr,Vs), proving nonhomothety. In dimension one every nondegenerate bilinear form is homothetic, so d=1 is minimal.

## Originality

**qualified_supported**. Murray's open author manuscript was checked directly: the symmetric-local converse in Section 4 assumes char(k) != 2, Theorem 15 gives the central-norm condition as necessary, and Conjecture 16 states the converse without retaining a characteristic restriction. Targeted searches for Conjecture 16 together with characteristic-two, dual-number, truncated-polynomial, alternation, and homothety terminology did not locate a published correction or equivalent counterexample. The construction is elementary once characteristic two is tested, so an unindexed note or informal correction remains a residual priority risk.

## Scientific value

**meaningful_minimal_counterexample**. The record gives a dimension-minimal counterexample to a published 2005 conjecture, extends it to every positive even dimension, and identifies the missing invariant: centrality of the separating norm does not detect alternation in characteristic two.

## Independent checks

- Inspected Murray's open manuscript at the homothety definition, Section 4 characteristic assumption, Theorem 15, and Conjecture 16.
- Verified the reverse-identity Gram matrix and alternating/nonalternating calculation directly.
- Checked that the example satisfies the literal residue-field, finite-order-Nakayama, and central-norm hypotheses.
- Ran targeted current searches for published corrections or characteristic-two counterexamples.

## Literature and evidence checked

- https://arxiv.org/abs/1401.6486
- https://doi.org/10.1016/j.jalgebra.2005.07.031
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/21/murray-frobenius-norm-conjecture-characteristic-two--780b8c8c93a5
## Limitations

- The result refutes Conjecture 16 only as literally stated in characteristic two.
- It does not decide a corrected converse in characteristic different from two or the general nonsymmetric case.
- Because the construction is short, an unindexed correction or observation remains possible despite the targeted search.
