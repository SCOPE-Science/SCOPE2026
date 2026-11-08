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

From the package directory execute `python3 verification/check_cuboctahedral_fivecut.py`; only Python 3 standard-library modules are needed. This checker reconstructs every graph edge and facet without reading external data. It exhaustively checks all 4,096 subsets, two independently ordered acyclic face-poset matchings and all 15,576 Hasse incidences, then exactly computes integral signed Morse differentials and unimodular maximal-rank minors. It separately computes simplicial mod-two boundary ranks.

The expected literal output is embedded as `verification/check_output.txt`; a successful execution begins `CUBOCTAHEDRAL_FIVECUT_MIXED_WEDGE_VERIFIED`. The two integral reductions give forward 1,418 pairs, 15 critical five-cells, 121 critical six-cells and rank three; reverse 1,420 pairs, 13 critical five-cells, 119 critical six-cells and rank one. The full simplicial face vector is `(12, 66, 220, 495, 792, 872, 516)`.

**Limits.** Complete finite acyclic matchings and integer unit minors establish an integral homotopy equivalence for this graph only. The mod-two calculations are corroboration and alone would not prove torsion-freeness or an integral wedge. No independent external review or infinite-family classification has been performed.
