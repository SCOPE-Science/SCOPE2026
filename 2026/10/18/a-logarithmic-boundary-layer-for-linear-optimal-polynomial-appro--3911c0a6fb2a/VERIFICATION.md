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

# Verification and reproducibility

The analytic verification consists of the reversible substitution \(r=1-(1-z)q\) with \(r(1)=1\), strict convexity of the normalized \(H^p\) objective, the conjugate-reversal symmetry, the scalar stationarity equation, and the two exact endpoint substitutions displayed in `RESULT.md`. The constants \(1/(2\sqrt{2\pi})\) and \(\sqrt{2/\pi}\) in the derivative balance give the factor \(4\) in the coefficient boundary layer; the positive endpoint of the objective gives \(1/\sqrt{2\pi}\). All limit statements are proved for arbitrary real \(p\to\infty\), not extrapolated from integer values.

Run `python checks/check.py` from the package root to reproduce `checks/check_output.txt`. The standalone code needs only Python's standard library and evaluates the exact stationarity integral by midpoint quadrature in the angle coordinate, followed by bisection. The quadrature values are approximate; no arbitrary-precision enclosure, global symbolic certificate, or independent mathematical audit is claimed. Full source statements, assumptions and asymptotic proofs are contained in `RESULT.md`.
