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

# Verification details

The proof certificate is `CERTIFICATE.json`, with a dependency-free checker `verify.py`. Run `python verify.py CERTIFICATE.json`. The checker reconstructs binary words, distinct two-deletion output sets, integer feasibility, exact rational primal and dual inequalities, and all inclusion/exclusion nodes and exact leaf bounds. It verifies a complete binary branching tree, rather than accepting a solver's status message. The earlier-length statements are checked using the bundled witnesses and dual weights. The matching standard output is provided in `VERIFICATION_OUTPUT.txt`.

For the length-eight integer upper bound, the certificate has 205 nodes: 102 branches and 103 dual leaves. Every leaf dual bound is strictly below 16. For the fractional LP, the primal and dual objectives both equal \(2188/135\). The verifier uses arbitrary-precision rational arithmetic. The proof is finite, does not establish broader blocklength claims, and has not been independently audited.
