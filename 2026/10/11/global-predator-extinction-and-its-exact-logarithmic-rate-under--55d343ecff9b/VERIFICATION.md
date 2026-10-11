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

# Reproducibility and limits

Run `python3 verify.py` using Python 3 and only its standard library in the same directory as the mathematical record. It checks saturation algebra by exact fractions, constructs strictly positive coexistence equilibria by exact rational identities, and computes and brackets delay characteristic roots for examples including \(h=q\) and \(\tau=0\). Expected output is `CHECK_OK`.

The complete mathematical verification rests on the continuous-time comparison proof in RESULT.md. A finite collection of numerical examples does not prove global convergence, uniqueness of an infinite-dimensional attractor, or theorem novelty. In particular, the exact rate is the limit of \(t^{-1}\log p(t)\), not a claimed positive asymptotic prefactor. The independent-audit channel is unperformed.
