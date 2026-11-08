---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For every p=3 mod 4 and even r>=2, J²=-I over V=Fp^r with x²+1 irreducible, so all nonzero vectors decompose into four-element J-orbits. With one representative vi per orbit and check columns (Jvi|-vi), X/Z elementary syndromes are exactly {±vi,±Jvi}, all nonzero and distinct; the r-row check has full rank. Each orbit contributes the same alternating tensor vi(Jvi)^T-(Jvi)vi^T; summing over all vectors vanishes by finite-field coordinate second moments (r>=2), proving symplectic row commutativity. All nontrivial weight<=2 errors have nonzero syndrome, while a zero-syndrome weight-three witness combining Xi Zi with a different qudit exists; every nontrivial stabilizer occupies >=ceil((p-1)p^(r-1)/4)>2 physical sites except (p,r)=(3,2), so the witness is logical and d_diamond=3. Radius-one ball size 1+4n=p^r equals syndrome space. Independent finite modular computations corroborated p=3,r=4; p=7,r=2; p=11,r=2 and actual stabilizer supports. Joint-Lee radius one is not standard quantum Hamming radius one.

## originality

PASS

Qualified best-of-knowledge originality after claim-level comparisons with actual literature; no identified decisive prior theorem entailed the precise asserted value-bearing formula. Full-text limitations and possible indirect dominance are explicitly recorded.

## value

PASS

This supplies a constructive infinite family of non-CSS perfect codes in a recently formalized joint-Lee metric, with a direct orbit-symmetry commutativity mechanism and an exact distance proof. It fills an existence/design gap beyond isolated small examples; sphere-packing equality alone would not imply an isotropic stabilizer design.

The dated certificate retains the supplied scientific assessment, sources and limitations.
