---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

For n>=5 the Kneser distance is 0 for equal probes, 1 for disjoint ground edges, 2 otherwise. For intersecting targets {a,b},{a,c}, the distinguishing probes are exactly ground edges crossing {b,c}, giving two isolates or a K2 component as the only failures. For disjoint targets the distinguishing set consists of the targets and edges leaving their four-point union. If this union is edge-closed, the target partition must be a balanced K2,2 bipartition; after excluding K2 and two isolates, the remaining connected obstruction is P4 or C4 or P3 plus one isolate. The equivalence holds for every n>=5 (including n=5). For G(n,p) at p=(log n+c)/n, factorial moments of isolates yield Poisson(exp(-c)); Cayley spanning tree bounds eliminate order-2/3/4 components, so P(resolve)->exp(-exp(-c))(1+exp(-c)). Monotonicity justifies drifting windows. An independently written direct metric-distance/subset enumerator agreed with component recognition for all 1024 n=5 and 32768 n=6 ground graphs (resolving counts 843 and 31232). The finite check is not the all-n proof.

## originality

PASS

Best-of-knowledge original structural or statistical addition survives direct statement/implication comparison with published primary results. Established premises, included special cases and residual priority risks are identified rather than represented as discoveries. Unsuccessful search is not treated as proof of novelty.

## value

PASS

A complete linear-time recognition criterion for every resolving probe set of KG(n,2) is a structural strengthening of mere metric dimension. It identifies exact smallest obstruction types and changes the random critical-window limit from the connectivity zero-isolate probability to a one-isolate Poisson tail. Both classifications and the sharp threshold are mathematically motivated and independently usable.

The dated certificate retains the supplied scientific assessment, sources and limitations.
