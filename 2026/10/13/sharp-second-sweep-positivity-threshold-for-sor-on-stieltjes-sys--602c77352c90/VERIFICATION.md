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

The analytic verification uses the normalized SOR splitting
\[
T=(I-\omega L)^{-1}((1-\omega)I+\omega U)
\]
and the exact nilpotent expansion of \((I-\omega L)^{-1}\). The coefficient minimum occurs at path length \(n-1\), yielding the boundary \(\omega=(n+1)/n\).

`verify.py` uses only exact rational arithmetic. It reconstructs the second-iterate matrix for \(n=3\), \(\omega=7/5\), \(\varepsilon=1/10\), checks the SPD principal minors, verifies
\[
(x^{(2)})_3=-\frac{68943}{15625000}<0,
\]
and checks the closed endpoint-entry formula. It also verifies the boundary coefficient signs for a finite range of dimensions as a regression test. Those finite checks do not certify the arbitrary-dimensional statement; that statement rests on the displayed symbolic identities.

Limits: standard forward SOR, zero start, real SPD Stieltjes matrices, exact arithmetic, and only sweeps one and two are covered. No independent audit has been performed.
