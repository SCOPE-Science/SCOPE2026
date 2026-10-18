---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Frozen RESULT.md ed759eb842e79a069e6ad0120e42823552387488 specifies complex reduced underlying projective variety. Distinct binary-separated row and column weights define a diagonal C* action with exactly mn ambient projective fixed coordinate points. Each r×r permanent is semi-invariant (all terms use selected rows/columns once); every coordinate point lies on vanishing locus for r≥2. The C*-fixed locus of P is exactly these points. Standard algebraic C*-Euler localization χ_c(Y)=χ_c(Y^{C*}) gives mn; projective compactness identifies χ_top and χ_c, while additive χ_c of complement is 0. Checked binary weight uniqueness and all permanent monomial weights for m,n,r=(2,3,2),(3,4,3),(4,4,2) independently; integer-valued checks only supplement the general proof. r=1 would give empty projective locus, rightly excluded.

## originality

PASS

Chan--Ilten study Fano schemes of same permanental varieties; Boralevi et al study their components, codimensions and singular loci via C* actions. The inspected primary results do not establish the Euler characteristic of the entire projective permanental locus for all r,m,n. Classical C*-localization is fully credited; only the parameter-uniform application is the candidate contribution.

## value

PASS

Euler characteristic is a natural global invariant of geometrically difficult singular/reducible permanental varieties. An exact all-format computation and vanishing of complement χ_c can serve as a consistency constraint even while finer topology remains unknown. Its proof is unusually short and coarse, but the mathematical object/invariant are independently motivated and the all-parameter fact is not a random slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
