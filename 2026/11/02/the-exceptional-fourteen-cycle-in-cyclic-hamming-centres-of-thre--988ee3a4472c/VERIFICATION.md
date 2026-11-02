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

Run `python3 verify.py` from the folder containing this file. Requires only Python's standard library. Expected terminal line:

`VERIFY_OK: finite full census n=3..26; independent rotation-Hamming distances n=3..17; extremal bounds`

The script constructs every three-subset for each tested length, canonicalizes rotation orbits, derives a separation profile for each orbit, and independently computes shifted Hamming distance for every pair of necklace orbits through length 17. It checks all optimum radii and optimum counts for lengths 3–14, explicitly checks the two fourteen-position centres, and extends the predicted radius-four regime through length 26. It also tests the numerical inequalities used in the analytic proof. It is *not* a certificate of the infinite-size theorem; that theorem uses the Cauchy–Davenport inequality, Mantel's theorem, and the classification of the extremal complete bipartite graph.

This work has undergone the stated self-review only; independent scientific audit has not been performed.
