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

# Computational verification and boundaries

Run `python3 verify.py` with Python 3 standard library. It rebuilds original graph edges rather than importing research artifacts. It constructs permutation orbits, discards non-independent top-layer orbits, calculates orbit adjacency from original graph edges, verifies each neighborhood inclusion used in the collapse, and compares the terminal graph exactly with the claimed graph. The tested 117 parameter triples include derangements with multiple disjoint cycles, permutations with one or more fixed labels, different cycle lengths, and depths zero through eight. Signed invariant-face enumeration checks 37 reduced Lefschetz numbers; separate mod-two boundary ranks check 28 small homology cases.

The exact recorded standard output appears in `verify_stdout.txt`. A successful run prints `VERIFY_OK orbit_graph_folds=117 signed_full_Lefschetz=37 complete_mod2_homologies=28`.

Finite computational checks cannot certify every parameter; the proof uses uniform neighborhood inclusions and the known homotopy theorem for the reduced graph. The signed Lefschetz calculation corroborates, but cannot replace, the direct fixed-point simple-homotopy argument. Integer homotopy classes are justified by elementary collapses and the cited integral homotopy classifications, not by mod-two ranks alone. No independent scientific audit has been performed.
