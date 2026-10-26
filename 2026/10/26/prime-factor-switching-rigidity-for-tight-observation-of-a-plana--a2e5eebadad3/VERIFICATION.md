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

# Computational and analytical verification

The proof appears in `RESULT.md`. Its indispensable steps are: exact two-by-two information spectrum; signed root-of-unity telescoping; the cited minimum-length and equality classification of root-of-unity vanishing sums; an explicit feasible alternating-block construction; and unique monic cyclotomic division in the one-odd-prime-factor case.

Execute `python verify_sensor_schedule.py` using Python 3 with no third-party dependencies. The checker was executed with this output:

```
EXACT_CYCLOTOMIC_OK n=2..16 schedules= 65534
CONSTRUCTIVE_CYCLOTOMIC_OK additional n=18..75
GRAM_SPECTRUM_OK exact finite model; floating angular cross-check
```

The first check enumerates all binary sequences up to global complementation for \(2\le N\le16\) using integer polynomial remainder modulo \(\Phi_{2N}\); verifies the claimed least-switch and unique optimal sequence for each eligible \(N\); and verifies the entire prime-power family count wherever it applies. Additional explicit block schedules were tested for a finite collection of horizon lengths at most \(75\). The final Gramian check compares the derived closed spectral formula against a finite trigonometric matrix calculation. Numerical roundoff does not enter the cyclotomic divisibility results. These finite checks do not certify claims for unbounded \(N\), which depend on the mathematical proof and Lam–Leung's established theorem.

All claims require exactly the assumptions stated in `RESULT.md`; none addresses arbitrary rotations, random sensor failures, process noise, unequal sensor costs or general non-isotropic priors. No independent audit has been performed.
