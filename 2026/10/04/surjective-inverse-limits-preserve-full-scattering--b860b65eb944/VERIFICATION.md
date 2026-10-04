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

The final claim was checked directly from the open-cover definition of full-scattering.

For an arbitrary nontrivial finite cover of the inverse limit, each member has a nonempty open hole. A finite collection of such holes contains cylinder neighborhoods coming from one common finite stage. Inside those stage neighborhoods, closed sets with nonempty interior are chosen. Their complements form a nontrivial stage cover: a common point of the closed sets would lift, by surjectivity, to a point omitted by every member of the original cover.

Each original cover member is contained in the pullback of the corresponding stage-cover member. Hence every time-join of the original cover refines the pulled-back time-join. The least subcover cardinality is therefore bounded below by that of the stage join. Because the canonical projection is surjective, pullback preserves the least subcover cardinality exactly. Stage full-scattering then forces divergence for the original cover.

For the countable-product corollary, each finite coordinate product is full-scattering by Xu's 2026 theorem, and the countable product is the surjective inverse limit of those finite products.

No numerical experiment, finite enumeration, or external certificate is used. The verified claim does not cover non-surjective inverse systems and does not assert a quantitative rate of divergence.
