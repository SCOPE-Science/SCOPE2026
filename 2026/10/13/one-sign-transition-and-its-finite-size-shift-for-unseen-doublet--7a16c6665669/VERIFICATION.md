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

# Verification of unseen–doubleton covariance classification

The included `verify.py` uses Python's standard-library exact rational arithmetic. Run `python3 verify.py` in the directory containing the script. It enumerates every integer composition for 170 small Dirichlet–multinomial configurations with \(3\le k\le6\), \(0\le N\le8\), and shapes selected from \(\{1/3,1/2,1,3/2,2\}\), checking total probability one, independently computing both sample statistics and their covariance, and comparing with the closed formula. It then verifies 8,316 rational successive-ratio identities and strict decreases across a broad finite grid, along with the exact shape-one formula.

A separate high-precision gamma-ratio calculation was used to compare the continuous roots with the asymptotic shift for shapes \(a\in\{0.2,0.5,1,2,5\}\) at \(k\in\{100,400,1000\}\). The numerical root offsets approached \((a+3)/(2(a+1))\). The finite tests do not establish the continuous strict monotonicity, gamma limit, all-parameter sign theorem, or asymptotic coefficients: those require the proofs in `RESULT.md`.

The complete source papers referenced for the principal comparisons are accessible at their cited publisher, author-hosted, or arXiv addresses. A potentially relevant older partition paper was available only through its abstract and was not used to assert absence of implicit prior coverage.
