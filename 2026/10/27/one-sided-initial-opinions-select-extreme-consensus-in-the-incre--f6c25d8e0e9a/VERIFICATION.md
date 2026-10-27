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

# Reproducibility and proof scope

The complete mathematical argument is in `RESULT.md`. The only computational dependency is Python 3 (standard library); run `python3 verify.py` beside this file.

Exact checks: integer polynomial coefficient identity \((1+r)rZ'(r)-2krZ(r)=r(r-1)\sum_{j=0}^{2k-2}(j+1)(2k-1-j)r^j\) for \(1\le k\le40\); exact discrete-parabola Laplacian and positive linearized residual for \(1\le k\le40\); rational stationary-mean inequalities at three arguments for each \(k\). Additional numerical checks cover the neutral reflecting eigenfunction signs and convergence examples \(1\le k\le6\).

The analytic comparison principle, general geometric-mean factorization, and all-\(k\) spectral/subsolution argument are proved in the text. Finite tests do not certify arbitrary initial distributions or an infinite range of opinion sizes. No independent audit has been performed.
