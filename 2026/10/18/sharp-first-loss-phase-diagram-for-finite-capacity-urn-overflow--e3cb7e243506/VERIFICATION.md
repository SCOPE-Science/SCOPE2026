---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

Enumerated exactly zero/one/two rejected occupancies at m=r+2: counts N-a-1,a,1 on denominator N=n^(r+1). The LC inequality N<=a²+a+1 gives the four boundary pairs: (r,n)=(2,14) passes and (2,15) fails, (3,3)/(3,4), (4,2)/(4,3), (5,2) fails. R(n,r) monotone via n^(r+1)/(n-1)² and quadratic denominator, and via n-multiplier at r step; check n=2 independently. ULC equivalent (a+2)²>=4N; only (2,2), and PGF factors (1+z)(3+z)/8. At (2,2) m=5 exact PMF {1:20,2:10,3:2}/32 gives shifted quadratic z(10+5z+z²)/16, discrim -15. Finite rational dynamic-programming check checked n,r in 2..6 and all phases n<=150,r<=40; infinite classification relies on explicit monotonic argument, not tests.

## originality

PASS

Compared exact hypotheses, invariants, reductions, implicit prior implications, and relevant primary theorem/proof sections. None of the inspected cited primary results implies this final precise statement under its hypotheses; originality is best-of-knowledge only, with named residual risks.

## value

PASS

Earliest-time shape classification of an elementary but nontrivial finite-capacity occupancy law distinguishes ordinary from ultra-log-concavity and records a unique delayed real-rooted exception; finite-horizon threshold is a natural reusable diagnostic for possible Poisson-binomial approximations and model validity, not a mere rebranding of asymptotic overflow limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
