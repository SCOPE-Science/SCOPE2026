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

The two provided Python programs reconstruct the exact cellular model for two unordered particles, enumerate all simple cycles and disjoint pairs without sampling, and compute integral Smith forms. `verify.py` verifies the chain boundary identity, the degree-two integer Smith invariants, the complete graph automorphism set, all torus relations by cycle length, and a twenty-by-twenty unimodular minor of one symmetry orbit. `check_character_direct.py` independently constructs the homology action of all ninety-six graph automorphisms on the selected integral torus basis and recovers the rational trace distribution.

Reproduction requires Python 3.10 or later, SymPy and NetworkX as specified by `requirements.txt`; no external datasets are used. The computations constitute complete finite checks for the *specified graph*, not extrapolation to an infinite family. The mathematical identification of the cubical model with the continuous configuration space uses the stated published subdivision theorem; the code does not reprove that topological theorem. Scientific priority relative to inaccessible or unpublished work is not mechanically certified.
