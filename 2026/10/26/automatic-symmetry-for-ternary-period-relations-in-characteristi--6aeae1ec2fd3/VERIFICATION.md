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

Execute `python3 verify_group_algebra.py`. Expected exact line: `VERIFY_OK group=168 rank=160 swaps=168`.

The verifier constructs the entire 168-element binary linear substitution group from the three named generators, checks closure, constructs 336 relations, computes their rank over \(\mathbb F_2\), and reduces every swap relation to zero against the resulting basis. This is exhaustive finite verification of the group-algebra identity and therefore yields an infinite-degree theorem by algebra, not by testing individual polynomials. The code and proof specify the same left-substitution order \(Cg\), \(Ag\), and \(Sg\).

Scientific limits: the theorem is limited to characteristic two. The symmetric-kernel basis quoted from the motivating article is not recomputed and is not part of the new claim. Independent mathematical audit has not been performed.
