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

All mixed-coordinate scale-two cliques lie in five-point diamond or four-point square facets, as shown by exact common-neighbor classification; C5 fiber is a simplex on five vertices (4-simplex), C6 fiber adds exactly two alternating triangles, and longer cycle fibers have only consecutive triples. Nine mn explicit elementary free-face pairs collapse the diamond/square baseline complex onto the standard grid torus triangulation, preserving primitive row/column circles. C5 extra contractible fiber attaches along its primitive coordinate circle and C6 adds two disks of winding ±1. With A=n*s(m), B=m*s(n), s(5)=1,s(6)=2,s(t≥7)=0, elementary CW cancellation yields T² when A=B=0, S¹∨∨^{A+B}S² when exactly one count is positive, and ∨^{A+B−1}S² when both are positive. Each scale-two shortcut reduces homologously to a two-edge original path, making H1(scale1)→H1(scale2) surjective with kernel free rank mn+1−β1. Independently reconstructed exact maximal cliques against the predicted facets for (5,5),(5,6),(5,7),(6,6),(6,7),(7,7),(7,8); the source verifier additionally encodes exact free-coface replay. Uniform proof is combinatorial, not extrapolated.

## originality

PASS

PASS best of knowledge, with square cases explicitly credited: the Adams et al. paper proves square C_m□C_m cases, including 5×5, 6×6 and sufficiently large square tori; the submitted theorem adds an all-rectangular uniform proof, especially C5×C_n, C6×C_n and 5×6 mixed regime. The existing width-four theorem is mathematically different (S³ instead of S²).

## value

PASS

The exact homotopy and H1 threshold transition for all natural rectangular torus grids resolve short-circumference boundary phenomena not inferable from the known square results. The 5/6 transitions are structurally meaningful due to simplex and octahedral C_t fibers, and the explicit 9mn elementary collapse supplies an integral, reproducible general method.

The dated certificate retains the supplied scientific assessment, sources and limitations.
