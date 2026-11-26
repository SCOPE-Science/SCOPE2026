---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The standalone program `artifacts/verify.py` uses exact Python integer operations. It compares the defining binomial GCD with the imported prime-power criterion for \(3\le n\le150\). It then compares direct trial-factorization census counts by layer with the exact disjoint prime-power formula at \(X=10,100,1000,10000,20000\); these are comparisons at five cutoffs, not every cutoff through 20,000.

It also evaluates exact counts at \(X=10^6,10^9,10^{12}\), including the first two exponent layers, recorded in `artifacts/replay.txt`. These are finite checks. The fixed-exponent asymptotics use the prime number theorem and partial summation, while aggregation uses a separate uniform upper bound for exponents at least three. Neither uniform-in-exponent asymptotics nor exact positive binomial-GCD values are certified here.
