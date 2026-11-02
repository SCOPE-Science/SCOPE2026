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

# Verification of the conditional terminal-coupon ordering

The analytic proof applies to all integers \(m\ge2\), \(q\ge1\), all positive required coupon weights and any nonnegative null rate with total mass one. It uses the exact labeled completion EGF, convolution log-concavity, Toeplitz total positivity and one explicit strictly positive boundary minor for each pair of unequal probabilities. There is no reliance on an unverified computer algebra lemma.

The independent Python 3 verifier is provided as `verify.py`. Execute `python3 verify.py` to obtain `PASS 5416 exact rational assertions` with zero external dependencies. It computes the full distribution of truncated coupon counts by state-level dynamic programming, separately evaluates the generating-function coefficients, and compares the two laws for multiple profiles, quota sizes and null-rate boundaries; then it checks strict odds minors and endpoint identities. These finite tests are not substituted for the mathematical proof.

The comparison with May (2008) acknowledges an existing terminal-count formula; no claim of new enumeration is made. The novelty assessment is limited to the strict reverse MLR ordering and consequences. Historical priority is qualified, especially for uninspected full texts and broad total-positivity treatments.

No independent audit or external validation was performed.
