---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The rational polytope has q² prefix-sum equalities for length-five words and unit capacities at each distinct ordered length-three deletion shadow. A complete finite lemma on 52 restricted-growth patterns proves weighted shadow cost >=14 for equal-symbol prefix and >=19 for different-symbol prefix, with weights 14,3,2,5,2 on AAA,AAB,ABA,ABB,ABC. Summing weighted output capacities yields 14q+19q(q-1) <=14q+q(q-1)(2q+6), hence q>=7. For q>=7, assign prefix aa to aaaaa, and split each ab (a!=b) among symbol-permutation orbits abbca with mass 2/5, abbcc with mass 1/5 and abcde with mass 2/5. Each capacity load by equality pattern is exactly (1,1,4/5,1,5/(q-2)), so feasible iff q>=7, with every prefix total one. Independently checked complete 52-pattern min-cost classification and all q=7 output constraints by exact arithmetic; the universal all-q claim follows by orbit counting. Crucially no integral 7-symbol systematic code is asserted.

## originality

PASS

Existing weighted shadow converses already provide necessary q>=7 for the integral length-five systematic code problem; necessity is not novel. Grishin–Zabokritskiy 2026 concern genuine systematic two-deletion codes with three checks over sufficiently large alphabets and a different adjacent-burst relaxation. The present explicit rational primal solution shows the elementary prefix-constrained LP relaxation is feasible for all q>=7; a previously proved integer bound does not imply this. Full text of closest 2026 preprint was not accessible and remains a stated risk.

## value

PASS

Fractional coding shadow packing is a natural relaxation for deletion-code lower bounds. A sharp feasible/infeasible threshold proves that its single-output-capacity inequalities cannot improve the known seven-symbol necessary alphabet barrier, a useful boundary for future stronger LP and integrality approaches.

The dated certificate retains the supplied scientific assessment, sources and limitations.
