---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Uniform Cayley trees correspond bijectively to m=n−2 iid Prüfer letters. Marked degree K=D−1 counts occurrences of label1; conditional on K=k the other m−k letters are iid in q=n−1 labels. Therefore L|K=k=E_{q,m−k}+1_{k=0} with exact Stirling occupancy pmf and mean 1_{k=0}+q((q−1)/q)^{m−k}. One common ball-addition coupling shows strict first-order stochastic decrease from degree1 to degree2, then strict increase for every later degree up to n−1; not a total order between degree1 and higher states. Exchangeability and deterministic sum degrees=2(n−1) give Cov(D,L)=0. Poisson(1) limit K and uniform fourth moment control give numerator Var(E[L|D])→e^-1−2e^-2>0; exact vacancy-pair variance gives Var(L)/n→same constant; hence n eta²→1. Independently exhaustively enumerated all Prüfer words n=4,5,6, verifying exact conditional means and covariance; inspected verify.py which extends rational conditional pmfs n≤8 and finite tails n<20. Finite checks do not prove the n→infinity limit.

## originality

PASS

Prüfer conditional occupancy law and degree-count moments are classical and must not be relabeled new. The identifiable contribution surviving prior enumeration is the strict sign-changing stochastic ordering across marked degrees together with a sharp nonlinear regression correlation-ratio scale despite exactly zero covariance.

## value

PASS

A natural dependence question that linear correlation misses is answered exactly: the marked degree has a strict conditional leaf-count stochastic valley at degree two and a nonzero yet asymptotically small 1/n nonlinear explained variance. This sign change and sharp scale clarify what a single degree can predict from a global leaf count; neither a generic occupancy count nor a tiny enumeration.

The dated certificate retains the supplied scientific assessment, sources and limitations.
