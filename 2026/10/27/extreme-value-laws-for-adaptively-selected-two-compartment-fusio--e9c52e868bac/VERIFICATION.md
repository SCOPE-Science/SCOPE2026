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

# Reproduction and proof checks

The standalone Python 3 program `VERIFY.py` performs **131 deterministic identity/comparison checks** on the finite adaptive-fusion formula. Run from this directory with `python3 VERIFY.py`; only the Python standard library is required.

It enumerates every imbalance configuration for an exact rational symmetric five-point distribution and independently checks optimal pair selection, the derived exceedance formula, and its multinomial expansion for pool sizes 2 through 5. It then evaluates Poisson-difference tails by direct convolution of two Poisson laws and by an independent Bessel-power double series, and compares two independent forms of the finite-pool selected-gain probability. Additional concrete signed-count vectors check the optimizer without sampling. In the completed run the script printed `PASS: 131 deterministic identity/comparison checks` and three sets of positive-burst probabilities.

The proof of fixed-load logarithmic growth uses bounds on infinitely many Skellam tail terms plus Stirling's formula, not numerical extrapolation. The sequential Gaussian/Gumbel asymptotic uses the exact moment-generating function and the standard normal tail equivalent. The script does not formally verify the infinite asymptotic arguments, experimental assumptions, or scientific priority. No external audit or certification was performed.
