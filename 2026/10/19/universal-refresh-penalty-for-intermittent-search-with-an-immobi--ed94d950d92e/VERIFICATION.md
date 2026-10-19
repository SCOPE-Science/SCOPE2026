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

## Reproducibility

The analytic derivation in `RESULT.md` establishes the theorem for any admissible active Markov search. For an independently constructed finite-state check, run `python verify.py` with NumPy and SciPy. The program builds killed active generators and full two-state resetting generators separately, then solves their mean hitting-time linear systems. It compares 864 generator observables with the claimed analytic formulas across six refresh fractions, several finite graph sizes, variable transition rates and switching/reset rates. On the recorded execution the maximum absolute discrepancy was about 1.35e-12. The finite matrix checks are only illustrations and are not a proof for arbitrary infinite-state motion.
