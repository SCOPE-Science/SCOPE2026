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

# Reproducibility of the periodic-lift classification

Run `python verify.py` with Python 3 and no third-party dependencies. The program constructs four-state Boolean de Bruijn transfer matrices from the local rule, checks finite-ring input images against positive matrix traces, and checks period-doubled lifts with squared products. It visits all binary cyclic words of lengths \(1\) through \(12\), checking both exceptional odd-weight cyclically `11`-free words and the exact Lucas/character census. Observed execution result:

`VERIFY_OK: n=1..12; 8190 exact cyclic words; 32760 transfer/cycle/ring checks; 420 total exceptional words; 12 Lucas character formulas`

This exhaustive bounded computation checks the finite instances only. The general theorem and asymptotic statements are proved symbolically in `RESULT.md`. The checks do not constitute external peer review or independently certified validation.
