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

`verify.py` reconstructs
\[
\dot x=y(a-z),\qquad \dot y=z(x-b),\qquad \dot z=x(c+y)-dz
\]
and checks, with symbolic algebra, that at \(d=0\):

- both \((0,0,0)\) and \((b,-c,a)\) satisfy all three equilibrium equations;
- the Jacobian characteristic polynomials are \(\lambda^3+abc\) and \(\lambda^3-abc\);
- the divergence is \(-d\), hence vanishes identically when \(d=0\).

The exhaustive equilibrium count additionally uses the proof's exact case split \(z=0\) versus \(z\neq0\) under \(abc\neq0\). The script does not attempt to classify the excluded degenerate cases or establish any global recurrent dynamics.

Recorded execution output: `VERIFY_OK`.
