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

# Verification of the inner-parallel visibility law

The proof requires no computer calculation: the tube-coordinate Jacobian, midpoint localization, uniform chord-depth Taylor expansion, the elementary minimization of \(p/t+q/(1-t)\), integration of the visible threshold, and Jensen's inequality provide all essential steps.

`verify_parallel_shell.py` is a dependency-free Python 3 diagnostic script. Run `python verify_parallel_shell.py` in the directory containing it. Its deterministic seed and numerical quadrature reproduce the following recorded checks:

- Exact circle annulus probabilities divided by \(\sqrt\varepsilon\) for \(\varepsilon=0.08,0.02,0.005,0.001\): approximately \(0.61766259,0.60445153,0.60126368,0.60042105\), converging to \(0.600210877438\ldots\).
- Ellipse of semiaxes \((2,1)\): curvature-integral coefficient \(0.577437293058\ldots\); disk lower bound at the same perimeter \(0.483355522208\ldots\).
- Ellipse shell sampling by the exact normal-coordinate area Jacobian, and direct segment clipping against a 720-normal outer polygonal approximation of the eroded ellipse: at thickness \(0.02\), visibility \(4869/60000=0.08115\); at thickness \(0.005\), \(2434/60000=0.0405667\). Their asymptotic predictions are approximately \(0.081662\) and \(0.040831\). The random-seed diagnostic returns `INNER_PARALLEL_SHELL_TESTS_OK`.

These finite numerical checks are not interval certificates and do not prove the limit or uniqueness. Clipping uses a finite-support approximation to the eroded ellipse, so only the analytic derivation is evidence for all bodies. No independent mathematical audit has been performed.
