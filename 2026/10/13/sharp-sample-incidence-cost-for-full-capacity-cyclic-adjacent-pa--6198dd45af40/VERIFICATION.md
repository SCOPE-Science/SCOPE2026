---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

For m>=2,n=2^m-1, m binary tests must map the n adjacent-pair defect sets bijectively to all nonzero m-bit masks (zero reserved for empty). Thus each bit is 1 in 2^(m-1) edge outcomes. Each selected vertex hits at most two cyclic edges, forcing pool cardinality >=2^(m-2). Equality forces no two selected vertices adjacent and all m pools have that cardinality. Explicit item masks a_i=i at even indices; 1 for i==1 mod4; 0 for i==3 mod4, yield edge OR labels 1..n exactly, independent pools of size 2^(m-2), so Wmin=m*2^(m-2). Independent integer reimplementation verified m=2..12, but universal proof is symbolic.

## originality

PASS

The incidence lower bound and equality structure address sum of label-cardinalities beyond optimal number of colors/pools. Under cycle edge/vertex duality, union vertex-distinguishing edge coloring matches OR decoding; Bousquet et al and Kittipassorn–Sanyatit optimize palette size, not total edge-subset cardinality, and typically require nonempty edge subsets. Constant-weight consecutive-positive matrices demand stronger item-label assumptions. The related 2026 low-weight Gray-code conference paper could overlap and was not read in full.

## value

PASS

At full information-theoretic test capacity, total item-to-pool incidences is a natural resource burden (sample uses, assay load) independent of the number of tests. Exact minimum, per-pool perfect balance, equality characterization and a construction at every capacity give a reusable extremal design benchmark, despite excluding singleton/noisy decoding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
