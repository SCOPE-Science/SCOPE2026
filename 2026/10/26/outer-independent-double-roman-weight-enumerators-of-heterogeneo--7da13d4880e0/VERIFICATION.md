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

The attached `verify_oidr.py` computes the four hub-case products by coefficient convolution and separately enumerates the original graph's labeling predicate. All ten predefined cases pass, including heterogeneous blade sizes. Six additional graph-size vectors were checked using the same independently defined predicate. The checks cover up to ten vertices (at most \(4^{10}\) candidate labelings per case) and verify the full histogram, its minimum, the minimum multiplicity and the next-weight coefficient. This finite computation does not establish the theorem for arbitrary graph sizes; the four-case mathematical proof is required.

Exact reproduction from a directory containing the attached script: `python verify_oidr.py`. No external libraries or network connections are required.

The nearest foundational literature concerns the definition, optimum bounds, and computational complexity, while subsequent papers treat tree bounds and stability. The original introductory article's abstract and bibliography were accessible, but its full text was unavailable; any unseen coverage must be checked separately before asserting publication priority. Independent mathematical audit has not been performed.
