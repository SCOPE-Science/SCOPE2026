---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

A cycle is never shattered: all but one edge 1 (same side) and last edge 0 (different sides) is inconsistent. On a forest each Boolean assignment to equality edges produces exactly two complementary vertex colorings per connected component; if first uses c_i in the prescribed a-set, the other uses t_i-c_i. Feasibility is precisely [z^a] product_i (z^{c_i}+z^{t_i-c_i})>0. Every c_i between 0 and floor(t_i/2) arises from a tree edge labeling, so the criterion is necessary and sufficient and independent of tree shape. Balanced assignments yield sum floor(t_i/2) <=a and |S|=sum(t_i-1)<=2a; all-positive spanning-tree labels exclude a one-component support since 1<=a<n, yielding |S|<=n-2. Star on 2a edges with >=a isolates (n>=3a+1) is shattered by explicit center/leaf/isolates construction, establishing exact VCdim=2a in stable range. Small a=2 exception from size profile and direct witnesses. Independent finite exact 100490 support tests for 2<=n<=6 agreed; these do not prove infinite generality.

## originality

PASS

Best-of-knowledge originality assessment limited to specific evaluated statements after Resultary, inspected primary sources and same-Git records; not historical priority certification.

## value

PASS

An exact support-level characterization for fixed-size bipartition equality queries on arbitrary query graphs, showing invariance under tree shapes and a sharp stable regime VCdim=2a, is a usable structural result in learning fixed-cardinality graph partitions. It identifies a natural finite arithmetic decision procedure rather than a routine dimension bound only.

The dated certificate retains the supplied scientific assessment, sources and limitations.
