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

Run `python3 verifier.py`. No third-party libraries or external data are needed. The verifier checks the defining recurrence using exact integers through the index \(2^{11}\), the asserted formula at all examined dyadic indices beginning with \(2^4\), the relevant termwise valuation inequalities, and the first three convergent two-adic polylogarithm series modulo \(2^{64}\).

# What the checks do not show

The finite checks do not prove the infinitely quantified theorem. The proof in RESULT.md supplies its own analytic convergence, exact algebraic identities, and universal valuation bounds for all \(m\ge4\). The project has not received an independent mathematical audit or publication-priority certification.
