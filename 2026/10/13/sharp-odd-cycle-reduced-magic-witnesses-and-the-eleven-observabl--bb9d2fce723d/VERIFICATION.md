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

The graph used is the anticommutation graph exactly C_(2k+1), k≥2. A label dependency lies in the kernel of its binary adjacency matrix; the kernel equation forces a two-periodic, thus constant, vector. No proper subset has a dependency. Independently of the cited projected-polytope theorem, a commuting independent set with assigned signs gives a normalized common-eigenspace projector. Expanding this projector into Pauli products gives zero expectation on every measured observable outside the set, since none of those labels is in the span; completing the commuting subgroup expresses the projector as a stabilizer mixture. In the other direction, a pure stabilizer projection has ±1 support on a commuting subset and zero elsewhere. Thus the polytope is the unconditional lift of STAB(C). The edge and odd-hole inequalities suffice: on a zero coordinate face the remaining path polytope is integral and its k disjoint edges imply the sum bound; with all coordinates positive, a vertex would require all or all but one edge equation. All edges tight gives the forbidden all-half vector; all but one plus the sum equation forces a coordinate to zero. For the centrally symmetric lift, the signed-affine norm is max(1,gauge), by splitting a convex representation of b/gauge into oppositely signed contributions at opposite points. An edge has capacity sqrt(2) by anticommutation. For the odd-hole term maximize signed Hamiltonian top eigenvalues. On each eigenspace of the central involution i∏P_j, monomials from a symplectic basis of the rank-2k quotient form k standard Pauli pairs. They generate M_(2^k) with a multiplicity factor; the remaining cycle product is fixed by the central sign. Matching these pairs and the center to the Majorana realization (flipping one generator as needed) covers arbitrary realizations. Edge-sign switching of the skew adjacency leaves just a flux; negating all signs flips the flux for odd length and preserves positive singular modes. The all-plus skew spectrum 2i sin(2πj/L) gives the largest energy 2∑_(j=1)^k sin(2πj/L)=cot(π/(2L)), with mode occupancies chosen independently. Dividing by k and comparing to sqrt(2) gives the stated maximum. Strict concavity of x↦cot(π/(4x+2)) from zero makes its ratio to x strictly decreasing. The exact k=4 and k=5 comparisons straddle sqrt(2), as claimed. Eigenstates attain both constituent optima where needed.

## originality

PASS

Supported for the specific all-odd-cycle reduced-magic synthesis and sharp C11 crossover, not for the projected-polytope framework, odd-cycle facets, or all-length cotangent spectrum in isolation. An important omission in the frozen literature discussion is McNulty's preceding exact cycle incompatibility result, not merely a general free-fermion method. It already contains the normalized cycle support that supplies the spectral ingredient. The earlier reduced-magic theorem gives the clique rule for perfect graphs and does not settle how the odd-hole inequality competes with it on imperfect graphs. A later compatibility paper supplies an equivalent gauge on these cycles and, together with the cycle facets, covers the same capacity as a corollary; this is substantive equivalent coverage but not evidence the frozen statement was preceded by that paper.

## value

PASS

Odd cycles are a basic nonperfect test family for the reduced stabilizer method. Imperfection produces a necessary additional facet but does not imply an increase in maximal reduced magic over an edge: the theorem pinpoints exactly when the genuinely nonclique witness improves capacity and when it remains only a pointwise distinction. That finite crossover and the all-realization exact certificate are useful benchmarks beyond the previous perfect-graph rule, not a recomputation of the known quadratic spectrum as an end in itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
