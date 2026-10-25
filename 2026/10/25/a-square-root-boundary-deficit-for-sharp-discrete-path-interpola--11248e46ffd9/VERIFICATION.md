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

# Verification record

The included `check.py` uses only the standard library. On integer path sizes 2 through 12 and four positive resolvent parameters, it compares the closed hyperbolic diagonal with a direct independent tridiagonal linear solve and with the discrete-cosine spectral expansion, checking every vertex. It also checks endpoint dominance, sampled all-length monotonicity, the exact two-vertex value, and the asymptotic prediction at lengths 100, 1000 and 10000. Execute with `python3 check.py`.

These are finite calculations and do not establish universal claims. The proof of the full-domain sharp constant, strict monotonicity and boundary asymptotic is contained in RESULT.md. The originality analysis is a literature comparison subject to explicitly listed access risks; no independent mathematical audit has occurred.
