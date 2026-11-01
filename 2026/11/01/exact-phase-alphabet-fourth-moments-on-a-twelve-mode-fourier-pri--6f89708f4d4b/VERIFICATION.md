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

The exact certificate is `CHECK.py`, which uses Python 3 and the standard library. Run `python3 CHECK.py` to enumerate all 1,751,969 normalized configurations, using Gaussian and hexagonal integer-pair arithmetic; the completed output is `CHECK_OK 1751969 exact normalized arrays`.

The program checks the complete support convolution formula for every configuration, the four exact minima and smallest nonoptimal values, the complete equality counts, and all geometric/conjugation orbit representatives and sizes. It also evaluates the independent aperiodic autocorrelation representation on every winner and on additional nonwinners. The proof's normalization shows why exactly those configurations exhaust the finite-alphabet domain; the no-alias condition on finite grids is analytic.

The validation is not an independent audit and does not cover continuous coefficient phases, other support sets, or phase alphabets other than 2, 3, 4, and 6.
