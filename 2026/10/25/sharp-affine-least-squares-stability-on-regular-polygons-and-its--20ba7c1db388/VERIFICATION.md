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

The uniform-area covariance of a circumradius-one regular n-gon is ((2+cos(2*pi/n))/12) I. Thus the kernel is K_n(x,y)=1+(12/(2+cos(2*pi/n))) x dot y. Absolute kernel-row integrals are convex in x, so a vertex realizes the global norm, while rotation gives the same norm at each vertex. The unique negative cap y_1<-1/c contributes 2(-area(cap)-c first_x_moment(cap))/area(P). The polygon shoelace/cap intersection prescription covers n=3, even and odd n and boundary clipping. A radial expansion r_n(phi)=cos(pi/n)/cos(s) gives mean delta r=-pi^2/(3n^2); the derivative of the disk integral yields 5*pi*sqrt(15)/12, with a Lipschitz error term controlling the angular microstructure. Reconstructed cap formula independently from clipping: triangle=19/8, square=233/108, hexagon=361/180 to machine precision, and rescaled corrections 5.07083 (n=80), 5.06974 (n=320), 5.069727 (n=500) approach 5.0697233. Finite checks support but do not prove the n->infinity limit. The proof supplies all quantifiers and the needed radial remainder.

## originality

PASS

Best-of-knowledge original for the all-regular-n exact area-weighted norm and its nonzero n^-2 correction. General projection stability and fixed simplex/ball cases are substantial prior background, but neither their hypotheses nor their conclusions give the polygon-dependent cap formula or evaluated second-order defect.

## value

PASS

Filled regular polygons are a canonical geometric approximation of the disk, and the degree-one L2 projector is the natural least-squares stability baseline. The all-n sharp endpoint constants and signed n^-2 correction answer a motivated domain-approximation question beyond arbitrary numerical cases; triangle/square/disk special cases alone would not qualify.

The dated certificate retains the supplied scientific assessment, sources and limitations.
