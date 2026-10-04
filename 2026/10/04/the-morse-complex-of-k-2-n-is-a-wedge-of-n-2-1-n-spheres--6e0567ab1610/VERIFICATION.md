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

`verify_k2n_morse.py` is a standalone Python verifier using only the standard library. It constructs all augmented faces from the defining matching and directed-cycle constraints, applies the exact sequential element matching, and compares its unmatched set against the closed-form critical families.

The replay checks every integer \(1\le n\le7\). For \(1\le n\le6\), it additionally orients every Hasse edge according to the discrete-Morse matching and topologically sorts the full directed Hasse graph to verify acyclicity directly. It also checks
\[
\chi(\mathcal M(K_{2,n}))=1+(-1)^n(n^2-1).
\]
A successful replay ends with `VERIFY_OK`.

The finite replay is not used as an infinite proof. The all-\(n\) theorem depends on the survivor induction in `RESULT.md`; the computation stress-tests that induction, the \(n=1\) boundary case, and the critical-cell count.
