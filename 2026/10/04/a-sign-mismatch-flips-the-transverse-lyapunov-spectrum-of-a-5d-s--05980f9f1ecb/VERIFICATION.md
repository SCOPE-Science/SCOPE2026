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

The exact checks concern the printed system
\[
\dot x=yz,\quad \dot y=x-y,\quad \dot z=1-x^2,\quad \dot w=-3s-x,\quad \dot s=w-ds,
\]
with \(d>0\), and the comparison plus-sign variant obtained only by replacing the last equation with \(\dot s=w+ds\).

`verify.py` uses only the Python standard library. It checks:

- the two printed-system equilibria by direct substitution;
- the minus-sign and plus-sign equilibrium polynomial expansions;
- divergence \(-1-d\) versus \(-1+d\);
- strict negativity of both minus-sign fiber exponents for representative values on both sides of \(d=\sqrt{12}\);
- the exact transverse real parts \(-499/1000\) and \(+499/1000\) at \(d=499/500\);
- the source's reported Lyapunov sum \(0.4976+0.4942+0.1737-0.0002-1.1673=-0.002\), matching the plus-sign divergence at \(d=0.998\).

The proof that the full spectrum is the union of base and fiber spectra is structural: the vertical tangent subbundle is invariant and carries the constant fiber cocycle, while the quotient cocycle is the Sprott-C variational cocycle. The proof that the base has at most one positive exponent on a non-equilibrium compact ergodic measure uses its autonomous zero flow exponent and constant divergence \(-1\).

The replay does not numerically integrate trajectories and therefore does not attempt to reproduce finite-time Lyapunov estimates or establish existence of a particular chaotic attractor. Those are outside the claim.
