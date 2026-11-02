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

# Reproducibility

Run `python3 verify.py` with Python 3 and no external packages. The script generates each directed one-swap output directly, verifies the six-neighbor compatibility graph, checks the construction over length range \(2\le n\le50\), validates the clique partitions on \(1\le m\le150\), and independently computes exact optima for \(2\le n\le9\) by recursive search. Expected output begins with `VERIFY_OK`. The all-length proof is contained in `RESULT.md`; finite verification cannot establish its unbounded quantifiers or literature originality.

The arXiv page https://arxiv.org/abs/2301.11680 shows initial submission on January 27, 2023, distinct from the June 2023 revision. Other references are identified in the result. The older shift literature has not been exhaustively catalogued; scientific originality has residual uncertainty. Independent validation has not been performed.
