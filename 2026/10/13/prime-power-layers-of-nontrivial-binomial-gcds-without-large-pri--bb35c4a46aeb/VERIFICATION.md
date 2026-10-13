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
# Verification

The standalone program `artifacts/verify.py` uses only exact Python integer operations for its finite checks. It computes the defining binomial GCD directly for \(3\le n\le150\), independently factors each \(n\) and checks the published prime-power criterion, and then compares a direct factorization-based census with the exact disjoint prime-power formula for every \(n\le20000\).

It also evaluates the exact counts at \(X=10^6,10^9,10^{12}\), including the first two dominant exponents, and records them in `artifacts/replay.txt`. These numbers are checks of finite identities only. The infinite asymptotics are established analytically in the proof using the prime number theorem and partial summation; no finite sequence of ratios is asserted to certify a limit.

The public materials do not certify a uniform-in-exponent estimate or the exact positive binomial-GCD values.
