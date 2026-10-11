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
# Verification record

The public verifier `verify.py` is a Python 3 standard-library script that reconstructs the 18 associative multiplication tables and independently computes the first \(n\) observations by iterating the local rule on each possible length-\(n\) initial window. It compares the resulting number of distinct time words with every claimed closed formula for the finite range \(1\le n\le10\).

Call `python3 verify.py` in a directory containing the extracted file. The checker uses 18 rule tables, performs an associativity test for all \(18\cdot27=486\) triples, and makes \(18\cdot10=180\) direct finite trace cardinality comparisons. The analytical language classification in RESULT.md supplies the all-\(n\) proof. In particular a failure or timeout of this program would not prove a formula false, and a successful run is not an independent audit or an infinite certification.

The mathematical scope is the time trace of a fixed single site under arbitrary bi-infinite initial conditions; the full global cellular-automaton entropy and other observation schemes are not verified. The reference's 2025 public presentation predates the 2026 arXiv posting. No external review beyond the reported same-model review has been performed.
