---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

In mass pairing, the diagonal terms of the centered operator vanish by zero flux divergence, and the off-diagonal entries of the mass-multiplied operator are opposite across each edge. For an arbitrary two-point rule, the energy quadratic form after the divergence cancellation is ΣₑFₑ(αₑ−1/2)(θᵤ−θᵥ)². On a simple graph the mixed term tests each active edge separately, proving energy uniqueness; any edge on a cycle can be active. For the common kernel, any two neighbors of v can be joined in G−v and hence occur consecutively through v on a simple cycle. The transport at v of this single cycle current is ±(θᵤ−θᵥ)/(2mᵥ); the common kernel forces equality along every even walk. The parity classes are the two sides in a connected bipartite graph, and an odd detour makes them a single class in a connected nonbipartite graph. Conversely constants are null by divergence balance and checkerboard face averages vanish on every edge. Skew-adjointness gives the conserved weighted projection onto the mean-zero sign in continuous time and in every Cayley/Crank–Nicolson step; invertibility follows from the positive real part of I+τD/2 in mass pairing. Dual Cauchy–Schwarz in the inverse-Laplacian norm yields the stated floor. On the periodic grid the two wraparound cycles prescribe parity, and direct substitution in the standard stencil gives the eigenvalue 4/hₓ²+4/hᵧ² (208 for the 4×6 fixture). Uniform masses make the checkerboard mean-zero, and a stationary checkerboard realizes equality at every time. Ordinary coordinate parity gives the bounded-grid claim.

## originality

PASS

The reviewed increment is the complete joint stationary-space characterization for cycle currents on simple 2-vertex-connected graphs and its consequence for the mixing objective. The centered stencil, mass and energy preservation, and the checkerboard parity mechanism have substantial precedents; novelty is not assigned to any of those in isolation. The strongest inspected prior statements do not establish necessity via all cycle currents or give the exact control-independent inverse-Laplacian obstruction with the periodic equality case.

## value

PASS

The result detects an exactly immovable contribution to a real numerical mixing objective, rather than just a possible grid oscillation. The bound uses the initial projection and the chosen norm, so it can serve as a diagnostic before optimizing controls. The all-circulations classification explains precisely which graph parity structures yield common stationary directions under the stated hypotheses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
