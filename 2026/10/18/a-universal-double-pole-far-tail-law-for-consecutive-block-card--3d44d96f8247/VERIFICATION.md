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

# Reproducible checks

The supplied `verify.py` is standalone Python standard-library code. Execute `python3 verify.py` to obtain the `VERIFICATION_OK 1237 exact checks` output. It enumerates the one-step merger probabilities from all permutations of lengths two through seven, independently propagates exact rational distributions for initial counts two through ten through fifty steps, compares the explicit survival expressions at initial counts two through four, verifies the annihilating polynomials for spectral remainders, and verifies strict ordering of the transient diagonal probabilities in the implemented range.

All calculations are finite checks; they do not by themselves establish the all-size theorem. The proof's core nonstandard steps are the duplicate-eigenvalue Jordan link from three to two, the strict separation of all other diagonal entries, and positivity of the recursively computed linear coefficient. The proof addresses those steps analytically. Independent audit has not been performed.
