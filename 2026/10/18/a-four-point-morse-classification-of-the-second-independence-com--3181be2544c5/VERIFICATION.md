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

# Reproducible verification

Run `python3 verify_kneser.py 5 6 7 8 9 10 11 12` using Python 3.10 or later; no third-party packages are required. The program explicitly implements disjointness degree at most one, enumerates all subsets satisfying this condition, builds the universal four-point matching, checks each matching incidence and all Hasse orientations, and performs directed topological sorting to detect cycles. An assertion failure exits nonzero.

The 37-face universal filter always has 18 matched covering pairs and one critical four-element face. This is the *complete* universal local computation used by the all-order proof, not a sample of larger graphs. Independently the full-order checks return face totals (including empty) \(261,747,1751,3635,7006,12956,23574,43034\) and critical three-cell counts \(1,5,15,35,70,126,210,330\) for orders five through twelve. The last order checks \(204072\) cover relations. Every finite Hasse digraph is checked exhaustively for acyclicity.

The proofs that the only possible class-B block is this six-bit filter, that class-A pivot toggles are valid for every order, and that the patchwork projection is order-preserving are mathematical arguments in `RESULT.md`. The program alone does not certify infinitely many orders. No external mathematical audit has been performed.
