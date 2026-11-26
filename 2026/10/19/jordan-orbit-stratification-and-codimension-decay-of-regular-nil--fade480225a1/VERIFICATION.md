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

For T=(B,D;0,0), T=TUT in the restricted semigroup implies im T⊆T(W), and a right inverse of B on im B extended linearly to W gives the converse. Equivalently V=W+ker T, so one can choose a complement to W inside ker T. This gives a W-preserving normal form B⊕0, and any W-preserving conjugacy must preserve the similarity class of the restriction. Thus the orbits are exactly indexed by partitions λ of r, with ambient type λ∪(1^c), rank r−ℓ(λ), and index λ_1. The column choices give q^(c(r−ℓ(λ))) lifts per B. The Jordan-module endomorphism algebra has dimension Σ(λ'_j)^2; invertibility on the module is equivalent to invertibility of each size-diagonal block modulo t, giving the stated centralizer factors. For an independent derivation of the total, write a_k for the number of nilpotent k×k matrices. The unique Fitting decomposition of an arbitrary r×r endomorphism gives q^(r²)/|GL_r|=Σ_(k=0)^r a_k/|GL_k| by counting complementary subspaces and choices on the two summands. Taking the consecutive difference gives a_r=q^(r²−r). Arbitrary columns are allowed for all nilpotent lifts, while only λ=(r) gives exponent q^(−c) in the regular fraction; the others are O_(r,q)(q^(−2c)). The r=1 identity and c=0 case agree with the formulas. For c>0 a single maximal chain in W can be extended by one complementary vector iff its image is chosen outside im B; this proves the unrestricted maximum r+1 versus regular maximum r. Independent finite enumeration reproduced 13/64 and 211/512 and confirmed the inner-inverse test for all 64 maps at (q,r,c)=(2,2,1).

## originality

PASS

The regularity criterion and ordinary finite-field Jordan counts are established. The supported distinct claim is the restricted-range nilpotent classification under the W-stabilizer together with the rank/index enumerator and codimension decay, not the classical single-block factor on its own. The inspected regular semigroup literature addresses the criterion, ideals, Green's relations or generation, not this conjugacy enumeration. The closest catalogue entry overlaps the coefficient but does not account for restricted-range lifts.

## value

PASS

Within the natural regular stratum of a restricted-range linear semigroup, the relative conjugacy problem, exact partition counts and rank/index distribution answer a complete structural question. In particular the formulas quantify how adding directions outside W makes regularity exponentially rare among nilpotents even though the possible nonregular index increases by one. These are useful all-parameter statistics of the constrained model, not arbitrary examples, and the proof identifies why ordinary similarity suffices despite using the smaller stabilizer group.

The dated certificate retains the supplied scientific assessment, sources and limitations.
