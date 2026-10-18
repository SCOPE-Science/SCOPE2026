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

# Verification record

The complete exact proof is in `RESULT.md`; the auxiliary `verify.py` checks the unsigned magnitude and sign of each base digit separately. It independently computes the Gaussian map without presuming the Pell identity, tests all bases \(2\le B\le120\), lengths \(1\le m\le4\), all signed real digits \(|a|<B\) and all nonzero signed repdigit digits \(|t|<B\), and compares the discovered fixed points with the predicted set. The scan is finite and is **not** a proof of the unbounded classification. The script separately verifies a dozen arbitrarily large Pell-derived examples under the actual digit map. Run `python3 verify.py`; it exits on any discrepancy and prints `VERIFY_OK` on success.

The infinite statements require only the algebraic digit decomposition, integer inequalities excluding other lengths, a Pell descent, and the monotonicity of hyperbolic cosine. The result is deliberately restricted to the repdigit-pattern class and does not establish the complete nonreal fixed-point spectrum of the Gaussian map. No independent audit has been performed.
