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

For K<=1 maximum-modulus fixed-point inequality M<=K tanh M rules out all nonzero equilibria. For K>1 the unique positive root r=K tanh r satisfies K sech²r<1. Necessity: if all neighbors have the opposite sign at a nonzero equilibrium, weighted tanh neighbors cannot equal the vertex value at any beta. For a supported binary sign vector, at x=r sigma same-sign weights dominate opposite-sign weights by q0^beta with q0=delta/(2r+delta)<1. On a shrinking q^beta supnorm ball, the full normalized-weight map has Lip bound tending to K sech²r<1 despite equal-opinion absolute-value kinks; its center defect is O(q0^beta). Contraction gives a unique nearby exponentially attracting equilibrium with O(q0^beta) supnorm error for sufficiently large beta. A mixed supported coloring exists exactly if both monochromatic sign classes contain an edge; equivalently graph has two vertex-disjoint edges. Conversely color outward from endpoints of such edges along a rooted spanning forest; the four-vertex path is minimal. Independently enumerated all connected labeled graphs through five vertices and compared supported mixed colorings against matching >=2, obtaining n=2:(1,0),3:(4,0),4:(38,34),5:(728,723).

## originality

PASS

Pérez-Martínez et al. (2023) introduce the exact saturated-tanh, homophily-normalized opinion model and study polarization in special network regimes. The inspected paper does not prove supported-sign-pattern iff stable strong-homophily equilibrium on an arbitrary finite graph or a matching-number-two obstruction. Brooks–Chodrow–Porter analyze a different sigmoidal bounded-confidence vector field and cannot supply a same-model theorem without reduction. The matching proof is graph elementary but the uniform finite-beta fixed-point contraction is the substantive new result. Qualified priority risk remains.

## value

PASS

For an established nonlinear social-influence model this proves a sharp, topology-only threshold for the existence of genuine stable polarization: two disjoint edges, witnessed minimally by P4. It also classifies each admissible binary sign pattern and quantifies exponential approach to saturated magnitudes, turning qualitative simulations into a verifiable arbitrary-finite-network theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
