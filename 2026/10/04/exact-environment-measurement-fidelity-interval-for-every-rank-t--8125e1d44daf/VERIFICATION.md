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

The proof was reconstructed from the fixed-Kraus feedback formula and the qubit determinant identity. Every finite Kraus representation of a minimal rank-two channel is represented by an isometry with two orthonormal columns. In a Takagi Kraus basis,
\[
\det B_k=s_1x_k^2+s_2y_k^2.
\]
Triangle and reverse-triangle inequalities give the exact global endpoints, and explicit two-outcome unitaries attain them.

`verify_rank2_feedback.py` uses only the Python standard library. It checks amplitude damping and dephasing, verifies determinant-form singular-value invariance under deterministic random minimal-Kraus unitary remixings, and stress-tests the sharp bounds on deterministic random trace-preserving rank-two channels with finite Kraus refinements containing two through six outcomes. It prints `VERIFY_OK`.

The finite replay is supplementary. The general theorem is supplied by the analytic proof in `RESULT.md`.

No independent audit has been performed.
