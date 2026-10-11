---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The proof is structurally sound. If a proper closed convex \(F\) contains \(a+V\), convexity gives \(x+v+t(a-x)\in F\) and closedness gives \(F+V=F\); quotienting by the hyperplane direction makes \(F\) the inverse image of a closed interval. Two distinct hyperplane directions would span all of \(\mathbb R^d\), forcing \(F=\mathbb R^d\), so proper members have unique direction. A face cannot mix distinct proper directions. Within one direction, the complex is the nerve of intervals; deleting an interval with minimal finite right endpoint is a valid elementary 1-collapse, and the all-right-unbounded remainder is a simplex. Universal vertices only join the unique maximal face and can be removed last.

## originality

PASS

The focal 2026 paper poses the general question whether \(N_k(\mathcal F)\) is \((d-k)\)-collapsible and reports that standard swiping arguments appear not to extend. The audited codimension-one proof uses a special structural collapse unavailable in lower codimension: every proper closed convex set containing a hyperplane is a generalized slab with one normal line, so each direction block becomes an interval nerve. Resultary and web searches found the audited record as the exact match and no older codimension-one theorem. Best-of-knowledge originality therefore passes, with an explicit access limitation on the primary paper.

## value

PASS

Codimension one is a natural boundary case of an explicitly posed collapsibility problem, and the proof identifies the geometric reason it is tractable: hyperplane-containing proper convex sets collapse to one-dimensional interval data after quotienting. This is a motivated structural lemma resolving a full parameter regime, not a tiny instance.

The dated certificate retains the supplied scientific assessment, sources and limitations.
