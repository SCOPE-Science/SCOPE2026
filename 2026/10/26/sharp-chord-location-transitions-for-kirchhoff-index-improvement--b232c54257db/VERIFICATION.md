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

The exact-rational standalone `verify.py` checks the one-edge rank-update formula against direct Kirchhoff indices obtained by inverting the grounded weighted Laplacian and sums all pair resistances. It exhaustively considers all nonadjacent endpoint pairs for every path order from 4 through 12, over a finite set of positive rational weights including exact claimed critical values and perturbations to either side. Execution produced `VERIFY_OK exact_laplacian_chords= 1587`. The closed-form proof, not finite testing, is the reason the claim applies to arbitrarily large orders and all positive real edge conductances. Numerical interpolation, randomized testing, and independent audit are not claimed.
