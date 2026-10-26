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

The theorem is an analytic identity for every real \(\beta>-1\), integer \(k\ge0\), and \(t\in[0,1]\). The proof uses the shifted Jacobi ODE, a parameter-contiguous derivative identity, the standard Jacobi square norm, and strict interlacing of derivative zeros. Those are the infinite-family arguments. The finite checks below are supplementary diagnostics, not a certification of infinitely many cases.

Run `python verify_jacobi_crossings.py` from the same directory using Python 3 with SymPy and SciPy installed. The script verifies a symbolic differentiated boundary identity with abstract coefficients, then 35 exact polynomial-integral instances for \(k=0,\ldots,6\) and \(\beta\in\{-1/2,0,1/3,1,5/2\}\); it also tests representative endpoint signs and root brackets. The accompanying `verification_output.txt` is the output of this command.

The checker does not establish novelty, the general Jacobi zero theorem, or any multi-mode operator-theoretic property. No independent audit has been performed.
