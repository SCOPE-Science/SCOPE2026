# Independent scientific audit — SCOPE-20260917-8a9eab50ab21

Date (UTC): 2026-10-01

## Final claim

For the five-dimensional Heisenberg Lie algebra over every finite field F_q, the total number of subalgebras and the subalgebra commutativity degree are given by the record's exact polynomials; equivalently, the number of nonpermutable ordered pairs is q^10+3q^9+7q^8+8q^7+7q^6+5q^5+q^4, so the commutativity degree is asymptotic to 3/q.

## Correctness

**PASS** — The classification was reconstructed from the one-dimensional center and four-dimensional symplectic quotient. Center-containing subalgebras correspond to arbitrary quotient subspaces; all others are graphs of linear functionals over totally isotropic subspaces. For two graph subalgebras, nonpermutability is exactly equality of restrictions on the intersection together with nonorthogonality, giving functional weight q^(r+s-t). Counting line-line, line-Lagrangian, and Lagrangian-Lagrangian cases reproduces the nonpermutable polynomial. Independent symbolic expansion reproduces the stated numerator, and fresh exhaustive enumeration for q=2 and q=3 gives 158/18,964 and 693/292,329 for subalgebras/permutable ordered pairs, exactly matching the formula.

## Originality

**PASS** — The motivating Muhie--Otera--Russo source introduces the invariant for finite-field Lie algebras and gives the rank-one Heisenberg case; the accessible primary record and detailed indexed material do not give the five-dimensional rank-two formula. Resultary search found this 2026-09-17 record as the exact match; all-rank SCOPE formulas on 2026-09-18 and 2026-09-20 postdate it. Older subgroup-commutativity work concerns finite groups and no matching rank-two Lie-algebra formula was located.

### Equivalent formulations

No earlier equivalent rank-two Lie-algebra formula was found.

### Broader coverage

Later coverage does not negate the historical originality of the 2026-09-17 record; no earlier stronger theorem was found.

### Exact database or table

The result is derived by symplectic incidence counting rather than recomputing a known table.

### Claim versus prior implication

The exact rank-two polynomial requires the new graph-intersection incidence calculation.

## Scientific value

**PASS** — This computes the first Heisenberg rank beyond the motivating source's explicit case and supplies a reusable symplectic graph-pair criterion reducing higher-rank questions to finite incidence counts. The exact q-dependence and asymptotic 3/q are natural invariants, not an arbitrary finite slice.

## Source inspections

- **On the number of modular pairs in finite dimensional Lie algebras on finite fields** — https://arxiv.org/abs/2609.19086. Accessible primary record/abstract and indexed theorem information for the Heisenberg rank-one case; full paper text was not retrievable in this run Assessment: PARTIAL_COVERAGE. The source treats the three-dimensional/rank-one Heisenberg case; no rank-two formula was found in accessible material.
- **Exact subalgebra commutativity degree of the five-dimensional Heisenberg algebra** — https://github.com/Resultary/2026/tree/main/2026/9/17/SCOPE-heisenberg-h2-subalgebra-commutativity-degree--8a9eab50ab21. Title and summary Assessment: SELF_MATCH. Exact same rank-two formula.
- **Exact subalgebra commutativity degree of finite Heisenberg Lie algebras** — https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-heisenberg-subalgebra-commutativity-degree--e3fb5b5762fa. Title and summary Assessment: LATER_COVERAGE. An all-rank formula published one day later covers rank two.
- **The subgroup commutativity degree of finite P-groups** — https://doi.org/10.1017/S0004972715000702. Bibliographic/abstract-level material Assessment: NOT_COVERING. Concerns subgroup commutativity in finite groups, not the stated Lie-subalgebra rank-two formula.

## Limitations and residual risks

- The theorem is for Heisenberg rank two. The general graph/incidence criterion is supplied, but no all-rank closed polynomial formula is claimed in this record.
- The motivating 2026 primary paper was not available in full text in this run; the comparison is therefore best-of-knowledge.
- A specialized class-two group formula could conceivably imply odd-characteristic cases, but no matching formula was located.

## Disposition

**PASS**
