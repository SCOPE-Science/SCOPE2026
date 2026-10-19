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

The packaged `verify.py` uses only the Python standard library. Running `python verify.py` computes all cliques for the ranks \(2\le n\le5\), independently applies literal partial-map multiplication to all vertex pairs, and checks maximal-face counts, mod-two reduced Betti numbers, and exact **integer Lefschetz traces** for a label transposition, a cyclic label permutation, global inversion and their combinations. Every case matched the predicted sign character; output ended `VERIFY_OK_RANK_ONE_COMMUTING_EQUIVARIANT`.

Integral torsion-freeness and the result for arbitrary \(n\) follow from the proof's homotopy-equivalence argument, not from these finite mod-two calculations. This is not independent mathematical validation.
