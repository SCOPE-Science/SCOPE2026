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

# Reproducibility and proof checks

The accompanying `verify_cycle_power.py` is a standalone Python 3 script without third-party dependencies. Execute `python3 verify_cycle_power.py` in a directory containing the extracted files.

The exact finite Fourier sign rule is \(\operatorname{sgn}(\sin(\pi a/b))\), determined by the residue of the integer \(a\) modulo \(2b\), with special handling of removable denominator zeros. The script checks all nonconstant frequencies of the four exceptional graphs and verifies mean-zero nullities \(5,6,11,10\). It separately checks explicit strictly positive Fourier frequencies for every smaller excluded cubic power, and integer-angle signs for bounded-diameter higher powers. The finite six- and twelve-site witnesses are verified by exact integer quadratic forms, with value \(2\) in every tested instance. Independent breadth-first searches reconstruct shortest paths, and direct numerical Fourier transforms cross-check the sign formula on additional finite parameters.

**Analytic checks are essential.** The all-parameter statements rely on the trigonometric sign inequalities and uniform local distance patterns proved in `RESULT.md`, not on extrapolation from finite loops. The resulting kernel statement uses the classical negative-type/positive-definite exponential equivalence; its converse is independently visible in the first-order small-scale expansion. The companion script is ordinary reproducibility code and not independent certification. No separate external audit was performed.
