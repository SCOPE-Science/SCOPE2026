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

For r≥3 on G_r=K_{2,...,2} (r pairs), the Connes distance with adjacency Dirac matrix is the reciprocal of the minimum commutator operator norm among real f with f(x)−f(y)=1. Pair-stabilizer and swapped-pair sign averaging reduce antipodes to f=(1/2,−1/2) on one pair (norm sqrt(r−1)) and adjacent pairs to the four values (1/2,a,−1/2,−a). The latter commutator reduces to a 3×2 matrix with rows (1,a+1/2), (a+1/2,2a), (sqrt(r−2),2a sqrt(r−2)); the larger eigenvalue F_r(a) of its Gram matrix yields the exact distance. Since the derivative matrix has full column rank, F_r is strongly convex; endpoint derivative signs give unique a∈(−1/2,0). Gram leading diagonal A_r>r−1 except the nonzero off-diagonal endpoint, so d_adj<d_opp. Expansion a≈−3/(8r) gives gap ≈1/(8r^(3/2)). Independently computed full 2r×2r skew commutators vs reduced Gram for r=3,4,5,8,12,20 and rational a trial values, agreement to <10^−11. No claim for r=2 or weighted graphs.

## originality

PASS

Best-of-knowledge PASS for exact two-orbit adjacency–Dirac metric on all cross-polytope/cocktail-party graphs and quantified asymptotic distinction. General finite graph Connes distance and Birkhoff–James methods are established; complete bipartite graph r=2 is excluded.

## value

PASS

An exact graph-operator metric on a canonical highly symmetric finite family is a natural invariant, and the quantified r^(−3/2) adjacency/nonedge gap makes clear how this metric differs from ordinary shortest-path distance. The two-orbit classification and asymptotics are more than a numeric instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
