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

The all-parameter proof is symbolic and is given in `RESULT.md`. The attached `verify.py` is an independent finite replay for the first three nontrivial parameters. It enumerates all set maps for \(q=2,3,4\), filters exactly the order-preserving maps, constructs connected components of the pointwise-comparability graph, and computes images of an integral cycle basis of \(K_{2,q}\).

The replay confirms that the nonzero-\(H_1\) maps are exactly the isolated maps and that the total-map, null-component, and homotopy-class formulas hold in all three checked cases. `verification_output.txt` records the exact output and terminates with `VERIFY_OK`.

Limits: finite replay at \(q=2,3,4\) is not a proof for all \(q\); the universal statement rests on the case-split proof. No independent audit has been performed.
