---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

The bounding-box area is w_n(theta)w_n(theta+pi/2), the product of two perpendicular support-function widths. Reduction of the nearest-vertex phase modulo 2pi/n for even n and modulo pi/n for odd n gives a uniform cosine phase with (C,D,b)=(2R^2,1,2pi/n) for 4|n; (2R^2,cos(pi/n),pi/n) for n=2 mod 4; and (2R^2 cos^2(pi/(2n)),cos(pi/(2n)),pi/(2n)) for n odd. These identities hold for n=3,4 and all larger n without degeneracy. Uniform |T| in [0,b] proves the arccos CDF on the exact interval and zero endpoint atoms. Integrating cos(T), cos^2(T) establishes exact moments. Since Var(cos T)=b^4/45+O(b^6), the n^4/R^4 variance limits are 64pi^4/45, 4pi^4/45, pi^4/180, hence 256:16:1. For X=(U-B)/(U-L), the arcsin CDF yields a uniform b-expansion; maximizing sqrt(x)-x^(3/2) at x=1/3 gives sharp b^2/(36sqrt(3)) Kolmogorov correction. Independent Cartesian vertex-width quadrature checked 12 n cases, orientation samples, and moments, independent of the source phase code. Finite checks corroborate but do not prove universal n.

## originality

PASS

Best-of-knowledge new content is the full Haar push-forward law, its three variance asymptotics, and normalized limiting distribution; pre-existing minimum enclosing-parallelogram endpoints are expressly not new. The closest fully read prior exact polygon formula is for the minimum over optimizable orientations, not random fixed-axis bounding-box area.

## value

PASS

Random orientation versus optimal placement is a genuine geometric-probability distinction: this all-n law quantifies uncertainty in standard axis-aligned bounding rectangles. The arithmetic mod-four fluctuation hierarchy and exact universal normalized loss law are natural sharp invariants, not arbitrary sampled values.

The dated certificate retains the supplied scientific assessment, sources and limitations.
