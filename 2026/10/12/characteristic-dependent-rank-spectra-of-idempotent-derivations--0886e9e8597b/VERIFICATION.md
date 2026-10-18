---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Derivations of T_n(K) are inner, unique modulo scalar matrices, by Peirce-component multiplications. Composition-idempotent ad_H is semisimple, so the nilpotent part in its commuting Jordan decomposition vanishes modulo the scalar center; upper unitriangular diagonalization then gives λ_i−λ_j∈{0,1} for i<j. With λ_1=0 odd characteristic forces one 0-to−1 cut; characteristic two permits any binary label string. A labeling with k opposite entries has c=k(n−k) unequal ordered pairs, orbit size q^c and derivation rank c. This yields the displayed parity-dependent rank enumerators. Independently enumerated upper triangular generators modulo scalars and checked D²=D plus rank distributions: (n,q)=(3,2) gives 1+12t², (3,3) 1+18t², (4,2) 1+32t³+48t⁴, matching formulas.

## originality

PASS

Best-of-knowledge exact rank profile for projection derivations rather than idempotent triangular elements or Jordan superderivations; structural innerness is credited to earlier algebra work. Relevant idempotent matrix literature could imply pieces, but no inspected accessible source contains both characteristic regimes and full rank multiplicities.

## value

PASS

An exact classification and rank enumerator for natural projection operators on finite-dimensional triangular matrix algebras, separating characteristic two from odd characteristic; informs derivation-space geometry over all finite fields.

The dated certificate retains the supplied scientific assessment, sources and limitations.
