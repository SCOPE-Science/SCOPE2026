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

# Reproducibility

Execute `python3 verify_mk.py` with Python 3.9 or newer. No third-party dependencies are needed. The output must exactly match `verification_output.txt`. The program generates the finite complex and group from the incidence triples, rather than trusting a precomputed list; it reconstructs signed simplicial boundaries and performs two independent modular quotient evaluations in degree three. The strict incidence counts, discrete-Morse acyclicity, integral critical boundary, point-group permutation classification, and complete character comparison are asserted in code.

This is an exact finite calculation, not an external mathematical audit. It proves no claim about other configurations or integral splitting of the rational group module.
