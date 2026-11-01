---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The half-plane weighted Bergman Paley-Wiener/Laplace transform with strictly positive L2 density maps T_b to multiplication by exp(-bt), whose closed numerical range is convex hull of decaying logarithmic spiral S_k(x)=exp((-k+i)x), x>=0, plus 0. For k=Re b/|Im b|>0, phi=arctan k, c=(1+k^2)^-1/2, the exact support function is max{cos theta,c exp[-k(theta-phi)]} for theta>=phi, and cos theta below phi. Comparing monotone branches proves unique crossing Theta in (3pi/2,2pi), cos Theta=c exp[-k(Theta-phi)]. The boundary comprises S_k([0,Theta-phi]) and its single chord to 1; minimum support h(Theta)=rho is the origin-centered radius. The maximizing spectral values are finitely many points in each direction and the multiplier spectral measure is nonatomic, so no boundary point of the numerical range is attained; every convex-hull interior point is realized by positive-density mixtures. The expansions rho=1-2pi k+O(k^3/2) as k->0 and rho~e^-1 k^-1 exp(-pi k) as k->infinity follow from the crossing equation. The finite angle test agrees at moderate k; k=10 double-precision is at numerical resolution and is not treated as asymptotic proof.

## originality

PASS

Chacon--Chacon 2005 Theorem 5.13 states the Hardy-space parabolic-composition operator numerical range closure is the convex hull of a spiral; this foundational geometric hull is explicitly prior. Blois 2026 gives a weighted half-plane Bergman Laplace model in a cyclicity context. The added quantitative boundary, unique tangent, inradius and pitch asymptotics are not stated in the inspected 2005 theorem or its argument; novelty is restricted to that increment.

## value

PASS

The exact supporting chord, tangent and global centered inradius of a familiar winding spectral hull form a natural quantitative numerical-range characterization in an infinite-dimensional operator family. The sharp pitch laws and nonattainment distinguish it from merely recognizing the spiral convex hull.

The dated certificate retains the supplied scientific assessment, sources and limitations.
