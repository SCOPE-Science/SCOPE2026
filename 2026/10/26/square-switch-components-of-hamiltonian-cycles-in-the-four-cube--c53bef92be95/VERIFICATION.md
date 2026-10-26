---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction

Run `python3 verify.py` without third-party packages.

The verifier constructs \(Q_4\) from four-bit labels and checks:

1. An exhaustive canonical vertex-walk enumeration equals an independent enumeration from the \(272\) perfect matchings of \(Q_4\): both give exactly \(1344\) undirected Hamiltonian cycles.
2. All \(24\) square masks are generated once. A face-flip adjacency computation exactly equals an independent unordered-cycle-pair symmetric-difference test.
3. The resulting graph has \(1920\) edges and degree census \(240,384,192,288,240\) in degrees \(0,1,2,4,8\), respectively.
4. Complete component searches return \(240\) singleton components and one connected component of order \(1104\).
5. Breadth-first search from every vertex in the nontrivial component yields radius \(10\), diameter \(12\), eccentricity counts \(96,192,816\), and the twelve reported pair-distance counts.
6. All \(384\) coordinate permutations/complements give nine automorphism orbits with the asserted sizes and degrees.

The observed verifier terminator was `VERIFY_OK`. All loops have finite, explicit domains, with no dependence on heuristics, unbounded solver behavior, or external data. Exhaustiveness follows from (i) the recursive Hamiltonian-walk or matching-pair descriptions and (ii) enumeration of every square/edge pair and every graph state.

The asserted findings are exact finite statements. Reproduction is not an independent audit, and the checks make no statement about Hamiltonian-cycle reconfiguration in higher-dimensional cubes or larger switch sizes.
