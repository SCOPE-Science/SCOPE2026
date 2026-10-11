---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For a cross-part edge xy with x in V_i and y in V_j, a vertex resolves x,y exactly when it lies in V_i union V_j, so every local-resolving constraint is s_i+s_j>=1 for the part totals s_i. For k=2 there is one constraint and optimum 1. For k>=3, summing all pair constraints gives (k-1) sum_i s_i >= k(k-1)/2, hence objective at least k/2; s_i=1/2 attains it. At equality every pair constraint is tight, and for k>=3 these equations force every s_i=1/2. Thus the optimizer face is exactly as claimed. An independent direct-distance replay verified every local neighborhood through order eight, and the inspected package verifier blob afc61af0042b0b689b4b6fc518ad5d2622b9d050 solves the vertex LP through order ten.

## originality

PASS

The foundational paper explicitly states the conflicting value k-1 in Lemma 2.11 even though its own preceding definitions and local-neighborhood identity lead to the corrected LP. Exact lemma-number/formula searches, correction/erratum searches, and Resultary queries found no later repair or equivalent optimizer classification.

## value

PASS

The claim repairs an infinite-family formula in the foundational paper for the parameter, fixes an internal contradiction already visible on K_3, and gives the full optimal part-total face. This is a natural structural correction, not an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
