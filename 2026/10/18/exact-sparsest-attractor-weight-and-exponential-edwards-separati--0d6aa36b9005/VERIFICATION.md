---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Under padded-zero boundaries every jammed word of positive length has one- or two-house runs. An internal gap has length one or two, with length two requiring a double run on each side. A boundary vacancy requires a double run and at most one vacant boundary site. Charge half each internal gap to each neighboring run and all boundary vacancies to the nearest run. Each run is charged at most its number of houses. In equality every double run must meet a double gap or an end vacancy on each side, and an end singleton cannot saturate; therefore all runs are doubles with double gaps and one vacant site at each boundary. The resulting word is (0110)^k and is jammed. On a permutation giving this word, each designated vacancy sees its own blocking pair already accepted; no other blocking triple is available in the final word. Conversely induction on visits makes just the designated pairs enter when all these within-block precedences hold. I.i.d. continuous priorities factor the block events with probability 2!2!/4!, giving the weight and rate. Independent run/gap transfer reproduces the stated static generating function, including the empty word; its x=1 recurrence and 76/81 induction coefficient give the stated all-n bound and full-flat ratio. Independent exact subset-DP reproduces basin counts 4, 1120, 2217600 and 16144128000 at lengths 4,8,12,16.

## originality

PASS

The supported contribution is the all-k dynamical minimum basin, and its consequent endpoint rate and quantitative comparison to the full flat ensemble. The open-chain statics, the weights for k=1,2 and earlier dynamical-versus-flat effects are already covered and excluded from distinct credit. No general dynamic weight result yielding this endpoint was established in the sources inspected.

## value

PASS

The true minimum is a natural edge of the coverage distribution. Its exact dynamical weight provides a rare-event benchmark, and division by the probability in the full uniform blocked-state ensemble proves exponential suppression rather than merely differing mean densities. This is useful even without a general rate function. The inequality is a bound, not claimed optimal.

The dated certificate retains the supplied scientific assessment, sources and limitations.
