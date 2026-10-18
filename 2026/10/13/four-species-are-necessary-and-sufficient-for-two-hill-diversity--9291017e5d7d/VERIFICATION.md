---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Sorting both s-component probability vectors yields a signed step function h(t)=Σ(1_{p_i>t}−1_{r_i>t}) with at most s−1 sign changes: supports from opposite-signed intervals at increasing indices are disjoint and ordered. The Mellin transform M(z)=∫t^z h(t)dt is a real exponential-polynomial integral with at most s−1 real zeros counted with multiplicity by the confluent Chebyshev/zero-variation lemma, proved via Rolle and sign interpolation. F(q)=Σp_i^q−Σr_i^q=q M(q−1); normalization M(0)=0 consumes one zero, and at q=1 the Shannon tie requires M′(0)=0. Therefore there are ≤s−2 finite q>0 ties for unequal multisets. Independent exact integer power sums for the displayed P and Q gave F(2),F(3),F(4) signs +,−,+ with differences 2362, −517776, 16323602434, hence exactly two simple crossings, in (2,3) and (3,4). No assertion of s−2 attainability for every s≥5.

## originality

PASS

General Rényi/Hill diversity comparison and crossing examples predate this record. Leinster–Cobbold 2012 explicitly exhibit two profile crossings but do not in the inspected corresponding section determine minimal positive species count. Patil–Taillie 1982 examines comparison/crossing for structured perturbations rather than establishing a universal equal-support s−2 bound in inspected passages. The new quantified tie maximum follows a nontrivial sign-variation argument; an existing total-positivity or power-majorization theorem might imply it without stating ecological terminology and remains a material residual risk.

## value

PASS

Hill/Rényi profiles are standard diversity-orderings in ecology; an upper bound on ranking reversals in terms of richness and an exact smallest double-reversal example clarify a natural model-selection ambiguity. The s=4 threshold is supported by an all-s theorem, not merely a numerical curiosity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
