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

The computation is supplementary finite validation of the algebraic theorem, not a replacement for the proof. Run `python verify_torus.py` (Python 3 standard library) with its working directory set to the folder containing this document and the script. It reconstructs binary adjacency matrices and computes ranks over \(\mathbb F_2\) by exact bitwise elimination. It checks both nullity formulas for 16 different parameter triples and 14 temporal powers each, for 224 paired matrix checks. It then enumerates 4096 trajectories on the 4-by-3 torus and checks the first-entry and least-period census exactly. The original replay output is included in `verification_output.txt`.

The infinite-parameter result rests on the explicit local-algebra proof in RESULT.md. The finite verifier does not address all odd factors or all field sizes; extension to arbitrary characteristic-two fields follows in the proof because ranks are unchanged by scalar extension and state counts depend on the field only through its cardinality. No independent audit has been performed.
