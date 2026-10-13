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

The proof is symbolic. The key identity is the exact PSB error projection \(R^+=(I-pp^T)R(I-pp^T)\), followed by commutation of projectors from a fixed orthogonal basis.

`artifacts/verify_psb_batching.py` uses exact rational arithmetic to check the masking law and invariant greedy scores on a non-diagonal positive-definite instance. It also simulates a sharp diagonal case with \(n=5\) and \(t=1\), confirming that five nontrivial PSB updates require three completed outer iterations and that the next primal step is the first exact minimizer for the chosen initial error.

The finite script is supporting evidence only. The general count and sharpness argument are proved in `RESULT.md`.
