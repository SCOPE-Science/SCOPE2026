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

# Reproducibility

The standalone `artifacts/verify.py` uses Python 3 with no third-party dependencies. Run from the extracted directory by `python3 artifacts/verify.py`; a successful complete execution prints `VERIFY_OK`.

Over \(\mathbb F_2\) and \(\mathbb F_3\), the program multiplies two explicit \(4\times4\) upper-triangular matrices for every ordered pair, constructs the full commutator histogram, and compares every derived target fiber with the formulas. For \(\mathbb F_4\) and \(\mathbb F_5\) it exhaustively traverses all \(q^6\) first operands, derives the linear adjoint image from their matrix columns, enumerates every image and its kernel size, accumulates the complete fiber histogram, and checks all targets and predicted ranks. The \(\mathbb F_4\) arithmetic uses the irreducible polynomial \(t^2+t+1\).

One complete replay produced the following zero-target counts: for field sizes \(2,3,4,5\), respectively, \(1024,41553,557056,4140625\). It also checked that the number of ordered pairs was \(q^{12}\) in each field and that the target image was all of \([N,N]\). These exhaustions cover their stated small fields only; the general prime-power assertion uses the analytic rank and Fourier proof in `RESULT.md`.

The result has undergone self-review but not independent audit.
