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

# Reproducibility and verification

Run `python checker.py` in the same extracted directory; no third-party dependencies or network connection are needed. The program independently enumerates perfect matchings for \(N=6\) and \(N=8\), constructs Gram matrices directly from actual Walsh sample evaluations, and compares exact rational determinants to the incidence-graph formula. It performs 158 direct checks, 20 maximal-cardinality tests, exhausts all 5005 six-vertex omitted-edge graphs, and counts connected odd-unicyclic graphs on 3, 4, and 5 labeled vertices as 1, 12, 162. The analytical proof in RESULT.md separately establishes the theorem for every even \(N\ge6\).

The verification does not exhaust all edge subsets for arbitrary \(N\), does not independently establish historical originality, and does not constitute independent mathematical audit or certification.
