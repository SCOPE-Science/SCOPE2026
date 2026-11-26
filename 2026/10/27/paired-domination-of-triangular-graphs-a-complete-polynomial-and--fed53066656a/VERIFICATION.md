---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

An unselected edge of the clique is undominated exactly when both endpoints are unused, so at most one unused label is necessary and sufficient. A perfect matching in the selected line graph pairs selected edges at common endpoints. In a connected component, assign every non-tree edge to one endpoint and process a rooted spanning tree from its leaves: pair all currently available assigned and child edges if there are an even number, passing the parent edge up, or consume the parent edge in one pair and pair the rest if there are an odd number. At the root the unpaired count is even by global parity, proving sufficiency. In the labeled exponential formula, log A selects connected graphs, averaging its z and −z forms keeps those with an even number of edges, and (1+x)e^(−x) replaces unrestricted singleton isolates by zero or one. No perfect matching multiplicities enter. For the minimum, each edge pair covers only three labels, so b pairs must cover at least n−1 labels, giving b≥ceil((n−1)/3). Disjoint paths attain equality in the first two residue classes; in the third, two wedges sharing exactly one label form a four-edge tree and the remaining wedges are disjoint. For a component with 2r edges and v labels, the nonnegative defect 3r−v is at least r−1; total defect 3b+i−n is at most two. The only zero defect component is P3. The possible positive-defect components are a five-vertex tree (defect one), a four-edge graph on four labels (defect two), and a seven-vertex tree (defect two). This gives the listed component multisets for each residue class and choice of isolate. The factors 3/3!=1/2, 125/5!, 15/4!, and 7^5/7! count component types on blocks of labels; dividing by multiplicity factorials for repeated types gives the displayed terms across the three formulas, with the stated omissions. Boundaries n=3,4,5 are included.

## originality

PASS

The supported distinct result is the complete enumerator and all-residue minimum census, particularly the minimum component profiles and multiplicities for n≡0 and n≡2 mod 3. The edge-pairing criterion is a consequence of classical perfect-matching theory, and the exact n≡1 minimum type, cardinality and count are already in a distinct earlier Resultary record. Neither part is credited as new. The article's proof of those parts is useful for making the wider census self-contained.

## value

PASS

The full counting invariant for a natural line-graph family tracks which sizes occur and with what frequency, rather than just bounding the optimum. The genuinely distinct minimum census identifies all equality configurations in the two other residues: it separates unused labels, cycles in four-edge components, and larger sparse trees. Those structural distinctions and counts are useful for studying the space of optima, as illustrated by the separate slide-graph work in the previously covered residue. The standard parity reduction or the n≡1 count alone would not support this value finding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
