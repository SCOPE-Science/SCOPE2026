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
# Reproducibility and scope

Run `python verify.py` in an environment providing SymPy. The checker constructs the full Gram and kernel-normal matrices, the prescribed block factors, exact rational preconditioned active matrices, minimal-polynomial Krylov ranks, and a homogeneous orientation control. It checks the derived determinant and secular exclusions for each integer \(2\le q\le7\), and performs exact preconditioned-CG and unpreconditioned-CG recurrences for \(2\le q\le5\). The script checks \(78\) exact symbolic assertions in its main loop, plus eight exact CG termination assertions. This finite verification is supplementary: the proof covers all integers \(q\ge2\) by analytical secular interlacing and Jensen's inequality.

No random sketch performance, floating-point stability, practical tolerance, wall-clock cost, or historical priority has been independently verified. No independent mathematical audit has been performed.
