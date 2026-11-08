---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS. For complete Poisson resets of (Z,U,theta) in the stated two-dimensional inertial active Brownian SDE, exponential renewal age and the integrated OU displacement kernel give E[Z]=gamma*v/((r+d)*(r+gamma)), E[Z^2]=2gamma^2*v^2*(2d+2gamma+3r)/((r+d)*(r+4d)*(r+gamma)*(r+2gamma)*(r+d+gamma)). Independent symbolic subtraction reproduced the displayed rational centered Q with numerator P=5r^3+(5d+7gamma)r^2+2gamma^2*r-4d*gamma*(d+gamma). Noise κ contributes only isotropic trace, not Q. P'(r)>0, P(0)<0, P(2d)=12d^2(5d+2gamma)>0, hence unique root in (0,2d) and exact variance sign ordering. For fixed 0<r<2d, P is concave quadratic in gamma with one positive gamma zero; this orders the r roots strictly with gamma. Implicit asymptotics yield (2/sqrt5)sqrt(d gamma) near gamma=0 and 2d-12d^2/gamma at large gamma. Boundary gamma=0 not asserted; density isotropy not asserted. Checked the polynomial and expansion independently with sympy; algebra and renewal derivation, not finite samples, support all parameters.

## originality

PASS

Best-knowledge original finite-inertia tensor threshold and strict parameter shift, not the already-published resetting model or overdamped limit.

## value

PASS

PASS. The inertia-dependent unique centered-covariance zero is a natural physical response threshold for an established stochastic resetting model, with exact finite-parameter rate and strict approach to the overdamped threshold. It can be used to benchmark anisotropy control independent of isotropic thermal diffusivity; not routine substitution into a known scalar mean-square formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
