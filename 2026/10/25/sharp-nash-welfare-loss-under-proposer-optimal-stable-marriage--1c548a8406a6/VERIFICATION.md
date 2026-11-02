---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

Under positive utilities u=n-r, Gale-Shapley men-optimality gives every changed man a strict loss: u_T/u_M<= (n-1)/n; exactly the same k women change, each with ratio at most n. Hence P(T)/P(M)<=(n-1)^k and the root welfare ratio <=sqrt(n-1). The explicit changed-k cyclic construction realizes equality for every 2<=k<=n. For n>=3 equality in the global n-power bound forces k=n and each man first/second and woman last/first partners, proving exactly n!D_n((n-2)!)^(2n) labeled extremizers and unique optimal T. For n=2 any stable alternative has product ratio 1. Independent brute enumeration computed n=2:16 and n=3:46656 complete preference profiles, n=3 12 extremizers and 5424 strict improvements; no finite check is used as all-n proof.

## originality

PASS

Statement- and implication-level primary-source and mathematical-index comparisons found no directly covering result in the material actually inspected; related ingredients and covered special cases are credited. Best-of-knowledge originality is qualified by the explicit residual risks; a negative search result is not novelty proof.

## value

PASS

Worst-case fairness loss of a canonical stable matching versus the welfare-maximizing stable matching is a natural comparison newly motivated by rank-induced Nash optimization. Sharp all-n ratio, complete equality rigidity and extremizer census are mathematically useful beyond an algorithm existence theorem; this is strictly for complete balanced rank-order utilities, not arbitrary cardinal matchings.

The dated certificate retains the supplied scientific assessment, sources and limitations.
