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

# Verification and reproducibility

Running `python verify.py` using Python 3 standard libraries prints `VERIFY_OK`. The verifier enumerates unrestricted difference vectors independently of the closed finite sums, checks \(\delta_a\) and \(\omega_{ab}\) for \(2\le q\le5\), \(1\le r\le3\), and exhaustively compares finite ball counts when at most two coordinates are near the boundary. It independently enumerates **all** ternary compositions for \(6\le n\le21\), compares the six volume frequencies, and recomputes the exact first two deficit moments and variance using rational arithmetic.

The stored `verification_output.txt` is the observed standalone execution output. It is not a substitute for proof: no finite enumeration can certify the infinite asymptotic statement. That statement follows from the exact boundary-count formula, fixed-degree binomial expansions, and the order-\(n^{-3}\) bound on configurations with three or more small coordinates. No external audit is represented by this file.
