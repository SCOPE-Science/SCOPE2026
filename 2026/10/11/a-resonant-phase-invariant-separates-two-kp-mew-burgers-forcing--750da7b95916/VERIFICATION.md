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

Run `python verify.py` with a standard Python 3 interpreter. The checker has no third-party dependencies and uses exact rational polynomial arithmetic. The expected output is `VERIFY_OK`.

It verifies the four polynomial identities
\[
\dot I_1=0,\qquad \dot I_2=0,\qquad \frac{d}{d\zeta}\operatorname{Re}K=0,\qquad \frac{d}{d\zeta}\operatorname{Im}K=0
\]
for the resonant oscillator field \(\omega_2=2\omega_1\), together with
\[
|K|^2=I_1^2I_2.
\]
It then evaluates the Figure 11(b) oscillator initialization exactly and obtains
\[
K=\frac{117-44i}{125},\qquad I_1=I_2=1.
\]
The printed forcing leaf is checked at its canonical phase point as \(K=1\); constancy of \(K\) then covers every common time translate.

The checker does not integrate the nonlinear \(u,v\) dynamics or recompute Lyapunov exponents. The accepted theorem does not require either operation.
