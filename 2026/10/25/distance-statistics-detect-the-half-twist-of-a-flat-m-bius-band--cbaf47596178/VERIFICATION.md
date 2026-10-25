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

The exact proof in `RESULT.md` is an analytic covering-space and integration argument; no external/infinite computational certification is asserted. `verify.py` is standalone with declared `numpy` and `scipy` dependencies. Running it samples two area-uniform points, directly minimizes their distances over seven horizontal deck-image lifts, and checks a measure-preserving coupling with the cylindrical comparison. It also performs adaptive numerical quadrature of the derived one-dimensional integral at several widths and circumferences.

Checked cases: \((C,H)=(1,1),(1,3),(3,0.4),(2.3,1.8)\) for the exact local polynomial and onset-ratio convergence; \((C,H)=(1,1)\) with 400,000 direct sampled point pairs for thresholds 0.30, 0.50, 0.55, 0.60, 0.75, 1.00. Assertions passed. The normalized asymptotic ratios at \(\varepsilon=10^{-5}\) were approximately 0.9951, 0.9984, 0.9787, and 0.9959, respectively, consistent with the proved limit. Finite numerical accuracy does not establish the infinite theorem, and a separate independent scientific audit has not occurred.
