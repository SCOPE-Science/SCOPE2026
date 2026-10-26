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

# Verification of the weighted-cube trace-norm classification

The universal classification follows from the proof in `RESULT.md`: trace-norm metric-segment equality, positivity of the common polar preimages, orthogonality of singleton supports, and a trace-saturation argument. In particular, the absence of embeddings below the dimension bound does **not** come from computation.

The standalone Python program `checker.py` requires NumPy. Run it using `python checker.py` in a directory containing this file; no input data or network is required. The deterministic reference run printed:

`PASS: 104261 finite diagnostics (floating complex matrices and exact integer witnesses)`

The diagnostics cover weighted cubes of dimensions three through six embedded by random complex rectangular partial isometries, cases with nontrivial higher-rank positive blocks, and complete integer-diagonal Hamming-distance identities for dimensions three through eight. The checker is independent of any other package path and uses no saved test log. Numerical tests do not establish the universal rigidity or minimal matrix size. No independent audit has been performed.
