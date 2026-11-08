---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

For C=phi_w∘B the regular full fiber is the simple zero set. Partial fractions show C' lies in the finite span of the normalized Bergman kernels, including the possible zero at the origin. Minimal-norm Gram interpolation gives ||C'||²=v*G^{-1}v/(1−|w|²)²; proper degree-d change-of-area gives ||C'||²=d. Thus H on the fiber has the unique eigenvalue d. For degree two, source/target automorphisms reduce B to z² and weighted composition U_Bf=√2 z f(z²) has exactly odd functions as range. A two-kernel difference is odd iff z2=−z1 (distinct), so equality occurs precisely on a full fiber; strict positivity off-fiber follows from the known semidefinite inequality. Exact independent rational inverse-Gram checks verified three real-zero fibers of degrees 2, 3, 4; those tests are supplementary.

## originality

PASS

The sharp uniform bound d belongs to Tian (2026), and the power-map full-fiber example is already in the published range-valence result. The new, narrower claims are the exact inverse-Gram identity for EVERY regular fiber of EVERY degree-d finite Blaschke product and the if-and-only-if equality locus for any distinct degree-two sampling pair. Searches by derivative weighted composition, Bergman Gram equality and full fiber found no explicit corresponding classification. Tian primary full text was inaccessible here, so this PASS is best-of-knowledge with a substantial priority risk, not a whole-document negative finding.

## value

PASS

This is a complete geometric equality classification for all regular interior degree-d fibers and the first nontrivial off-fiber setting, resolving which point configurations actually saturate a known sharp inequality rather than only repeating its uniform constant. The distinction between full-fiber interpolation, arbitrary sample pairs and the known monomial example is a natural analytic invariant useful in further rigidity/critical-fiber work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
