---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-01.md",
      "INDEPENDENT_AUDIT_2026-10-01.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

Independent reconstruction of the committed construction reproduced P_full size 4, pairwise 2-intersection, U=14,64,362,2428 and |F|=14,60,362,2616 for n=6..9, with the closed rook formula matching brute force for n=6..8 and the formula at n=9. Exhaustive 2-coset scans for n=6,7,8 give Delta_2=|F|-4. The general pairwise-intersection and Delta_2 comparison arguments are consistent with these checks and the factorial/rook formula.

## originality

PASS

Known stability results do not mechanically imply this exact transverse-coset construction or rook-theoretic count.

## value

PASS

The family is a motivated next-layer stability construction for the open gamma_2>=3 extremal problem. Its exact deletion formula and diversity-4 boundary supply a reusable sharpness candidate rather than an arbitrary finite slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
