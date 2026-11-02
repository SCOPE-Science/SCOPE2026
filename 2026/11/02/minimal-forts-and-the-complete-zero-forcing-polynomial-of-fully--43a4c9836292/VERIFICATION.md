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
# Verification of the zero forcing and minimal-fort enumerators

The standalone `verify.py` constructs the one-edge full subdivision from the graph definition, implements ordinary blue-vertex zero forcing with a deterministic maximal closure, and computes minimal forts directly from the neighborhood criterion. For n = 3, 4, 5, it exhausts all 2^(n + binom(n,2)) vertex sets, compares direct zero forcing with the forest-and-original-vertex criterion and checks all polynomial coefficients. It also checks the minimal-fort classification directly. Separately, labeled trees are enumerated using Prüfer words for n = 3 through 7 and the resulting optimal set counts are checked. The program terminates with `VERIFY_OK` on successful checks.

Directly checked minimum-seed counts are 6, 60, and 620 for n=3,4,5, respectively. The all-parameter proof is the cut-neighborhood classification of the minimal forts, the fort-hitting equivalent of ordinary zero forcing, the labeled forest exponential formula, and the unique excluded centered star for each singleton original vertex. Computational verification of finitely many n does not imply the infinite formula. Independent audit was not performed.
