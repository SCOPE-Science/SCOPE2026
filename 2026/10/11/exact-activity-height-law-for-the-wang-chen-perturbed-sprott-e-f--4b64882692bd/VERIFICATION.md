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

The claim is analytic. For a compactly supported invariant probability measure \(\mu\), invariance gives \(\int Lf\,d\mu=0\) for polynomial test functions \(f\). Applying this to \(f=z,y,x\) gives \(\int x=1/4\), \(\int y=\int x^2\), and \(\int yz=-a\). The exact identity \(\dot z=-4(x-1/4)\) then gives
\[
A=\int \dot z^{\,2}d\mu=16\left(\int x^2d\mu-\frac1{16}\right),
\]
which yields the activity–height formula after normalization by \(\int y=(1+A)/16\).

Positivity of \(y\) on compact invariant supports is obtained from the exact stable-filter representation of \(\dot y=x^2-y\) along bounded complete trajectories. The equality case \(A=0\) is proved by support collapse and invariance, not by numerical tolerance.

`verify.py` uses only the Python standard library. It checks the printed vector field algebraically, verifies the equilibrium exactly, and verifies the moment conversion formulas with rational arithmetic. Its expected output is `VERIFY_OK`.

The verification does not attempt to certify existence of the numerically reported periodic or chaotic attractors, and it does not convert finite trajectory averages into invariant-measure statements. Those are explicit limits of the claim.
