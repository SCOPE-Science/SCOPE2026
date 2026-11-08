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

PASS. A maximum cycle-free multipath face on the complete loopless bidirected graph has n−1 arcs and is exactly one directed Hamiltonian path, giving n! distinct top oriented simplices in degree n−2. Closing each path yields its unique directed Hamiltonian cycle; different cycles partition the n! facets into (n−1)! blocks of n. The oriented missing-cycle boundary z_C is an integral top cycle with primitive ±1 coefficients. For every consecutive (n−2)-arc path plus isolated vertex, exactly two top cofaces close to the same C, forcing adjacent top coefficients to have the z_C ratio; these constraints connect each block and prove all integral top cycles are sums of z_C. No chains exist one degree above. The S_n stabilizer of each directed cycle is C_n and its rotation acts by (-1)^{n−1} on the cycle boundary; induced integral module follows. Rational transfer after barycentric subdivision and Frobenius reciprocity give S_n and A_n orbit-space top dimensions 1/0 and 2/1 by n parity. Independently reconstructed the complete n=3,4,5,6 Hamiltonian facet partitions and all two-coface incidences; finite checks are not substituted for the n-parameter proof.

## originality

PASS

PASS. The original Ω_n was introduced earlier, and Vrećica–Živaljević prove connectivity bounds and low-dimensional sharpness, not this complete integral top-cycle basis or top S_n-module. Caputi et al identify the complete-digraph multipath complex with Ω_n and study other graph families. Searches for aliases such as acyclic partial permutations, cycle-free chessboard complexes, and Hamiltonian top cycles yielded no prior theorem with the full induced integral representation. Originality remains bounded by inspected sources; the elementary missing-simplex construction itself is not claimed novel.

## value

PASS

PASS. An all-n explicit integral basis and natural S_n representation for the top homology of a classical nontrivial simplicial graph complex is a motivated structural invariant; the parity-dependent quotient-space Betti numbers follow with genuine equivariant information. This is not only a single finite calculation, graph relabeling, or a renamed homology rank.

The dated certificate retains the supplied scientific assessment, sources and limitations.
