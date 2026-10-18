---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For complete multipartite r>=3, a dominating set with support one must take an entire part; with >=2 supported parts it automatically dominates. For any selected vertex in V_i, outside neighbors consist of all omitted vertices outside that part, count B_S+sum_{h in S\{i}}y_h. Hence the inequalities are necessary and sufficient for every selected set; binomial choices of omissions yield exactly the claimed full cardinality polynomial. With K=k-B_S and total omissions Y, feasibility requires y_i>=max(0,Y-K) with caps n_i-1; the three upper bounds on Y by sum caps, K+min cap, and floor(sK/(s-1)) are also sufficient by an integer interval allocation argument. Thus minimum size at fixed support equals N-B_S-Y_S. Independent direct adjacency/neighbor checks agreed with support formula on 2920 graph-subset instances. Universal conclusion follows the counting/allocation proof.

## originality

PASS

Best-of-knowledge originality limited to the specifically unpreempted structural/classification content. Scalar minimization does not imply each coefficient without a new selection-count proof, so acceptance is limited to this substantive stronger enumeration.

## value

PASS

A complete cardinality enumerator for all feasible k-limited dominating subsets across arbitrary multipartite part-size profiles is a natural rich invariant, more than the already published scalar minimum. It counts every size and every support and gives a local feasibility criterion useful for enumeration/sampling. The fixed-support minimum is a derived useful secondary formula; **the scalar global optimum itself is prior-covered and not credited as new**.

The dated certificate retains the supplied scientific assessment, sources and limitations.
