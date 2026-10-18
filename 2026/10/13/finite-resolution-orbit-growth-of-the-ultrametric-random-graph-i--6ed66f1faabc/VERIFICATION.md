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

The Kubiś–Pech–Pech homogeneous ultrametric random graph has arbitrary finite graph patterns compatible with each finite ultrametric; strict metric homogeneity identifies ordered injective tuple orbits with their full labeled finite metric-graph diagrams. A minimum pair distance of 2^{-h} is encoded by a chain of h intermediate partitions from the indiscrete partition to discrete at level h+1, hence O_{n,h}=2^{binom n2} H_h(n). Conditioning on a refinement layer gives H_{h+1}(n)=sum_{pi in Pi_n} prod_{B in pi}H_h(|B|). Counting strict partition chains and choosing their transition slots gives H_h(n)=sum_{k<=n-1}c_{n,k} binom(h+1,k), whose leading coefficient is (prod_{j=2}^n binom(j,2))/(n-1)!=n!/2^{n-1}. Therefore leading orbit coefficient is n!2^{(n-1)(n-2)/2}. Independently recomputed exact H rows for 1<=n<=7, 0<=h<=3 and leading finite differences through n=5, all matching the claimed table. Special n=1,h=0 cases also follow.

## originality

PASS

Best-of-knowledge PASS for the exact finite-resolution ordered-tuple orbit profile of this particular universal homogeneous metric graph, not for classical higher Bell numbers or order-polynomial leading terms in isolation. Kubiś–Pech–Pech establishes the universal graph and strict metric homogeneity; Skau–Kristensen supplies nested-partition combinatorics. Their inspected texts do not state the exact graph orbit factor 2^{binom n2} and resolution-polynomial profile as an invariant of this automorphism group. Resultary’s neighboring colored-gap result concerns a different ordered minimally expanded ultrametric structure and Fubini, not this unordered partition-lattice setting.

## value

PASS

For this natural non-oligomorphic Polish metric automorphism group, counting finite-resolution orbit types is an intrinsic structural invariant. The exact formula quantifies polynomial resolution growth at every fixed arity, with a leading constant, and explicitly separates unrestricted graph bits from hierarchical metric data. This is a motivated reusable group-action statistic rather than arbitrary finite enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
