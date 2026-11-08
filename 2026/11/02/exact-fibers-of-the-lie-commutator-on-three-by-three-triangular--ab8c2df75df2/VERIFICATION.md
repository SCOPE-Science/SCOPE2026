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

Actual multiplication gives u=A·S, v=B·T, w=(A+B)·R+det(S,T); there are q² diagonal lifts for fixed A,B. For A+B≠0, R contributes q solutions; for A+B=0 the determinant count splits according to u=v=0 and w=0. The derived formula q³M(u)M(v)+1_{u=v=0}(q^8 1_{w=0}−q^7) yields four positive strata and, after summing over w, independent U,V; half L1 deviation gives (q−1)/q^5. Independent literal matrix-pair enumeration checked every pair at q=2 and q=3, including characteristic two.

## originality

PASS

De Mello 2019 classifies images of multilinear polynomials on UT_3 over infinite fields and already covers commutator image surjectivity. Kaur–Sharma–Singh 2020 compute commuting probabilities of invertible triangular groups in odd characteristic, not ordered full-algebra nonzero additive bracket fibers. The result is limited to this finer complete distribution.

## value

PASS

Exact preimage counts and a localized central-coordinate independence defect quantify the nonuniformity of a canonical bilinear Lie bracket map, refining image or zero-commutation-only calculations. The exact four strata and TV formula can support random triangular matrix and Lie algebra analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
