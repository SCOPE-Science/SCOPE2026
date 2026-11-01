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

# Verification of the multiharmonic flip-resonance formulas

Run `python verify.py` with Python 3, `sympy`, and `mpmath` to reproduce the recorded checks.

The checker verifies (i) symbolic cancellation of the cubic branch coefficient and the linear return-trace coefficient, (ii) the zero, first three derivatives and corresponding analytic formulas at selected roots, (iii) numerical solutions of the **original** local two-cycle equations at two supercritical offsets for \(W=2,3,4,7,50\), (iv) both stages of the full kicked-rotor map returning to the initial point and momenta, (v) the predicted elliptic trace, and (vi) the example fixed-point count at \(W=50\), \(K=1/10\).

The actual packaged checker was executed successfully with output `CHECKS_OK 345 exact symbolic, high-precision root, full-map return and trace checks`.

These computations verify representative algebra and numerical reconstruction, not the infinite claims. The quantified assertions for all integer \(W\ge2\), exact local branching and spectral signs follow from the analytic trigonometric-factorization, implicit-function and Taylor proofs in `RESULT.md`. The asymptotics are local and not uniform in \(W\). No independent external mathematical audit was performed.
