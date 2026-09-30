# Independent audit — 2026-09-29

**Record:** `2026/09/17/gaussian-moment-deficit-correlation-obstruction--31c741d42df0`  
**Audited source tree:** `64d4682420dd56d62a61de997de65d4c7d0be68a`  
**Repository:** `SCOPE-Science/SCOPE2026` at checked commit `253a0fe5d0217455660a277f9adb940030e567ad`  
**Overall independent-audit verdict:** **PASS**

## Correctness — PASS

The finite-cubature argument is sound. The spherical 2q-th moment tensor lies in the convex hull of u^(⊗2q); because these tensors lie in the affine hyperplane fixed by contraction with the q-fold identity, Carathéodory gives at most binomial(k+2q-1,2q) positive nodes. Contracting yields the exact coefficient (2q-1)!!/[k(k+2)...(k+2q-2)], and the identity forces the nodes to span R^k. If their Gram matrix were compatible with a standardized common margin F, the rank-k representation produces an isotropic V with all node projections distributed as F. Jensen then gives E|V|^(2q)>=k^q, producing exactly the stated Gaussian-moment threshold. For q=2 the algebra gives k>2κ/(3-κ). Independently reconstructing the six normalized icosahedral directions gives Gram eigenvalues 2,2,2,0,0,0 and the exact quartic identity sum <a_j,x>^4=(6/5)|x|^4, hence κ>=9/5. The standardized Beta(a,a) fourth moment is 3(2a+1)/(2a+3), so it is below 9/5 exactly for a<1. Devroye–Letac's open full text states universal Beta(a,a) compatibility through dimension five for a>=1/2, and Wang–Zhang gives the uniform threshold nine, completing the stated Beta classification.

## Originality — PASS

Phillips supplies the fixed-margin projection framework and the icosahedral arcsine endpoint, while Wang–Zhang settles the uniform dimension-nine threshold; Devroye–Letac supplies the positive low-dimensional Beta result. None of those sources states the general theorem that every strict even-moment deficit below the Gaussian moment yields a finite obstruction via positive spherical cubature, nor the resulting exact threshold five for the entire interval 1/2<=a<1. Targeted searches across fixed-margin compatibility, moment obstructions, spherical designs and cubature did not locate an equivalent theorem. This is a qualified priority assessment rather than proof of exhaustive novelty.

## Scientific value — PASS

The theorem converts a one-dimensional scalar moment deficit into a finite-dimensional elliptope obstruction with an explicit cardinality bound, covering every platykurtic margin and all higher even-moment deficits. The icosahedral specialization yields a sharp fourth-moment-only six-dimensional barrier and, when combined with prior positive results, an exact continuum of symmetric-Beta thresholds.

## Sources used in the independent comparison

- https://arxiv.org/abs/2609.14610 — Phillips, Two short proofs of incompatibility for correlation matrices; provides the fixed-margin framework and the six-direction icosahedral arcsine obstruction.
- https://arxiv.org/abs/2609.16278 — Wang–Zhang, The exact dimensional threshold for Spearman rank-correlation compatibility; proves the uniform threshold d<=9.
- https://doi.org/10.1007/978-3-319-18585-9_25 — Devroye–Letac, Copulas with prescribed correlation matrix; open full text inspected for universal Beta(a,a) compatibility in dimensions at most five for a>=1/2 and the uniform low-dimensional results.
- https://doi.org/10.1016/j.spl.2019.03.015 — Wang–Wang–Wang, Compatible matrices of Spearman's rank correlation; earlier rank-decomposition and incompatibility context.

## Limitations and residual uncertainty

- The moment-deficit criterion is sufficient rather than necessary, and the Carathéodory node bound is not asserted optimal.
- For Beta(a,a) with a>1 the record proves eventual incompatibility but not an exact dimension threshold.
- Priority remains qualified with respect to older copula, moment-problem and cubature literature under different terminology.

This independent audit is scoped to correctness, originality, and scientific value. Repository material was used as evidence only; no GitHub modification was made during the audit.
