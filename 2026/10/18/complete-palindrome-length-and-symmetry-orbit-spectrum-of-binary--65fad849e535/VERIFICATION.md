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
# Verification and limits

Run `python3 verify.py` in a clean Python 3 environment. Only the standard library is used. The script contains two complete generators for binary order-five de Bruijn cycles and two independent palindrome-length procedures. The local-matching generator exhausts precisely \(2^{16}\) choices; the independent Euler-tour routine checks all unused edges and a final return to its initial vertex. Exact wordwise agreement, the full integer histogram, the canonical symmetry orbits and every printed count are asserted. The check is an exhaustive finite certificate for order five, not a proof of a general-order statement.

The proof of exhaustiveness is written in `RESULT.md`. The source-code and data assertions are distributed together; no external dataset, private path, downloaded paper, or additional package is necessary. The source literature establishes context rather than independent validation of these counts. The journal full text for Simpson's 2014 paper was not obtained, so its comparison rests on the publicly accessible abstract and source description.
