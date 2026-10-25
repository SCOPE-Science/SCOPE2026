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

# Exact verification and proof boundaries

Run `python3 verify.py` from the package directory (Python standard library only). The checker returns `PASS 212 exact-rational checks` and the positive \(L=7\) witness \(15515949/210827008\).

The checks include all retained-edge subgraphs of cycles and their one-leaf versions for \(3\le L\le8\), each at four exact rational probabilities. A distinct two-leaf unicyclic graph is exhaustively checked against the general covariance formula at four rational probabilities. The coefficient pattern is checked for \(3\le L<40\), the four negative discriminants are checked, and positivity witnesses are checked at eight cycle lengths up to \(L=100\).

These are finite tests. The infinite-family theorem is established analytically in `RESULT.md` by the pointwise bridge decomposition, exact covariances, Descartes' sign rule and the uniform positive witness. No external proof checker, formal proof assistant, or independent audit is claimed. The verification makes no claim about all possible published priority precedents.
