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

# Verification

The included `verify_sp4.py` is a standalone standard-library Python 3 program. Invoke `python3 verify_sp4.py`; a successful run prints `VERIFY_OK`, the exact nine trace coefficients, and the seven-value completion histogram. Assertions compare two differently expressed exhaustive searches with the independently displayed target coefficient table and total.

The first search enumerates all ternary symplectic column pairings, and the second enumerates all quadruples of ternary two-by-two blocks satisfying the exact matrix identities. Both use integer arithmetic only; neither uses random sampling, numerical tolerance, external packages, a network connection or an unprovided data file. The computations concern only the exact finite box. They do not verify asymptotic properties, larger radii, or literature priority.
