# Independent audit — a six-variable Perazzo-type quartic

**Review date (UTC):** 2026-09-24  
**Source path:** `2026/09/08/055`  
**Audited source tree:** `f85a57adfa3346a02c2b6fc454f4e053ce53c465`  
**Review type:** separate AI independent audit.

## Claim audited

For `F=x0*u^3+x1*v^3+x2*(u+v)^3+w^4` over characteristic zero, the apolar Artinian Gorenstein algebra has Hilbert vector `(1,6,7,6,1)`, vanishing first Hessian, the weak Lefschetz property, and the stated codimension-six graded Betti table.

## Correctness — PASS

I rebuilt the apolar computation independently rather than relying on the committed verifier. Enumerating all differential monomials gives catalecticant ranks `1,6,7,6,1`. Using pivot derivative classes as quotient bases, I independently constructed multiplication matrices in every degree. For `L=x0+x1+x2+u+v+w`, the ranks are `1,6,6,1`, exactly the maximal possible profile, so WLP holds. The Hessian vanishes identically already from structure: the rows corresponding to `x0,x1,x2` are supported only in the `u,v` columns, hence three rows lie in a two-dimensional coordinate subspace.

I then independently built the graded Koszul complex from those quotient multiplication matrices and computed homology degree by degree. The Betti rows are exactly those stated in the record: degree 2 has `beta_1=14`; degree 3 has `(beta_1,beta_2)=(2,36)`; degree 4 `(4,8,39)`; degree 5 `(0,20,12,20)`; and the remaining rows are the Gorenstein-symmetric reverse, ending in `beta_{6,10}=1`. The Hilbert numerator `(1-t)^6(1+6t+7t^2+6t^3+t^4)` also matches all alternating Betti sums.

## Originality — PASS relative to checked literature

The nearest Perazzo WLP results do not mechanically settle this example. Fiorindo–Mezzetti–Miró-Roig (2023) treats the five-variable `P^4` family with two base variables. Miró-Roig–Pérez-Díez (2024) treats the `P^{n+2}` two-base family and explicitly notes that those results do not generalize to `P^{n+3}` with three base variables. Mezzetti–Miró-Roig (2024) proves broad max/min Hilbert-vector and WLP results under hypotheses including `n>=m` in the relevant theorems; this form has three `X` variables but three base variables, so in their notation `n=2<m=3`, outside that regime. Their minimal-free-resolution theorem is for five-variable minimal Perazzo threefolds, not this six-variable quartic. Miró-Roig–Pérez (2025) computes Betti numbers for full Perazzo algebras; this example is not full since `n+1=3` whereas `binom(d+m-2,m-1)=10`. No checked source gives this named form, its WLP witness, or this Betti table.

## Scientific value — PASS

The record supplies a concrete exact data point in the three-base-variable region that the two-base classifications do not control, including both a Lefschetz verdict and a full minimal-resolution invariant. This is narrow rather than a classification theorem, but the explicit Betti table addresses an instance of the still-partial Perazzo-resolution program and the WLP calculation distinguishes behavior in an expressly non-covered regime.

No repair was needed. The result is only about this named quartic; no general six-variable classification or full Lefschetz-locus description is claimed.

**Final disposition: PASSED.**
