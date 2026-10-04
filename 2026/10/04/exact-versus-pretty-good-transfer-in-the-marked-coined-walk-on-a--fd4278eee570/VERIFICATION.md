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

The proof uses the exact source formula
\[
\mathcal F_N(2t)=\sin^4(\omega t/2),
\qquad
\cos\omega=(N-4)/N.
\]
Unit fidelity is reduced to a root-of-unity condition. If \(\omega/\pi\) is rational, then \(2\cos\omega\) is a rational algebraic integer and therefore an integer, yielding only \(N=2,4,8\). For all other integer sizes, irrational-rotation density proves pretty-good transfer and excludes exact equality.

`verify_star_transfer.py` reconstructs the source's effective two-step \(3\times3\) matrix and compares direct matrix evolution with the closed fidelity formula over a finite test grid. It verifies the three exact exceptional sizes and searches representative nonexceptional sizes for high-fidelity integer-time witnesses. The replay prints `VERIFY_OK`.

The finite computations are supplementary and do not prove the all-size classification. The result has not undergone an independent audit.
