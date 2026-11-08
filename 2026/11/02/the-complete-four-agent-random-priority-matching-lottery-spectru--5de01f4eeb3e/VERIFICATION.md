---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For four labeled agents and four objects, normalization of the first ranking by object permutation is unique, reducing 24^4 labeled preference profiles to exactly 24^3 canonical profiles with multiplicity 24. Enumerating all 24 priority orders within each canonical profile counts the full 24-matching outcome lottery (not marginal probabilities). A NEW separately coded exhaustive Python implementation evaluated all 13,824 canonical profiles, found exactly 57 positive multiplicity signatures and the claimed 16 support sizes; exact rational aggregation gave E[K]=1597/288 and Var(K)=684839/82944. The actual package contains verify.py, independent full-label verify_full.cpp (all 331,776 profiles), verify_pareto.py, spectrum.csv and support tables; verifier source inspected for the full-label approach. Counting is exhaustive over this FINITE domain, not a general-n theorem. K=1 iff all first choices differ by exchanging priority of two agents; K=24 endpoint attested by the exhaustive table, not an asserted general theorem.

## originality

PASS

The literature does characterize serial-dictatorship/Pareto-optimal assignments and ordinal inefficiency for four agents, and a published SCOPE record gives the three-agent lottery-shape spectrum. Those do not supply this complete matching-level four-agent 57-signature distribution. Abraham et al. use signature for a topological order of one assignment, not the vector of lottery probabilities across assignments. Best-knowledge novelty is the complete exact finite table and missing support values, not the RSD rule or Pareto equivalence.

## value

PASS

Four by four is the first nontrivial market size for marginal RSD inefficiency and an established exact small-market benchmark. The 57 matching-probability signatures and impossible support cardinalities characterize the rule more finely than marginals; a future matching-lottery study can directly reuse the exact distribution. This is complete motivated finite enumeration with independent algorithms, not a random small example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
