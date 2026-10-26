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

# Verification

The standalone standard-library Python program `verify.py`, run beside `CERTIFICATE.json`, computes all required six-vertex edge-induced survivor distributions and verifies the analytic first-three-moment census with exact integer/Fraction arithmetic. It checked 32,768 labeled graphs and 688,128 exact moment equalities, and separately enumerated connected regular types through order six and the prism/bipartite probability generating functions. The certificate is reproducible program output, not a substitute for the general combinatorial proof in RESULT.md. Independent scientific validation has not been performed.
