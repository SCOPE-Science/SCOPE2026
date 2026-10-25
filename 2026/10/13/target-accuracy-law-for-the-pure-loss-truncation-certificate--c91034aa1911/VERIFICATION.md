---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

Let eps=e^{-lambda d}. For fixed nbar>0, g(nbar/eps)=[ln(nbar/eps)+1+O(eps)]/ln2 and h2(eps)=[eps ln(1/eps)+eps+O(eps^2)]/ln2; therefore B=eps[6 ln(1/eps)+4 ln nbar+6+O(eps)]/ln2. Put y=lambda d and L=ln(1/delta); log inversion gives y=L+ln L+ln(6/ln2)+o(1). Eventual monotonicity justifies bounded integer rounding; prime number theorem gives the coarser prime leading term. Substitution into the source-stated O(d^2 m log m) complexity proves its sufficient scaling. Independent mpmath for nbar=1.4 and d=40,100 gave exact/leading asymptotic ratios 1.000000123839 and 1.000000000000005. No lower bound for true physical cutoff is asserted.

## originality

PASS

The arithmetic gives a sharp asymptotic inversion of a highly specific thermal-tail continuity certificate. The initiating primary text could not be obtained in full, and only its abstract and package-cited Lemma 3 expression were accessible; published source coverage thus remains a particularly material risk. Searches of Resultary and related Winter/Shirokov approximation statements did not reveal a matching channel-specific inverse and operation-count law. This is qualified best-of-knowledge originality, not proof of priority.

## value

PASS

A designer of the specified finite-field pure-loss decoding construction may need the precise accuracy cutoff and loglog additive correction, with explicit link to the decoder arithmetic cost; the result quantifies a meaningful parameter cost, not only a renamed entropy formula. It is a sufficient certificate law, not a converse or universal quantum-channel complexity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
