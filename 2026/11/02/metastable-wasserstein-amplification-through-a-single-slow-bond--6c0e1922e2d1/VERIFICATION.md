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

# Reproducibility and scope

Run `python check_slow_path.py` using Python 3, NumPy and SciPy. The actual run completed with `PASS: 2290 finite comparisons / assertions; no infinite-family certification`.

The checker builds the full vertex generator and, separately, the reflecting half-size generator. It compares adjacent heat-kernel \(W_1\) distances computed from cumulative masses with adjacent expected-position differences, checks the reduction at the central edge, reconstructs the unperturbed Fourier series, and compares numerical peak locations and heights with the two-term asymptotic. Its finite set of tests is supplementary to the written analytic proof and is not an exhaustive computation for arbitrary size, rate or time.

The asymptotic conclusions hold for every **fixed** integer \(m\ge2\) as \(\varepsilon\downarrow0\). All geometric edges retain unit length while the one central *jump rate* changes. The original Markov semigroup is symmetric, conservative and irreducible for every positive rate. No separate independent human verification has been carried out.
