# Independent audit — 2026-10-01

**Record:** SCOPE-20260920-72f274369f61 — Strong cleanness descends from M2 to T2 over local rings

**Disposition:** passed

## Final claim

Let \(R\) be any local ring. Every \(A\in T_2(R)\) that is strongly clean as an element of \(M_2(R)\) is strongly clean in \(T_2(R)\); hence strong cleanness of \(M_2(R)\) implies strong cleanness of \(T_2(R)\).

## C — correctness

Reducing a strong-clean decomposition modulo the Jacobson radical forces the commuting idempotent to be the complement of the mixed-residue triangular matrix. Its image or kernel is then a rank-one free invariant summand; after normalizing a generator to \((t,1)^T\), invariance gives \(at+b=tc\), exactly the equation needed to build an upper-triangular commuting idempotent whose difference from \(A\) has unit diagonal. Both mixed cases and the two trivial-unit cases are covered. The argument uses only standard projective-freeness over a local ring and proves the stated arbitrary-local-ring theorem.

## O — originality

The 2008 Borooah–Diesl–Dorsey paper explicitly poses the elementwise question whether a matrix in \(T_n(R)\) that is strongly clean in \(M_n(R)\) must already be strongly clean in \(T_n(R)\). Its commutative theory and later general-local-ring matrix criteria do not, from the inspected statements, imply the audited arbitrary-local-ring \(n=2\) descent theorem. Targeted Resultary and literature searches found no stronger published theorem covering that implication.

### Source inspections

- **Strongly clean matrix rings over commutative local rings** (DOI:10.1016/j.jpaa.2007.05.020): OPEN_PROBLEM_SOURCE. Problem 49 asks exactly whether strong cleanness of \(\varphi\in T_n(R)\) inside \(M_n(R)\) descends to \(T_n(R)\); the paper does not solve the arbitrary-local-ring \(n=2\) case.
- **Strong cleanness of the 2×2 matrix ring over a general local ring** (arXiv:0805.0359 / DOI:10.1016/j.jalgebra.2008.06.012): PLAUSIBLE_NOT_DECISIVE. The accessible material describes a characterization of rings for which \(M_2(R)\) is strongly clean, not the elementwise \(T_2\subset M_2\) descent implication.

## V — value

The theorem resolves the first nontrivial dimension of an explicit published elementwise descent problem without commutativity, bleaching, completeness, or finiteness assumptions. The invariant-summand mechanism is a reusable structural explanation, so the contribution is mathematically motivated rather than a routine parameter specialization.

## Residual risks

- The complete Yang–Zhou (2008) and Tang–Zhou (2017) theorem texts were not both available through the inspected open routes; an equivalent arbitrary-local-ring elementwise implication hidden there remains a residual originality risk.

This audit is a mathematical review, not external peer review, formal verification, or a guarantee of priority.
