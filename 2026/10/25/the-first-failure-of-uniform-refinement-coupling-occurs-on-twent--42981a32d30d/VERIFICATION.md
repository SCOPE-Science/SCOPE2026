---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

The fixed-block-count uniform measures reduce exactly by symmetric-group averaging to block-size-profile transportation. A splitting edge represents precisely a possible refinement; a profile transportation flow can be lifted by random relabeling. Integer capacities LCM(S(n,k),S(n,k+1)) and integral max-flow give an if-and-only-if finite certificate. Independent Edmonds–Karp enumeration reconstructed all 171 (n,k) cases 2<=n<=19 and found all feasible. For n=20,k=2, the balanced profile (10,10) has mass 92378/524287, but its complete five-profile refinement neighborhood has mass 94410316/580606446, strictly smaller: cross-product difference 4137160923896. This proves impossibility at n=20 without extrapolating to larger n.

## originality

PASS

The theorem is specifically a normalized mass-transport/refinement stochastic-order statement, not a rank-matching assertion. Canfield (1993) studies injective matchings in the partition lattice; ordinary Hall matching cardinalities need not enforce the fractional normalized Hall inequalities between two uniform layers of different sizes. Pittel (2000) studies statistics of independently sampled unrestricted partitions, not adjacent fixed-block-count couplings. Resultary semantic search did not return a covering theorem. Best-of-knowledge originality holds subject to inaccessible full Canfield text.

## value

PASS

The exact first failure of a natural stochastic monotonicity principle at n=20, with a transparent sharp Hall obstruction and exhaustive positive range, is a motivated finite classification of a canonical family of uniform measures. It is not just a computation: symmetry reduction proves the finite network criterion and identifies the precise obstruction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
