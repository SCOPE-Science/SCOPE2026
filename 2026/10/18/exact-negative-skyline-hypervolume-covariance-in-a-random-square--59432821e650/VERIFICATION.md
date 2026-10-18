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

# Reproducibility of mathematical checks

`verify.py` is a self-contained Python 3 program using `fractions.Fraction`, `itertools.permutations`, and other standard-library modules. Run it with `python3 verify.py`.

The program independently enumerates all second-coordinate permutations for \(1\leq n\leq9\), taking expectations of the dominated-area statistic exactly by conditional integration of uniform-order-statistic values and independent uniform spacings. It checks mixed moments for the skyline count and for each record-position indicator, the harmonic formulas, and exact signs. Further exact rational comparisons reach \(n=150\), and three larger sample sizes each support two bounded numerical scaling checks. A completed invocation printed:

`PASS: 373 exact rational finite checks; 6 explicitly bounded large-n scaling comparisons`

The finite checks support, but do not logically substitute for, the proof for all positive integers in `RESULT.md`. No independent scientific audit, independent proof check, or historical-priority certification is claimed.
