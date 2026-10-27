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

The complete proof consists of six explicit Apéry-set staircases, the cardinality identity, and three strictly weight-lowering congruence reductions for each residue class. Checking these algebraic expressions at four arguments per residue proves the polynomial identities universally since their degree is at most three. Positive coefficients and corner ordering are established for every integer \(n\ge48\) by the displayed linear expressions and cubic sign comparisons.

Run `python3 verify.py` using the local package to check these identities and independently compute Frobenius numbers for a suite of values by shortest paths modulo \(P(n)\). This finite replay is corroboration only; all infinite quantifiers rest on the preceding symbolic argument. No independent external audit was performed.
