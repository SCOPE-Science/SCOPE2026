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
For the doubling Perron operator \(P\), the proof uses
\[
P\cos(2\pi\cdot)=0,
\qquad
P\cos(4\pi\cdot)=\cos(2\pi\cdot).
\]
The packaged `verify.py` checks the resulting coefficient recurrence for
\[
s(x)=\frac1{2(1-\alpha^2)}+\frac{\alpha^2}{2}\cos(2\pi x)+\frac12\cos(4\pi x),
\]
verifies that subtracting \(\cos^2(2\pi x)\) gives the stated conditional variance, and checks the exact lower endpoint
\[
\frac{\alpha^4}{2(1-\alpha^2)}.
\]
The stored checker output is `VERIFY_OK`.

The conditional-moment equations and their uniqueness are analytic consequences of invariance, the Lebesgue first marginal, and \(|\alpha|<1\); no finite orbit computation is used as proof.
