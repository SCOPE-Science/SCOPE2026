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

The two accompanying Python 3 scripts are standalone and use only the standard library. Run `python3 verification/verify_clique_bouquets.py` and `python3 verification/verify_equivariance.py` from the package root. Their text outputs are included with the same stems and `.txt` suffixes.

The face checker separately performs graph-adjacency connected-component traversal and closed-form decomposition enumeration for each tested finite graph, then computes mod-two simplicial boundary ranks. All ten tested parameter sets pass. The equivariance checker directly computes oriented-face Lefschetz sums and separately computes exterior-power permutation characters for six cases. All six comparisons pass. The proof establishes the integral homotopy decomposition for every admissible parameter through an explicit simplicial pushout and a null attaching map; finite tests do not prove infinite families or integral torsion-freeness.

The classification does not cover arbitrary block graphs, and the homology representation statement is not an equivariant homotopy equivalence. Independent external scientific audit has not been performed.
