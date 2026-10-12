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

# Verification of the analytic claim

The supplied `verify_negative_binomial.py` is a standalone standard-library checker. On a fresh invocation (`python3 verify_negative_binomial.py`) it completed with:

`VERIFY_OK exact_tail_sign_cases=105 adjacent_quotients=2142 finite_vandermonde=343`

The check uses exact `fractions.Fraction` arithmetic to reproduce all finite endpoint seeds quoted in RESULT.md, the sample negative-binomial mass ratios, the sign sequence for all \((r,t)\) in the finite grid \(3\le r\le17\), \(1\le t\le7\), and a finite grid of Vandermonde comparisons. This is not exhaustive for unbounded \(r,t\).

The infinite proof is mathematical: exact cancellation yields the one-turn \(\beta_i\) ratios; the identity for the sum of \(\alpha_i\) holds for every finite-mean nonnegative-integer law; the endpoint inequality is established by exact seeds and combinatorial induction for \(t\le5\) and an analytic monotonicity bound for \(t\ge6\). The proof covers all positive integer shapes at least three and all positive integer \(t\) without numerical inference. It does not check any noninteger parameter regime.

The external literature comparison is limited to materials actually available for inspection. The later published full text and earlier arXiv manuscript were read; the 2007 center-tail article was only accessible by abstract. The result has undergone self-review, not independent validation.
