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

The supplied `verification.py` requires Python 3 and SciPy. Reproduce with `python3 verification.py` from the same directory. On the packaged source it reported `PASS 495 analytical-identity spot checks; profiles cos(t), cos(t)^3, cos(t)^5; contrasts 0.1, 0.5, 0.9`.

The checker recomputes each first-arrival time from its defining integrated advection equation; compares the global candidates against 64 uniformly spaced release phases; checks the two exact scalar root equations, half-cycle peak value, period invariance and the cusp slope close to full-cycle lengths; and tests distinct non-sinusoidal profiles. Numerical errors are bounded by explicit assertions in the code. Finiteness of these tests cannot establish the universal theorem; the strict-monotonicity, concavity and uniform-implicit-function arguments appear in `RESULT.md`.

No independent audit or independent validation has been performed. No certificate of complete historical priority is asserted.
