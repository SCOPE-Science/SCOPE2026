---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

In plane basis with axial coordinate sx, squared distance to axis segment is c^2 x^2+y^2+(s|x|-a)_+^2, c=cos theta,s=sin theta. Integrating the positive ordinate gives exact ellipse branch A=pi r^2/c until theta*=atan(a/r), then cylindrical-plus-cap circular primitives; at theta=pi/2 stadium Amax=pi r^2+4ar. The squared axial-distance derivative w.r.t. s is -2s x^2 or -2a x, so section domains strictly nested and A(theta) strictly increasing, giving F=1-cos A^{-1}. At the cap contact, difference between virtual ellipse and actual area is a local square-root integral over shrinking width Delta~L^3(theta-theta*)/(ar); rescaling yields beta integral int u^2(1-u)^(-1/2) du=16/15, hence nonzero 5/2 coefficient. At c->0, shape derivative yields B=2a^3/(3r)+pi a^2+2ar and upper tail P(X>Amax-eps)~sqrt(eps/B). Recomputed high-precision independent cross-section quadrature for (a,r)=(1,1),(.2,1),(3,.7), corroborating asymptotic constant; finite quadrature does not prove continuum.

## originality

PASS

General unlabeled central-section distributions predate this, and spherocylinder distance formulas are standard. The complete capsule family distribution, 5/2 cap-contact coefficient and inverse aspect-ratio statistic were not established in the materially inspected convex-body distribution theorems. Historical stereology/spherocylinder specialized formula remains plausible priority risk.

## value

PASS

Exact natural Haar central-section distribution and nonanalytic cap contact encode capsule aspect ratio p*=1-r/sqrt(a^2+r^2) without orientation labels; sharp endpoint probability useful in stereology/tomography and identifies geometric smoothing effect.

The dated certificate retains the supplied scientific assessment, sources and limitations.
