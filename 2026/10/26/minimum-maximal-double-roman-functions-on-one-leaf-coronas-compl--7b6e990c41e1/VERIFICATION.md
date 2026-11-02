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

Pair (core v,leaf v′) has weight >=2 in any double Roman function; equality forces (0,2), while weight3 forces (0,3),(1,2),(2,1),(3,0). The core indices with weight>=3 form a dominating set D of G: each outside core has only its private leaf 2 and needs a high core neighbor. Thus weight>=2n+gamma(G), with explicit (2,1) cores on minimum D attaining it and meeting the non-dominating-zero-set maximality condition. Equality gives each D a choice S of high cores (2,1)/(3,0), while D\S uses (1,2)/(0,3), and V\D subset N(S) is exactly the outside-zero defense condition. Maximality excludes precisely the all (3,0)/(0,3) choice, yielding (2^q-1) per admissible (D,S). For C_n, circular gap lengths 1..3 with sum n and q=ceil(n/3) give cases n mod3: 3, n(n+11)/6, n admissible pairs. Independently brute-force checked complete 0..3 vertex labels and zero-set nondomination for K1, K2, K3, C4: optimal weight/count (3,2),(5,2),(7,3),(10,30). This includes isolated and n4 boundary; the source large graph checks and logs were read as corroboration only.

## originality

PASS

Cariaga–Jamil Corollary3(i) already yields the scalar 2n+gamma(G) for its specified connected bases, so that equality is explicitly not new. Ahangar et al define maximal double Roman zero-set condition. Neither inspected article provides the equality-case full bijection or the three-class sunlet multiplicities. This precise remainder is judged original on inspected evidence, with unindexed optimizer-census risk.

## value

PASS

Classifies all attaining label assignments rather than merely an old minimum weight on coronas. The count depends nontrivially on eligible (minimum dominating set,defending subset) pairs and reveals an exceptional cyclic n congruent1 mod3 multiplicity. Minimum optimizer census is a natural integral invariant of an established Roman domination variant and can support enumeration/optimization, including disconnected bases.

The dated certificate retains the supplied scientific assessment, sources and limitations.
