---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

In kQ/J^2, the commutator at each arrow a:u->v is exactly (c_u-c_v) wedge x_a=0 for the m tuple coordinates. An arbitrary unit (vertex torus plus J radical) conjugates x_a by a scalar t_u/t_v and an additive multiple of c_v-c_u. Therefore when colors differ the arrow value is gauge-removable; when equal it is a free k^m-vector. For any nonzero arrow support F on equal-color endpoints, projective directions contribute P_m=(q^m-1)/(q-1) each and scalar amplitudes modulo incidence torus contribute (q-1)^(|F|-n+k(F)); loops and parallel edges are correctly counted. Summing over q^(mk(F)) constant-on-F colorings yields the exact Tutte/random-cluster evaluation. Top polynomial degree n+beta(G) comes from all nonbridge edges; freely selecting b bridges gives the leading coefficient q^b/(q-1)^(n-k(E)). Infinite distinct q lines reconstruct the bivariate polynomial. Independent five small-case direct full unit-orbit enumerations checked paths, a loop and parallel edges; the proof is valid for all prime powers, though small code used prime q.

## originality

PASS

The random-cluster polynomial, torus incidence quotient, and quiver-representation counting are older. The stated entire commuting m-tuple unit-conjugacy orbit count for all radical-square-zero quivers, including loops and holonomy, is a different functor from absolutely indecomposable representation counts and full-matrix simultaneous similarity.

## value

PASS

A uniform closed form for every commuting tuple length in every finite radical-square-zero quiver algebra is a natural representation-theoretic enumeration and links exact moduli to a standard graph invariant. Nontrivial loop and cycle holonomy effects are captured explicitly; the top-degree term reveals cycle rank, and all parameters determine Z_G, making the theorem structurally informative rather than a routine isolated count.

The dated certificate retains the supplied scientific assessment, sources and limitations.
