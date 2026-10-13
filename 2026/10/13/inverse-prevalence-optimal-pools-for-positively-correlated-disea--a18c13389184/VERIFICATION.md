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

# Verification of the correlated-pooling theorem

Run the bundled `verify.py` using Python 3; it requires only standard-library modules. The executable checker reconstructs the negative-pool probability with exact rational products and checks the adjacent-difference and normalized-ratio identities at 168 parameter/group-size combinations. It checks strict monotonicity of the ratio in the stipulated beta range and computes rare-prevalence and independent-case sample sizes using a separate iterative calculation.

Observed output from the bundled script:

`VERIFY_OK exact_adjacent_and_ratio_cases=168 correlated_examples=[(0.05, 25, 1.25, 0.215400014), (0.01, 106, 1.06, 0.060613632), (0.001, 1008, 1.008, 0.008458309)] iid_examples=[('1/100', 11, 1.1), ('1/10000', 101, 1.01)]`

The identity beyond the sample parameters is proved by symbolic algebra in RESULT.md, and the unrestricted limit is proved there by uniform logarithmic product expansion. Finite computations do not verify infinitely many parameter choices or independent novelty. A full earlier paper on exactly this correlated testing model could not be materially retrieved and remains an originality risk.
