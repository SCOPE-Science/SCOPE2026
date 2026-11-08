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

For d>=1 constants (0,v) are exactly the intrinsic left-zero elements; they form a faithful S_{q,d}-set. Thus any abstract monoid automorphism induces a unique point permutation normalizing S. Its unit group T⋊F_q^× has T the unique Sylow p-subgroup, because |T|=q^d and p does not divide q−1. After an origin translation the normalizer preserves T and so is additive. Preserving the origin stabilizer of scalar multiplications yields a bijection σ of F_q with σ(ab)=σ(a)σ(b), and additivity of the point map gives σ(a+b)=σ(a)+σ(b); hence σ is Frobenius and L is invertible σ-semilinear. Conversely every affine σ-semilinear point map conjugates S into itself. The order q^d f |GL_d(q)| and intrinsic parameter recovery via |S|/|left zeros|=q, |left zeros|=q^d follow. For d=0 it is the multiplicative field monoid, with automorphism group (Z/(q−1)Z)^×. Independent enumerations of small point-permutation normalizers (q,d)=(2,1),(2,2),(3,1) yielded origin-fixing sizes 1,6,2 respectively and total sizes 2,24,6, agreeing exactly. These checks supplement the all-q proof.

## originality

PASS

The combination of abstract finite-monoid automorphisms, all finite fields/all d, and parameter recovery is distinct from the algebraic monoid-structure classification and the affine-monoid quiver results. The normalizer argument is classical in parts and a general finite-semigroup normalizer theorem could imply the entire classification; best-of-knowledge pass is qualified by that specific priority risk.

## value

PASS

Scalar-affine maps with constants form a natural finite transformation monoid; recovering every abstract symmetry and the field/dimension without assuming coordinates is a natural complete classification. The semilinear normalizer rather than arbitrary permutations is mathematically informative, with a nontrivial rank-zero boundary; this is more than a bare tiny numerical computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
