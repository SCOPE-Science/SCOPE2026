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

# Computational verification

Both `verify_primary.cpp` and `verify_secondary.py` use only standard C++17 or Python 3 libraries and contain executable assertions for all displayed counts. The first builds the cyclic Fano incidence graph; the second builds the incidence graph from nonzero vectors of \(\mathbb F_2^3\). Both recurse over all possible first classical pebbling moves; each lowers total size by exactly one, ensuring termination and exhaustive reachability. All \(\binom{t+13}{13}\) distributions at \(t=5,6,7,8\) are generated. Every legal unit jump and edge slide within the solvable subset is generated, and its connected-component multiset determined by disjoint-set union.

Primary check output includes `OPTIMUM_PROFILES_OK`, `CAPACITY_BARRIER_OK`, and `EXHAUSTIVE_PRIMARY_OK`. Second check output includes `OPTIMUM_PROFILES_OK`, `CAPACITY_BARRIER_OK`, and `INDEPENDENT_FANO_CERTIFICATE_OK`. Neither program certifies extrapolation beyond total eight, nor searches the external literature. No independent scholarly validation has been performed.
