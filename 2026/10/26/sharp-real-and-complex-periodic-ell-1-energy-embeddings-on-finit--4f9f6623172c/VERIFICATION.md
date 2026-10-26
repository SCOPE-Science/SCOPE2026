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

# Verification and limits

The proof establishes the sharp constants and all equality cases for every integer \(N\ge3\), using real duality, the cycle Green pseudoinverse and strict concavity of the pair-separation functional, plus exact spectral-gap equality in the complex case. The Green formula was checked against its defining identity and against the known normalized cycle Green formula.

Run the included portable diagnostic with `python3 check.py`; it uses standard-library `fractions.Fraction`, exhaustively enumerates \(2^N\) sign patterns for \(3\le N\le11\), and checks both the proposed exact rational maximum and its entire maximizing-sign family. The checker is a bounded sanity check; it cannot replace the infinite-size analytic proof.

Literature comparisons included the zero-extended finite-sequence sharp result (arXiv:2610.19010v1), the sharp cycle log-Sobolev theorem (arXiv:2605.29035v1), and the original cycle Green kernel (arXiv:math/0309080v2), each inspected at the relevant theorem/definition sections. A previously unlocated equivalent older result remains possible. Independent audit is not performed.
