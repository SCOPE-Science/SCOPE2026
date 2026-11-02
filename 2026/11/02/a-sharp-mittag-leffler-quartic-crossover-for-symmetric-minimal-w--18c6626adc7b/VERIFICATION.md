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

# Finite checks and analytic proof boundary

Run `python3 verify.py` using Python 3.11 or later and its standard library, in the directory containing the extracted package. The recorded output is in `verification_output.txt`.

The program independently checks the exact movement-clock recursion for three rational parameters and eighteen horizons, exact rising-factorial identities, normalized mass and support, direct versus recursive finite-binomial tails, the first three even terms of the fair-sign Cramér rate, finite examples of a Gaussian-tail comparison, and numerical approach toward the sharp quartic factor.

All 2,088 finite assertions passed in the packaged run. The checker does not simulate an infinite clock, establish an almost-sure limit, or prove a probability asymptotic from enumeration. The infinite claim follows from the detailed proof in `RESULT.md`, including exponential tilting with a Berry–Esseen remainder, the cited global normal-tail comparison and the positive Mittag–Leffler clock limit. No external certification has been performed.
