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

The proof is self-contained. Exact identities are certified by polynomial expansion in `CHECK.py` and in the proof. The checker uses symbolic arithmetic for the data Gram matrix and the completed-square identity, then independently minimizes representative smooth finite-dimensional regularized objectives from multiple starts.

Run: `python CHECK.py` with Python 3, NumPy, SciPy and SymPy installed. Each reported numerical check is a diagnostic, not a universal certificate. The analytical lower and upper variational bounds independently prove the limiting rates, and the necessary compactness assertions are established in `RESULT.md`.

Scientific boundary: only \(0<\gamma<1\), \(\beta>0\), full-rank three-by-two data matrix and rank-one penalty \(L=(1,0)\), with \(\varepsilon\downarrow0\) and other parameters fixed. No independent audit has been performed.
