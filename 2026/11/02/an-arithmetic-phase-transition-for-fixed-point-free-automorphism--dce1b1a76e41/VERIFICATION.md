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

# Reproducibility and verified checks

Run `python3 verify.py` in a Python 3 environment with no third-party dependencies. Its deterministic output is saved in `verify_output.txt`. The checker defines field addition, multiplication and inversion, including polynomial-basis extension fields of orders four and eight. It constructs the original Lie bracket, generates automorphism columns recursively, verifies all nonzero and zero original basis bracket relations in exhaustive cases, and calculates ranks of the complete automorphism matrices and their differences with the identity.

The exhaustive configurations are (n,q)=(4,2),(5,2),(4,3),(4,4),(4,5), covering all free shear coefficients for all nonzero a,d. The additional configurations (5,3),(6,4),(5,5),(8,7),(8,8),(5,8),(12,7),(8,11) test all multiplicative pairs and four shear assignments per pair; these are not exhaustive over shears. The implementation separately computes Euler's totient divisor sum and an independent direct enumeration of multiplicative pair eligibility in every configuration.

All 13 checks passed, and the output ends with `FILIFORM_FIXED_POINT_FREE_COUNTS_OK 13_CONFIGURATIONS`. Finite checks are corroboration only; the general theorem rests on the symbolic centralizer and multiplicative-order proof. Independent audit has not been performed.
