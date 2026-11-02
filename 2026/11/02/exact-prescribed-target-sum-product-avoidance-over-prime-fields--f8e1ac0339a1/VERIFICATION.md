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

Run `python3 verify.py` in a Python 3 interpreter with standard-library modules only. The script constructs graph components, computes maximal independent-set sizes through a two-state path/cycle dynamic program, obtains orders of projective transformations by iterating the point at infinity, and verifies the theorem's two predicted sizes and exact exceptional target counts for every prime between five and 199. For primes through seventeen, it also compares with a separate exhaustive enumeration of all subsets by bitmask.

The observed output from the packaged file was:

`VERIFY_OK prime_fields=44 target_cases=4178 exhaustive_bitmasks=48`

The verification covers finitely many fields; infinite validity depends on the projective orbit and cyclic-torus proofs in RESULT.md. No independent audit has been performed.
