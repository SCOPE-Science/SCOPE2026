---
audit_date: 2026-09-30
status: passed
---

# Scientific audit

## Final claim

Over F_3 there is an explicit non-complete-intersection codimension-three Artinian Gorenstein quotient with Hilbert function (1,3,5,5,3,1), five Pfaffian generators of degrees 2,3,3,4,4, and Jordan type different from the exceptional complete intersection (x^2,y^3,z^3) for every nonzero linear form.

## Correctness — PASS

The inspected alternating matrix was independently converted to its five submaximal Pfaffians. Their degrees were confirmed as 2,3,3,4,4. Independent Macaulay-matrix ranks gave Hilbert function (1,3,5,5,3,1) and minimal-generator gains 1,2,2 in degrees 2,3,4. Multiplication matrices were independently formed for all 26 nonzero F_3 linear forms; every Jordan partition differed from the complete-intersection comparator, including x+y+z giving (5,5,3,3,2) versus (3,3,3,3,3,3).

**Evidence.** artifacts/verify_lane109.py blob 15a9e9fd54c68e095e83fba639a20d2084c282a2

**Residual risk.** The minimal free-resolution shifts use the standard Buchsbaum–Eisenbud codimension-three Gorenstein structure theorem rather than a separately computed syzygy matrix; the generator data and Hilbert series are consistent with those shifts.

## Originality — PASS

Boij–Migliore–Miró-Roig–Nagel–Zanello identify the characteristic-3 complete-intersection exception for this Hilbert function, but their Lemma 3.7 concerns complete intersections. Abdallah–Altafi–Iarrobino–Yaméogo classify Jordan degree types for the same almost-constant Hilbert shape in characteristic zero and give only upper restrictions in finite characteristic; they do not supply this explicit F_3 non-CI Pfaffian ideal, its graded resolution, or its all-26-form separation from the CI exception.

- Equivalent formulations: Checked WLP/Jordan-type and Pfaffian codimension-three Gorenstein formulations.
- Broader coverage: The 2025 JDT classification covers characteristic zero broadly, not this finite-field realization.
- Exact database or table: The JDT tables are the closest exact table; their finite-characteristic statement is an upper restriction, not this explicit row.
- Claim versus prior implication: The prior CI exception and finite-characteristic JDT bounds do not construct or identify this non-CI algebra.
- Sources inspected: https://arxiv.org/html/1302.5742v2; https://arxiv.org/html/2406.06322v2
- Residual risk: A later database of finite-field examples could overlap, but none was found in the searches.

## Value — PASS

The example sits at a specifically documented characteristic-3 boundary and demonstrates that the exceptional Hilbert function contains a non-CI Gorenstein model whose Jordan behavior is uniformly separated from the exceptional CI. That is a motivated boundary witness, not an arbitrary random ideal.

**Context.** Boij et al. Lemma 3.7; Abdallah et al. small-Sperner JDT program

**Residual risk.** It is an explicit witness rather than a classification of the finite-characteristic locus.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
