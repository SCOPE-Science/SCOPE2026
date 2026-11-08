---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Normalized power-series recurrence follows by logarithmic differentiation. c2=9 alpha(18alpha-7)/121 and c3=-2alpha(486 beta²-405beta+121)/1331 with negative discriminant. Exact rational Bernstein coefficients prove positive s_n=-c_n/[beta(1-beta)] for n=4..21 and the q20,q21 bounds 4/5<q<11/10. The explicit Phi_n rectangle invariance for n>=22 has positive lower corner (49n-510t)/(2420n) and positive upper slack (n+930t)/(1210n), t=1+alpha in (1,2), completing the infinite induction. Independently reconstructed all 285 positive rational Bernstein coefficients and induction corner formulas in independent_checks.py, not reliance on saved logs. h^{-alpha} positive, endpoints alpha=0,1 excluded; no solution stability follows.

## originality

PASS

Lubich 1986 introduced the BDF convolution quadrature symbol; Jin–Li–Zhou 2017 address high-order corrections and convergence; Karaa 2024 studies positivity of convolution quadratic forms. None of the inspected statements supplies the exact 7/18 and all-index coefficient-sign classification. A more specialized BDF3 coefficient inequality could predate this.

## value

PASS

Sharp zero/nonzero sign frontier for every coefficient of a standard high-order fractional derivative discretization; it controls a basic kernel property needed when testing discrete monotonicity, and its finite-to-infinite certificate is nontrivial. The result makes no unjustified maximum-principle claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
