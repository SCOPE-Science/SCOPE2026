# Scientific review

## Correctness — PASS

The square map is additive precisely because of commutativity in characteristic two, so any binary evolution-algebra structure matrix acts as an \(\mathbb F_2\)-linear Frobenius-semilinear idempotent equation after scalar extension. The Fitting decomposition eliminates the nilpotent component. A normal basis gives \(2^r\) explicit geometric solutions and conjugates Frobenius to the invertible stable binary matrix inverse. Pairwise coprime leading monomials of the transformed equations prove the coordinate-ring length \(2^r\); the identity Jacobian proves reducedness. Kernel counts, Möbius inversion, zeta and splitting-degree statements follow. Primitive irreducible characterizes the maximally delayed first nonzero idempotent by eigenvalue order. The standard-library checker independently of matrix-power counting tests the original square equations in 2,208 bounded cases. Residual correctness risk: the proof is not formally or independently audited; exhaustive finite testing does not cover every dimension/degree.

## Originality — PASS (qualified historical search)

The 2010 primary evolution-algebra paper studies idempotent systems for real parameters. The 2026 survey gives general geometric idempotent bounds and a two-dimensional Galois criterion, but not the dimension-uniform sharp primitive-irreducible first-occurrence classification or its one-orbit zeta. The previously reported graphical-algebra formula already implies the fixed-point census for binary adjacency matrices and is expressly excluded from the claimed novelty; graph matrices form a restricted symmetric zero-diagonal class and cannot realize the cubic primitive companion construction. The earlier finite-field idempotent-free result establishes existence, not the exact optimal extension degree or Frobenius cycle type. Broad normal-basis/Singer-cycle facts underlie the proof and are not claimed as new. The scope, strict extremizer equivalence and all-extension orbit structure were not found in inspected primary literature or targeted searchable records; a general semilinear theorem that already packages this conclusion remains the leading originality risk.

## Value — PASS

The absence of nonzero idempotents in perfect evolution algebras over the original finite field is a motivated structural obstruction; field extension is the natural way to measure it. The theorem gives the **sharp** maximal minimal splitting degree, growing exponentially with dimension, classifies every extremizer by a natural matrix invariant, and resolves the exact Frobenius cycle/zeta profile of those extremizers rather than just counting points over one field. This is a natural family-wide cutoff and complete arithmetic classification, not a single arbitrary computation. It also distinguishes arbitrary binary structure matrices from graph-adjacency special cases. It does not purport to classify isomorphism types or all fields.

## Closest antecedents and limitations

Casas–Ladra–Rozikov (2010), arXiv:1004.0155; Casas–Ladra–Omirov–Rozikov (2012), arXiv:1208.1709; Kaygorodov–Martín González–Viruel (2026), arXiv:2610.22248; Narkuziyev (2018), arXiv:1803.11415; Wei–Zou (2023), arXiv:2310.12368; previously published fixed-point formula for graphical evolution algebras; and the published finite-field perfect idempotent-free existence result (URL in RESULT.md). Main residual risk: potential implication from an unidentified stronger general theorem on semilinear fixed points. Independent validation and exhaustive publication-priority certification are not supplied.

Self-review: passed. Independent audit: not yet performed.
