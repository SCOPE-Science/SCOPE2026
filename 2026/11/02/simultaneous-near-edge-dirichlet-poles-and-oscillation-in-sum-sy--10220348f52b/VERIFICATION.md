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

The standalone `verify.py` runs with Python 3 and no external dependencies.

Observed result:

```text
VERIFY_OK formal_coefficients=549 exact_dirichlet_coefficients=744 rational_arithmetic=yes
```

The exact checks compare the coefficient recurrence of \(m!z^m/\prod_{j=1}^{m-1}(1-jz)\) with Stirling numbers for \(2\le m\le10\), then compare coefficients of the rational Dirichlet expression against direct proper-factor convolution for \(2\le m\le7\) and \(2\le n\le125\). These finitely many identities corroborate the algebraic starting point only. The pole replication is proved by uniform recurrence and Rouché's theorem; the oscillation follows by the published nonreal-pole criterion. The code does not constitute an independent or infinite verification of those arguments.
