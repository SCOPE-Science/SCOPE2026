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

# Verification and boundaries

The exact proof uses the product expression for leaf probabilities, one-event conditioning on a parent selection, and sums of rational reciprocal terms. The local formula and its sign switch are valid for all \(2\le i<j\le n\). The finite sign result follows from strict discrete convexity; the asymptotic sign threshold follows from harmonic sums and strict convexity of \(g(t)=(1-t)/2+t\log t\).

Run `python3 verify.py` with a standard Python 3 installation. The checker enumerates every recursive-tree parent assignment through eight vertices and compares exact rational covariances and variances. It checks the finite difference and sign structure for orders through 150 and numerically samples the limit profile. Expected output: `VERIFY_OK 11429 exact finite or profile assertions`.

Finite testing does not prove the claims for arbitrarily large trees; their proof is in `RESULT.md`. Exact mathematical identity, prior-art priority and independent audit are distinct matters. The latter has not been performed.
