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

# Verification notes

Run `python verify_sprott_g.py` in an environment with Python 3 and SymPy installed. The checker recomputes the identity \(\dot H+H=-(a+1/2)x^2/b\), the change-of-coordinates Jacobian \(-b\), the conjugated differential equations, and the energy derivative \(\dot{\mathcal E}=-v^2/2+bhv\). It also verifies the equilibrium points, planar linear characteristic polynomials and the potential gap \(2b^3/3\) between the two stationary points (absolute value taken according to saddle–sink ordering).

The proof of bounded orbit convergence uses integrability and uniform continuity. The proof of heteroclinic existence uses the unstable manifold theorem, an energy barrier on the left branch, and bounded forward convergence. The uniqueness assertion uses alpha/omega limits and strict energy dissipation. These arguments cover all real nonzero \(b\), including the sign reversal, and do not rely on numerical integration.

The case \(b=0\) is treated without dividing by \(b\); its separate variation-of-constants estimate proves boundedness and convergence. No symbolic script constitutes an infinite-domain proof of the global phase portrait. Independent audit is not yet performed.
