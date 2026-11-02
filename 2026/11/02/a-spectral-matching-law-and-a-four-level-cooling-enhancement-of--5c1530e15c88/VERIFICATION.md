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

# Verification procedure and limits

Run `python3 check.py` using a standard Python 3 interpreter. The script requires no nonstandard packages or network connection and prints a PASS line on success.

The checker compares the greedily computed optimum with the exact maximum across **every permutation** for 325 fixed randomized strictly increasing integral spectra in dimensions 2 through 6. The initial Gibbs weights are exact rational powers of one half. Thresholds include exact energy differences (testing the inclusive event) and half-integer values. For each maximizer it verifies the precise greedy set of winning sources. Separately, it verifies the explicit four-level spectrum, the exact \(17/160\) right derivative at \(\beta=0\), a numerical root of the peak equation, the peak probability, and strict negative average extracted work for the displayed transposition at representative positive inverse temperatures.

Proof-level checks, not encoded as infinite computation, are the convex extreme-point reduction, the nested-target matching criterion, the lexicographic comparison of feasible source sets, canonical derivative monotonicity, and the energy-majorization identity. For universality at arbitrary real spectra, thresholds, inverse temperatures and Hilbert-space dimension, refer to the written analytical proof. Finite tests do not establish these universal statements or originality. No independent external proof or publication-priority validation has been performed.
