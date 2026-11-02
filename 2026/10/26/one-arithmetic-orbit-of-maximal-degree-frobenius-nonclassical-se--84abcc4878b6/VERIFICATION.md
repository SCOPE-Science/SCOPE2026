---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

PASS: Using the source's explicitly cited Asgarli–Duan–Lai Proposition 4.8, q=4 and characteristic 2 fix the normalized gradient of a maximal-degree smooth Frobenius-nonclassical sextic. The derivative-free degree-six difference is precisely a cubic G(x²,y²,z²) in 10 independent F4 coefficients; no scalar duplicates survive normalization. All three derivatives vanish simultaneously at exactly the 21 points of PG(2,F4), so geometric smoothness iff F is nonzero at those 21 points, with no untested algebraic-closure singularities. A separately authored F4 enumerator traversed all 4^10=1,048,576 coefficients and found exactly 960 smooth; a separately implemented orbit traversal under explicit invertible projective generators reached all 960 and orbit-stabilizer gives |PGL3(F4)|/960=63. The representative's nonzero rational evaluations and no-F4-points statement also follow. This is exhaustive finite arithmetic supporting an exact finite classification, not extrapolation. Inspected actual source files RESULT.md, verify_cpp.cpp, verify_python.py; the latter's code, not merely expected logs, was reviewed.

## originality

PASS

Known maximal-degree normal form, smooth examples, and conditional Singer-automorphism classification are acknowledged. Fresh exact finite enumeration plus transitivity for *all* smooth F4 sextics and arithmetic stabilizer 63 are not stated or logically forced by the inspected prior results. Best-of-knowledge PASS only, retaining priority risk from specialized finite-geometry literature.

## value

PASS

PASS: The projective orbit count is a natural complete arithmetic classification of a sharply constrained maximal-degree finite-field plane-curve family. The exact 960 normalized equations, single orbit and stabilizer 63 distinguish moduli from mere existence; a finite classification is substantive because all 1,048,576 candidates are conclusively resolved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
