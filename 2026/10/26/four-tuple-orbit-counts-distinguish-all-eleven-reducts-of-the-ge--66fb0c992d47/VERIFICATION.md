---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Homogeneity identifies ordered injective n-tuple orbits with all assignments of 3 states to m=n(n-1)/2 labeled pairs. From Agarwal’s 11-group classification, global reversal fixes only the all-zero assignment; signed cut switching Burnside fixes 3^{C(k,2)+C(n-k,2)} for a partition k/(n-k), and reversal-times-switching fixes 3^{k(n-k)}, giving S_n and (S_n+R_n)/2. Vertex 3-state rotations act on the complete edge array by additive F3 potentials of rank n-1, giving 3^{C(n-1,2)}, and reversal divides nonzero quotient classes into opposite pairs. Binary graph complementation/switching similarly yield 2^m,2^{m-1},2^{C(n-1,2)},2^{m-n}, with n<=2 boundary exceptions via triangle parity. Independent explicit graph search on all 11 finite group actions at arities n=3 and 4 recovered the displayed n4 vector (729,365,108,76,27,14,64,32,8,4,1), and n3 collisions. The Stirling transform of equality partitions gives n4 all-tuples counts (913,464,177,139,53,34,127,64,28,18,15). The source checker for n<=5 was inspected; algebraic Burnside/vector-space proof establishes every n, not merely computed n.

## originality

PASS

Agarwal’s classification of the eleven closed reduct groups of the generic digraph, including switching, global reversal and three-state rotation operations, is prior work and crucially assumed. The assessed exact injective/all-tuple orbit-count profile and first distinguishing arity four are not stated in the inspected primary group-classification sections; direct orbit formulas use established finite group actions plus new application of elementary Burnside/coboundary enumeration. Published Resultary profiles for random bipartite/poset reducts concern different structures and do not imply the generic digraph values. An earlier unpublished or indexed group-specific orbit census is possible.

## value

PASS

For a canonical eleven-element lattice of oligomorphic reducts, the least arity of a single orbit-number invariant that separates all groups is a natural exact distinguishing invariant. The complete formulas for each n and their sharp n=4 separation support further invariant comparisons; this exact fact can be useful without claiming a new general classification theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
