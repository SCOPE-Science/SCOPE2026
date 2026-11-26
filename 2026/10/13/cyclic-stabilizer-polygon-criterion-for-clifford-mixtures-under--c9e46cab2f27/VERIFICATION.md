---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Conjugation by u·σ is a half-turn about u, so the Bloch matrix is (λI+(1−λ)uu^T)R and preserves the norm of v=R^Tu. The exposed equality u^T Mv=1 forces C v=u for every contributing vertex C. If nonempty, these vertices form one coset of the rotations fixing v. The proper signed permutations with nontrivial fixed directions have axes through coordinate, face-diagonal or body-diagonal directions, with stabilizer orders 4, 2 and 3 respectively; all other directions have order 1. This follows by listing rotation types of signed permutations, including quarter-turns and half-turns on coordinate axes, half-turns on edge (face-diagonal) axes, and third-turns on body diagonals. Multiplying by C_0^T leaves the axis scalar one and transverse multiplication by λ exp(iδ). Every allowed Clifford transverse block is multiplication by an h-th root of unity, so matching the two real entries is exactly the polygon test. Choice of representative rotates the polygon and choice of transverse basis preserves the coefficient. For 0<p<1, including p=1/2, h=1 is excluded by |z|<1. At fixed third coordinate each possible nonvertical azimuth for a given special axis orbit differs by a multiple of π/2; a non-Clifford R_z therefore cannot connect v to u within an orbit unless u is vertical. The diamond gives the aligned inequality. For p=1 one can take u=(cos(θ/2),sin(θ/2),0), for which the equatorial half-turn followed in composition order after R_z(θ) gives the x-axis Clifford half-turn. The real-axis slice of the body-diagonal triangle is [−1/2,1], giving p<=3/4; the segment and diamond contain [−1,1]. The packaged LP checker and listed cases were inspected but not executed; no numerical tolerance proves the criterion.

## originality

PASS

The ambient Clifford polytope, pure-direction rigidity and circle-moment reduction, aligned dephasing threshold and documented p=1 tilted exception have prior coverage. The supported distinct claim is the evaluated cyclic polygon classification for arbitrary rotation and axis, with the resulting strict analytical exclusion for arbitrary non-Clifford phase angle throughout the intermediate-p interval and the body-diagonal threshold. It is not a new general membership formulation or the first identification of those aligned and endpoint cases.

## value

PASS

The exact slice classification replaces an ambient membership computation with at most a four-vertex polygon and gives constructive weights when feasible. For tilted dephasing it resolves the qualitative question of zero non-Clifford unitary cost at intermediate noise without relying on a numerical scan and separates a real endpoint exception. That is useful beyond restating the known ambient linear program or aligned threshold.

The dated certificate retains the supplied scientific assessment, sources and limitations.
