---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For graph H_n=K_n square K_2, n>=2, label selected vertex sets by layer indices A,B, sizes a,b and intersection r. A paired-dominating set requires a+b even. If both layers selected, layer domination is automatic; even a,b>=2 allows internal clique matching, whereas odd a,b requires at least one vertical matching edge, equivalent to r>=1, then internal matchings cover the remaining even sets. If one layer empty, all n opposite vertices must be selected to dominate and n must be even for internal matching. These cases are necessary and sufficient. At even size s=2k the disjoint invalid kinds are 2*C(n,s) one-clique sets excluding two valid full-clique exceptions when n=s even, and 2^(s-1) C(n,s) disjoint odd/odd index allocations. Subtraction gives p_{n,k}=C(2n,2k)-(2+2^(2k-1))C(n,2k)+2*1_{n even,s=n}. The polynomial follows by even-binomial sums. For s>n the C(n,s) term vanishes, so every even selected set is valid; explicit disjoint odd/odd selections at the largest even <=n show sharpness. At s=2, n>=3 gives n vertical pairs and n2 gives four edges. Independently brute-forced actual graph domination and recursively perfect matched all subsets for n2..5: coefficient vectors [4,1],[3,15,1],[4,62,28,1],[5,160,210,45,1]. This finite check supports but does not prove all n.

## originality

PASS

Best-of-knowledge accepted: primary comparisons and actual database queries distinguish the final precise invariant from prior definitions, general bounds/algorithms, and related properties; residual literature access and equivalent-formulation risks are recorded explicitly. No absolute historical priority is certified.

## value

PASS

Paired-domination number alone loses most structure. The full coefficient polynomial for the canonical two-clique prism, its exact disjoint odd-layer obstruction, all-set threshold above n and sharp boundary are natural independently useful extremal enumeration data for a graph family studied in domination theory; it can serve as an exact baseline for more general prisms. The result is not a textbook substitution into a general exact graph polynomial table found in the comparison.

The dated certificate retains the supplied scientific assessment, sources and limitations.
