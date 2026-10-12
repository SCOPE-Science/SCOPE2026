---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification scope

The scientific derivation is in `RESULT.md`, Steps 1–5. It establishes the identities and limits for every integer \(n\ge3\) and bias \(p\in[0,1]\). The embedded `verify.py` reproduces finite exact checks without third-party packages. Running `python3 verify.py` returned `PASS: 1936 exact finite checks across 88 (n,p) pairs`.

The checker verifies orientation enumeration, rotationally uniform marginals of the explicit coupling, correct mean edge discrepancy, exact total variation, endpoints, and the complete cyclic-run distribution for small cycles. Finite enumeration does not establish a universal theorem; the proof does. No independent audit or independent validation has been performed. Literature-priority uncertainty remains as specified in `REVIEW.md`.
