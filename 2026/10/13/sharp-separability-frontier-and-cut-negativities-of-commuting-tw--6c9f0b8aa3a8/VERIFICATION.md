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

For commuting Pauli strings the number of common sites with different axes is even. A conflict at v therefore forces a common second site w and identical two-site support. Any term touching just one of v,w would have to use an axis commuting with two different axes, which is impossible. On the pair, the two independent commuting generators have exactly their four-element Pauli span as centralizer modulo phases. Local Clifford rotations make it the Bell Pauli span and preserve the individual collected coefficient bounds; all other sites are single-axis and locally diagonal. The Gibbs state factors over the isolated pairs and the diagonal part. Partial transposition of each Bell projector gives half the identity minus a projector onto a permuted Bell vector (by transposing the maximally entangled projector and conjugating by local Paulis); the mixture has spectrum {1/2−q_s}. Two-qubit PPT is sufficient, and tracing to each pair gives the converse for full separability. Trace norms multiply, with factors of 1 from the diagonal Gibbs sector and all noncrossing pairs, and max(1,2p_e) from crossing pairs. Any two Bell sign triples differ in exactly two coordinates, so the maximum energy gap is 4J. The largest weight is consequently at most (1+3exp(−4βJ))^−1. The degree-two Hamiltonian J(XX+YY+ZZ) gives one energy −3J and three at +J, attains that bound, and is NPT exactly above βJ=ln(3)/4. This proves sufficiency and necessity, including the endpoint, for every cap Δ≥2.

## originality

PASS

The standard Bell-pair PPT law and the isotropic dimer crossing temperature are not themselves new. The supported contribution is the coefficient-preserving fixed-matching reduction for this Pauli class and the exact global consequences proved from it, particularly uniform optimality of the Heisenberg witness over arbitrary systems. Neither the closest unrestricted-locality result nor the inspected structural or degree-one results give those consequences under the stated hypotheses.

## value

PASS

For a physically natural restricted class the result isolates all finite-temperature quantum correlations into pairs even when the classical interaction graph is complex. It gives an exact separability decision and cut-by-cut quantitative entanglement without many-body Gibbs diagonalization, and a strictly improved, attained universal temperature boundary compared with the unrestricted-locality degree-two bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
