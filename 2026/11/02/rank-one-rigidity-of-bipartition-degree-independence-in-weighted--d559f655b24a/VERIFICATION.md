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

# Reproducible mathematical checks

Run `python check.py` with Python 3 and the standard library. The script enumerates spanning trees of weighted \(K_{a,b}\) for fourteen small rational-weight examples, including rank-one and heterogeneous arrays at each of seven distinct part-size pairs. It computes each normalized joint ordinary-degree law and verifies the conditional hub formula, the inverse reconstruction, the independence-versus-rank-one equivalence, and the product of two multinomial laws in rank-one cases. The completed package checker was executed successfully.

The proof does not rely on extrapolation from finite computation. Its unrestricted steps are the positive-probability event decomposition, the exact expectation inversion, and the weighted matrix-tree determinant identity. All hypotheses and exceptional one-vertex/zero-weight boundaries appear in `RESULT.md`.

The computations do not verify historical originality or prove an infinite mathematical assertion on their own. No independent mathematical audit has been performed.
