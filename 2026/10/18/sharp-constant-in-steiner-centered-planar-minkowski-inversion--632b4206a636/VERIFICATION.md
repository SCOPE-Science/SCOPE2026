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

# Reproducible checks and their limits

Run `python3 check.py` in the extracted directory. The program computes the mass and vector first moment of each atomic probability, validates the nonnegative transportation coupling, recomputes the periodic Green-kernel support gap, and checks that the explicitly proved lower-bound ratio increases toward \(\pi\) on a geometric sequence of positive angles. It also verifies the first-order asymptotic ratios at small arguments.

The program cannot by finite sampling certify a universal supremum or exclude previously published equivalents. The analytic proof in RESULT.md is necessary: the previously established universal upper bound, the explicit family, the limit \(E_\varepsilon/\varepsilon\to1/2\), the transport limit \(T_\varepsilon/\varepsilon\to1\), and preservation of balance under positive periodic heat convolution together prove the result. No independent audit has been performed.
