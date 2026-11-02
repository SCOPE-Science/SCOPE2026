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

The included `verify.py` contains exact arithmetic for the full list of twenty-eight bitangents in the seventh cyclotomic field. It verifies the three projective generators, the quartic restriction square conditions, the complete six-element Galois-action table, and every unordered pair of normalized bitangent coordinates. It checks all six primitive seventh-root embeddings at each of the three possible odd exceptional reduction primes. The captured `verify.out` concludes with `VERIFY_OK`.

The source of universality over all odd primes other than seven is the pairwise norm sieve plus the complete exceptional-prime checks, followed by reduction of unramified cyclotomic Frobenius. Sample direct counts over small prime fields are supplemental. The general theorem that a smooth plane quartic over an algebraic closure in characteristic different from two has twenty-eight bitangents, including hyperflexes, is used as classical input. The source-chronology and novelty comparison are matters for independent review; no independent audit or external certification is asserted.
