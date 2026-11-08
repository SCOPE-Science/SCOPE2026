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

In an inclined central plane with coordinates (u cos beta,v,u sin beta), a radial ray has quadratic intersection rho^2-2R sqrt(1-sin^2 beta cos^2 phi) rho+(R^2-r^2)<=0. Because the root product R^2-r^2>0, admissible intervals avoid the origin. For R sin beta<r all angles are allowed (annulus); above this threshold they form two components, each a disk. The area is 2R integral_0^{2pi} sqrt(1-s^2 cos^2 phi) sqrt((r^2-R^2 s^2 cos^2 phi)_+)dphi. It decreases strictly from 4pi Rr to 2pi r^2; at beta*=asin(r/R) the integral evaluates to 4r sqrt(R^2-r^2)+4R^2 asin(r/R). Near each of two degenerate angles, integrating sqrt((r^2 t^2+delta)_+) gives -(delta/(2r))log(|delta|/r^2) plus O(delta), for delta=r^2-R^2 sin^2 beta. Delta=-2Rr sqrt(1-(r/R)^2)(beta-beta*)+O((beta-beta*)^2), yielding the common coefficient 4(R^2-r^2) multiplying (beta-beta*)log|beta-beta*| and derivative tending to minus infinity. A Haar normal has |n_z| uniform, hence beta density sin beta and the topology probabilities; change of variables gives f_A(a)|log(|a-A*|/R^2)| -> (r/R)/(4(R^2-r^2)). Independent high-precision integrals for (R,r)=(2,1),(3,2) recovered area constants and cusp slopes 11.99999987 versus 12, and 19.99999983 versus 20. Full proof is local analytic, not a numerical extrapolation.

## originality

PASS

Best-of-knowledge originality of precisely the stated additional conclusion, not of its acknowledged classical object or method. Logarithmic area cusp and Haar topology law at the Villarceau transition is not directly implied by the strongest inspected primary theorem; exact comparisons and accessible source passages appear in the four structured checks. Inaccessible sources are identified as residual risks, not counted as negative whole-document evidence.

## value

PASS

A natural topology change in central planar torus sections generates a nonanalytic but explicitly quantifiable area singularity. Its coefficient and the corresponding vanishing Haar section-area density are useful precise invariants of stereological section statistics, going beyond the familiar Villarceau circle geometry. The exact topology probabilities and ratio dependence add a motivated geometric probability classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
