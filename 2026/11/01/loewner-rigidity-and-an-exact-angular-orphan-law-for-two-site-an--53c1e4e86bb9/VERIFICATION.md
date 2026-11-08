---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For site-dependent SPD matrices, subtracting squared distances yields q(x)=xᵀ(A−B)x+2(Bp)ᵀx−pᵀBp, q(0)<0<q(p). If A−B⪰0 then the 0-cell is a convex quadratic sublevel. Conversely any negative direction of H=A−B gives arbitrarily distant points of C0 along that ray. Star-shapedness from 0 would force the entire ray to lie in C0; negative semidefinite directions by density or the two independent null lines for indefinite H contradict q(p)>0 or force Bp=0. Site exchange gives Cp criterion. If H indefinite, completing square with K=(B⁻¹−A⁻¹)⁻¹ yields hyperbolic phase parameter η=pᵀKp: positive gives disconnected Cp, negative disconnected C0, zero two apex-sharing closed cones. K has inertia (1,1), so η=0 gives exactly two exceptional lines. Haar uniform angles in eigenbasis give 2 arctan(sqrt(μ/λ+))/π for orphan C0, independent of |p|. Independent quadratic phase identities and 200,000-point uniform-angle test gave 0.39183 versus 0.3918265520 for K=diag(2,−1), corroborating rather than proving the general result.

## originality

PASS

Known anisotropic Voronoi literature studies multi-site visibility under sufficient wedge/density assumptions and geometric tensors conditional on star convexity. The source establishes a necessary-and-sufficient Loewner comparison for unrestricted two-site whole-plane star-shape and exact spectral probability of each orphan phase. The conic classification is classical and not claimed alone; novelty is this sharp linkage to site-assigned SPD cells. Highly relevant Venkovic–Anzt full text was unavailable after lawful attempts and Oxford VPN disconnection, leaving a named priority risk, not automatic rejection.

## value

PASS

The all-SPD two-site iff is a sharp structural boundary for whether common anisotropic Voronoi visibility assumptions are satisfied; the indefinite case gives an exact site-labeled orphan phase diagram and length-free spectral probability. This is mathematically motivated by anisotropic tessellation topology and clarifies when tensor/meshing models can assume star-shaped cells, rather than merely restating textbook conic classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
