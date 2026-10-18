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

The ordered Singleton bound gives at most q^(4-3+1)=q^2. The two rightmost block coordinates (b,d) must distinguish codewords: if both agree, weight <=2. For equality they cover Q^2 bijectively. Holding b=u fixed and changing d=v makes the second block weight 2 and requires the first-coordinate map v->F(u,v) to be injective, hence a permutation. Holding d=v fixed symmetrically forces u->G(u,v) to permute. Both conditions suffice for distance>=3; there are 2q independent q-permutations, giving (q!)^(2q). At q=2 each permutation is affine, so F=v+alpha*u+beta and G=u+gamma*v+delta, and translations/shears act transitively. Independently exhausted all binary four-subsets of 16 words, finding exactly 16 maxima, and enumerated all 6^6=46656 q=3 permutation-function choices, verifying distinct codebooks and pairwise minimum distance >=3.

## originality

PASS

Compared the same objects and implications with primary prior literature and published research search. Prior optimal values or constructions are fully credited; no inspected stronger theorem implies the final complete classification. This is a best-of-knowledge determination, with the explicitly recorded unread-source risks.

## value

PASS

The smallest two-interacting-block ordered-metric MDS problem yields an all-alphabet complete classification of unrestricted nonlinear equality cases and an exact factorial count. Projection injectivity combined with separate row/column permutations exposes degrees of freedom excluded by linear-only treatments; a motivated structural statement rather than arbitrary tiny parameter computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
