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
# Reproduction and scope of verification

Run `python verify.py` with Python 3, using only its standard library. The script constructs every edge directly from two clique layers with a matching between layers, then checks open-neighborhood domination and distinct signatures of all unselected vertices for each of the \(2^{2n}\) subsets at each \(2\le n\le9\). Every outcome is compared against both the structural conditions and the closed coefficient formula. It also tests minima and leading coefficients of the symbolic formula for \(4\le n\le200\).

The output is reproduced in `verification-output.txt`. Exactly 349,520 candidate subsets are examined in the exhaustive range. These are finite computations; the combinatorial argument in `RESULT.md` proves the claim for arbitrary integer \(n\ge2\). No independent audit or externally certified proof is asserted.
