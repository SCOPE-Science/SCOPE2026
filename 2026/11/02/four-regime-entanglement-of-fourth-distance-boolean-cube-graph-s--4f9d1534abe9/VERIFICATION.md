---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The graph-state cross-cut amplitude matrix has phase (-1)^(a^T C b), and tracing out the other side yields all-ones blocks indexed by ker C^T: exactly 2^r eigenvalues 2^-r for r=rank_F2 C. Across a coordinate cut, C is the third-distance convolution on F2^(d-1). The group algebra is R=F2[x_i]/(x_i^2), and its adjacency element A_n=binom(n,3)+binom(n-1,2)e1+(n-2)e2+e3 with e3=e1e2, reducing modulo four to e1(1+e2), e2(1+e1), e1e2 or (1+e1)(1+e2). Positive-degree 1+e_i factors are units. Multiplication by e1 has rank 2^(n-1); e2 has symplectic 2-form normal form and square-zero Künneth homology of dimension 2^m (times two for odd n), giving stated ranks. When n=2 mod4, simultaneously normalize e1 and e2 to u1 and sum u_i v_i, so e1e2 reduces to a tensor-product rank. Independent binary Gaussian elimination directly checked distance-three convolution ranks for n=3..10, yielding d4..11 entropies 8,8,12,12,128,128,240,240. Finite ranks corroborate, rather than prove, general formulas. Scope is pure qubit state and one-coordinate half cuts, not arbitrary bipartitions.

## originality

PASS

Hein–Eisert–Briegel established the general graph-state Schmidt-cut rank rule, which is explicitly credited. Hamming association schemes and modular adjacency algebra presentations are also known. The 2002 full proceedings text of Yoshikawa supplies a group-algebra presentation and a modular algebra quotient, but no inspected explicit rank of the full F2 third-distance relation or the resulting fourth-shell graph-state entropy. The more directly relevant 2004 Yoshikawa article could not be fetched through open routes or the authorized disconnected VPN. It remains a material priority risk; no assertion is made that the general algebraic setting itself is new. Comparison with standard distance-one hypercube graph states and free-fermion Hamming graph entanglement shows different states/relations.

## value

PASS

The full fourth-distance Hamming relation and its coordinate half-space cut are canonical symmetric quantum-network choices. Knowing the entire exact reduced spectrum for exponentially many qubits and sharp four congruence-class regimes, including maximal entanglement exactly in one residue class, is a motivated classification. The characteristic-two group-algebra rank is nonsemisimple and not obtained from complex Krawtchouk eigenvalues. Value is limited to the specified pure unweighted graph-state model and cuts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
