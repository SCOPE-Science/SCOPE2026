---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Exact verification

Execute `python verify.py` in the directory containing this file. Standard-library Python only; no downloads or auxiliary files are required.

The extracted verifier performed **24,635 exact checks**: rational identity and support tests for \(2\le a\le30\), \(1\le b\le30\), strict cross-side likelihood-ratio inequalities for every tested pair \(a>b\ge2\), and a separate exhaustive enumeration of the edge subsets constituting spanning trees of \(K_{a,b}\) for \(2\le a,b\le4\). The brute-force enumerator does not call the path-count formula, so it checks that part independently. The expected number of trees is checked against the bipartite matrix-tree count.

**Limits.** Exact enumeration is finite; the general all-size theorem is proved algebraically in RESULT.md. The numeric checks do not establish novelty, independence, nonuniform-host extensions or an independent external audit. The established 2019/2021 prescribed-tree/forest containment results are explicitly acknowledged.
