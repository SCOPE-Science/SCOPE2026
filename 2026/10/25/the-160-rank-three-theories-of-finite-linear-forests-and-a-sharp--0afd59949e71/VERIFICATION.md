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

# Reproducibility and check scope

Run the three bundled source programs in their directory as described in `RESULT.md`. The exhaustive rank-three signature calculation covers every nonzero seven-digit base-four multiplicity vector (16,383 cases), producing 160 distinct signatures. The histogram and all 160 minimum-order class representatives are provided as CSV; the greatest minimum is 23, attained by code 4438. The independently written Python and C++ finite census implementations agree on these results. The direct recursive three-round game cross-check agrees on 901 graph pairs among 52 canonical forests of order at most eight.

These finite checks establish the enumerated quantities only for the canonical domain. Their extension to *all* finite linear forests rests on the separately stated path-cutoff proof, the disjoint-union game lemma, and completeness of the recursive type signature. There is no claim of exhaustive direct game search over all finite forests, nor of an independent external audit or formal proof-assistant certification.
