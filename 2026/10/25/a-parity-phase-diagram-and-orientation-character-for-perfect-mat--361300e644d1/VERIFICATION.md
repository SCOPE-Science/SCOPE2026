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

# Reproducibility and scope

Run `python3 verify_theta.py` in a standard Python 3 environment. The standalone verifier constructs the two-terminal graphs and enumerates perfect matchings directly from graph adjacencies. It compares the exact matching count and all intersections of matching facets with the parity/nerve theorem. Selected small cases are checked by exact mod-two boundary ranks, and separate signed simplicial Lefschetz sums test symmetry actions. Expected successful output reports 1,424 graph cases, 182 full mod-two homology cases and 15 symmetry checks.

The proof of the infinite statement is the forced alternating matching argument followed by the simplicial nerve theorem, not extrapolation from these finite calculations. The program uses no network service or external mathematical package. Integral homology and the sign character are established mathematically; only mod-two finite homology is checked by the program. No independent scientific validation has been performed.
