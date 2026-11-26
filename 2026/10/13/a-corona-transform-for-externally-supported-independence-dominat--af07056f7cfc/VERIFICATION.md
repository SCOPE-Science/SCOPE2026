---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

No core vertex can be selected, since an incident pendant leaf in the open neighborhood would have no neighbor outside the closed neighborhood. In a leaf-only selection, the open neighborhood is precisely the set of core vertices with a nonempty bundle. A partially selected bundle supplies its own outside neighbor; a fully selected bundle needs a core neighbor with no selected leaves. Partition by the uniquely determined zero-bundle set Z: the external boundary gets all nonempty selections and the undominated core vertices get only nonempty proper selections. This proves (1), including isolated vertices and the empty ESI set. At m=1 the proper-bundle factor vanishes, leaving exactly dominating Z and giving (2). At m≥2 each term has degree (m−1)n+|∂_H Z|−(m−1)|Z| and leading coefficient m^(n−|N_H[Z]|), with no cancellation, proving (3) and (4). For the classical identity used in (5), assign Roman labels 2 on Z, 0 on its exterior boundary and 1 elsewhere; conversely the zero-labeled vertices of any Roman function lie on the exterior boundary of its two-labeled set. Minimization gives γ_R=n−∂. The boundary is at most Δ|Z|, with equality for a singleton of maximum degree, so the claimed thresholds and m^n count follow. Independent adjacency-mask enumeration covered all 225 labeled-graph/multiplicity profiles of base orders 1–4 and m=1,2,3, testing 4,510,908 corona subsets and confirming the polynomials and extremal formulas. Replay: python3 /workspace/branches/dddf08ed-0bca-4aeb-8f80-4a251385c154/check_corona_esi_bounded.py --max-n 4 --max-m 3.

## originality

PASS

The distinct result supported by the comparisons is the full ESI polynomial transform on arbitrary uniform leaf coronas and its resulting domination reversal and exact ESI witness census. The support exclusion, the tree-only high-m extremal special case, and the classical differential–Roman identity do not count as new. The boundary-sum architecture itself has precedents for other invariants; the weights here are identified for a different set class. No equivalent claim was found in the checked sources; this is not a guarantee of priority.

## value

PASS

The formula counts all ESI sizes and extremal witnesses on a natural family built from arbitrary cores, including cores outside the earlier tree setting. Its single-leaf inversion encodes all base domination numbers by cardinality, not just the minimum, and the higher-m calculation separates baseline size from the count of optimal selections. These are concrete uses of the exact transform; no speedup or novelty of the old Roman identity is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
