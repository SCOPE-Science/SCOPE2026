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

# Exact verification record

Run `python3 checker.py` beside this file with Python 3 and no third-party dependencies.

- The script constructs all \(25\) aperiodic difference displacements and all \(25\) coefficient-convolution indices for the full \(3\times3\) aperture.
- Each of the \(51545\) normalized root-of-unity coefficient arrays is evaluated by two independently organized exact-arithmetic formulas. Each integer equality is asserted, not tested with floating-point tolerances.
- The resulting moment minima are \(113,97,105,97\) for phase counts \(2,3,4,6\), and normalized optimizer counts are \(8,2,16,6\), respectively. Multiplication by the free \(q^3\) common/row/column phase group yields the complete counts \(64,54,1024,1296\).
- The ternary proof also gives a symbolic universal lower bound: \(81\) from the origin and at least \(1\) from each of the \(16\) mixed displacements. The two cubic-root Fourier phase matrices attain it.
- Enumerated results are complete only for the four finite alphabets. The independent mathematical audit is not performed; the calculations are reproducible but do not constitute external certification.
