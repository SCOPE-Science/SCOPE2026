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

For the printed generalized Lorenz vector field, define \(z_*=R+s_1d/s_2\) and \(H=xy-(s_1+d)x^2/(2s_2)\). Direct expansion gives
\[
\dot H=\frac1{s_2}(-s_1x+s_2y)^2-x^2(z-z_*).
\]
For a compactly supported invariant probability measure, integrating this Lie derivative gives zero and therefore yields the exact claimed balance.

The equality case was checked separately. Vanishing of the square forces \(y=(s_1/s_2)x\) on the invariant support. The second equation then gives \(x(z_*-z)=0\). The branch \(x=0\) reduces to \(\dot z=-qz\), whose only compact invariant probability measure is the origin mass. The branch \(x\ne0\) gives \(z=z_*\) and then \(x^2=q(s_1d+s_2R)/s_1\), exactly the two nonzero equilibria.

`verify_generalized_lorenz_balance.py` symbolically checks the coboundary and equilibrium substitutions. It does not search for invariant sets or infer asymptotic dynamics from finite simulation.
