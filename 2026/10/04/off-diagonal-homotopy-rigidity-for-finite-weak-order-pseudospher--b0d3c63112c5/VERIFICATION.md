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

The symbolic proof was checked step by step against the exact hypotheses. Its critical points are: consecutive source-level image intervals are ordered; a shared target boundary level can contain only one image point; \(h\) strictly separated nonempty image intervals inside \(h\) target levels force level \(i\) to map into level \(i\); a singleton occupied target level makes the image contractible; and a special map cannot have a distinct pointwise-comparable neighbor.

The homology calculation uses the join decomposition of the order complexes and the elementary fact that a set map with image size \(s\) induces a reduced degree-zero homology map of rank \(s-1\).

`artifacts/verify.py` exhaustively enumerates all set maps in four unequal three-level cases, filters order-preserving maps, computes connected components under pointwise comparability, identifies isolated maps, and checks the predicted top-homology rank for every isolated map. Its recorded output is in `artifacts/verification_output.txt` and ends with `VERIFY_OK`.

The finite computation is not an exhaustive proof for arbitrary level sizes or height. No independent audit or independent validation has been performed.
