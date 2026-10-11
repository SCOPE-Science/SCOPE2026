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
# Reproducibility of the finite calculation
Run `python3 verify_ranking_rips.py` and `python3 verify_persistence.py` with Python 3.9 or newer. Both programs have no third-party imports or auxiliary input files. The former prints `VERIFY_OK` after exact checks of the 576 pairwise distances, shortest-path diameter six, 12 maximum-distance pairs, every face vector and mod-two boundary rank at scales zero through four, and the degree-two scale-two-to-three image rank. The latter directly sorts and reduces the filtered boundary matrix of all 17,372 simplices through scale four and prints `PERSISTENCE_OK` after matching every surviving nonzero-length barcode interval there.

The scale-five complement is checked to be 12 disjoint edges, whose independence complex is the 12-fold join of \(S^0\), hence \(S^{11}\); the scale-six complex is the full simplex. The calculation is exhaustive **only** for the specified 24-point metric and field \(\mathbb F_2\). In particular, it does not certify integral torsion, a general formula for larger permutation groups, or an independent audit.
