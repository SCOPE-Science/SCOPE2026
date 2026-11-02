---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

An independent C++17 finite enumerator rebuilt the Kneser vertices as unordered pairs and all closed signatures using disjointness; it counted every increasing k-subset, k=1,...,6 (499177 candidates total for K(8,2) and 2391495 for K(9,2)). Every k<6 subset fails identification; exactly 141120 and 7560 six-subsets pass. Full one-removal/one-addition adjacency yields edges 4730880 and 22680. For K(8,2) BFS produces one component and exact degree multiplicities 56:3360, 58:10080, 64:20160, 66:67200, 72:10080, 74:30240. For K(9,2) BFS gives 280 components each of 27 degree-six codes. Separately, the source constructive certificate enumerates 280 partitions of nine elements into triples and 3^3 center choices, all yielding spanning 3P3 identifying codes and all 7560 optimal codes; changing one path edge moves only one center, so each component is K3□K3□K3. Complete finite exhaustive searches prove exactly the stated finite orders and do not extrapolate to other n.

## originality

PASS

Best-of-knowledge PASS with a material access limitation. Roozbayani–Maimani establishes the scalar minimum identifying-code number for Kneser graphs, including both size-six minima; those numbers are not claimed as new. The full exchange graph, K8 degree census, and K9 ternary Hamming fragmentation are not present in its accessible abstract, but full text was unavailable and might include equivalent descriptions. Foucaud et al. consider identifying codes in line graphs, whereas K(n,2) is a complement of a line graph; graph-code equivalence is not automatic.

## value

PASS

The result supplies a complete optimum-configuration and local-move classification at two neighboring natural Kneser graphs of the same optimum cardinality, including a sharp connected-to-280-component transition. The exact degree spectrum and Hamming decomposition are independently useful finite invariants, not just minimum-size recomputations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
