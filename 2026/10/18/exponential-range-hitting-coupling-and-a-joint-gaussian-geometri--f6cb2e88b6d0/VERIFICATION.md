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

For fixed 1/2<p<1 on C_n, lifted nearest-neighbor trajectory covers precisely when its range first reaches n−1. Gambler’s ruin gives ultimate minimum K geometric with tail r^k, r=(1−p)/p. Let b=floor((n−1)/2); E={K≤b, minimum through H_b equals ultimate minimum}. The probability of K>b and the chance of a lower minimum after H_b are each at most r^(b+1). On E the range cannot reach n−1 before H_(n−1−K), and at that time its last new residue is n−1−K. Therefore the dependent joint path coupling fails with probability ≤2r^(b+1). First passage increments are iid with mean 1/(2p−1), variance 4p(1−p)/(2p−1)^3; the CLT applies. Tight K makes the shifted passage-time error O_P(1). Conditional strong Markov at fixed early s and a uniform CLT over finitely many positions prove asymptotic independence of K and normalized H_(n−1); taking s→∞ gives the Gaussian–geometric product limit. No assumption of finite-n independence is used.

## originality

PASS

Best-of-knowledge originality judgment on this complete exact claim, based on statement-level comparison with primary mathematical literature and published research records, with limited full-text access flagged rather than interpreted as novelty proof.

## value

PASS

Coverage exploration requires knowing both where the last vertex is and how long completion takes. The explicitly controlled joint pathwise approximation and independent Gaussian–geometric limit are informative beyond the known biased-cycle location marginal or generic hitting-time CLT, with a useful exponential size error. Fixed positive drift and absence of Berry–Esseen rate are stated limitations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
