---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For positive d,beta and K>=3, L>=K, deriving lambda_i=beta*i(i-1)(L-i)/(L-1)^2 and mu_i=d*i from independent mating/nursery samples gives the exact backward increment recurrence and hitting denominator. The derivative of each log ratio is (L+1-2i)/[(L-1)(L-i)], strictly eliminating L>2K-3. The K=4 denominators differ coefficientwise; at K=5 D_5,7 exceeds D_5,5 coefficientwise, and D_5,6-D_5,5=gamma(44+226gamma-253gamma^2)/48 gives the single positive switch gamma*=(113+sqrt23901)/253. Independent SymPy reconstructed these exact differences and bounds from model formulas. Finite checker tests do not substitute for derivative proof; interpretation concerns reaching K before extinction, not indefinite survival.

## originality

PASS

Exact capacity optimization is distinguishable from standard birth-death hitting recurrences and from qualitative habitat-size effects in spatial Allee systems. The full spatial primary paper uses a different process and survival outcome. No inspected stronger theorem or table implies both the universal K-dependent upper cutoff and the K=5 switching threshold. This is qualified best-of-knowledge originality rather than search-based proof of novelty.

## value

PASS

A natural finite Allee-rescue question asks what habitat size maximizes the probability that two founders reach a finite population threshold. The theorem supplies a nontrivial exact first optimizer switch and an all-K capacity bound, not just a plot or numerical sample. Its assumption of well-mixed independent draws limits practical extrapolation without erasing its structural model value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
