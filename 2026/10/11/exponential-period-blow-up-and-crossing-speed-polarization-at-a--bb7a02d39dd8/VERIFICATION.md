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

The analytic checks are the identity \(\dot w=-x(2w^2-bw+1)\), the integration formula for \(I_b\), the two-axis limits of \(A^2we^{-2I_b(w)}\), the full-period quadrature, and the elementary Laplace method with the endpoint \(\cos(\pi/2-s)\sim s\). These provide full mathematical proof for every \(A>0\) and \(|b|<2\sqrt2\).

Run `python checker.py` after installing `requirements.txt`. Its numerical tests compare the exact gamma expression with quadrature, check the asymptotic limiting constant along a prescribed sequence, and verify the crossing-speed ratio using high precision. The checks cover finitely many parameters only; no claim of exhaustive numerical verification is made. The provenance comparison inspected the primary global-center article in full HTML and a closely related earlier period-function work only in part.
