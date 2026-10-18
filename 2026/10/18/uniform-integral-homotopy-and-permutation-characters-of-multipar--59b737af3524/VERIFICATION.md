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

# Reproducibility checks

From the directory containing the scripts and recorded outputs, run `python pft_general_verify.py` and `python pft_symmetry_verify.py`. Both require only the Python standard library. The first enumerates all simple paths by depth-first search, builds every face and checks all mod-two boundary ranks for 67 graph/threshold configurations on at most nine vertices. The second checks all class-preserving permutations in five small multipartite parameter sets, comparing direct signed fixed-face counts with the polynomial character in 1,008 cases. Expected exact command output is recorded in the adjacent text files.

The chain-rank tests are over a finite field and do not constitute an integral torsion or infinite-parameter proof. The argument establishing the integral lattice saturation, homotopy classification, and full character appears in `RESULT.md`. No independent external audit has been performed.
