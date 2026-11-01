---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Every nontrivial Lyndon subsequence of 0^a1^b0^c1^d has two or four alternating nonempty runs. A four-run word 0^i1^j0^k1^l is Lyndon iff i>k or i=k,j<l, by comparing the suffix starting at the second zero run. Minimizing deletions over this criterion and the two-run option gives D=min(b,max(0,c-a+1_{b>=d})); equality cases a=c,b=d and c=1 are addressed. Positive-composition counting splits b<d vs b>=d, yields displayed exact generating functions; simplex Dirichlet integral gives P(D/n>t)=(1/2)(1-2t)^3 for 0<t<1/2, atom 1/2 at zero, and mean length 15n/16+O(1).

## originality

PASS

The published general longest-Lyndon-subsequence algorithms compute each input but neither state the four-run closed formula nor its exact population distribution or Dirichlet limit. Counting Lyndon subsequences and longest contiguous substrings are mathematically different statistics. Best-of-knowledge original new exact enumerative law, with potential unindexed specialization risk.

## value

PASS

Four alternating binary runs are the first family with a genuine choice between retaining both one-runs and discarding an interior run, and so are a natural minimal nontrivial case of the established longest-Lyndon-subsequence problem. Exact constant-time deficiency, entire rational distribution and nondegenerate limit with an atom give reusable precise information not mechanically obtained from a general individual-word algorithm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
