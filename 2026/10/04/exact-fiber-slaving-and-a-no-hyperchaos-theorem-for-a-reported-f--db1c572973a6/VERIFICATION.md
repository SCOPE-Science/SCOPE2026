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

The exact vector field was checked in the lawful open-access full text of the 2019 article.

`artifacts/verify_integral_spectrum.py` uses symbolic algebra to verify
\[
\dot Q=2zQ,\qquad Q=bx^2+ay^2,
\]
\[
rac{d}{dt}\left(rac{(w-1)^2}{Q}ight)=0,
\]
the base divergence \(2z\), the full divergence \(3z\), and the block-lower-triangular Jacobian with invariant pure-\(w\) direction.

The checker is only an algebra replay. The compact-support exclusion of \(Q=0\), the invariant-measure identity \(\int z\,d\mu=0\), and the Lyapunov-spectrum argument are proved analytically in `RESULT.md`; no finite-time numerical experiment is used as certification.

The exact first integral is valid wherever \(Q>0\). For \(a,b>0\), every compact invariant support is contained in that region because \(Q=0\) implies \(x=y=0\) and then \(\dot z=1\).
