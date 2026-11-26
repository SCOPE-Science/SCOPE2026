---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

Re-audited repairs/4/RESULT.md. For the two nonabelian groups, t=1+z has square zero and multiplication by t identifies the four coset directions with the ideal t kG. Because the quotient by that ideal is commutative, [ta,b]=t[a,b]=0. The displayed dihedral square is obtained by expanding in the coset basis, with scalar part S² and independent t, tr, ts, trs coefficients. The square-zero locus is the two stated spaces with central intersection. Within a branch elements commute; across their noncentral complements their commutator is a nonzero scalar multiple of tr. This gives the inclusion–exclusion pair counts and the complement size. The quaternion expansion instead forces all three nonidentity coefficients to vanish; the abelian truncated polynomial cases retain 4, 6 and 7 free coordinates respectively. The frozen proof line 37 incorrectly gave the span of the commutator images as ⟨tr,trs⟩ on both dihedral branches. The corrected proof uses [s,r]=trs and [s,rs]=tr on the first, and [rs,r]=ts and [rs,s]=tr on the second. Both pairs are independent, and the t-ideal is killed, so rank two and centralizer dimension six hold in both cases. The unit criterion follows by passing to the commutative quotient (there the square is the augmentation squared) and lifting across the square-zero ideal. In the six-dimensional centralizer the augmentation is a nonzero functional, so the index of its units in all units is (q−1)q⁷/((q−1)q⁵)=q². Conjugation preserves square-zero; dividing the two noncentral complements' total size by q² gives the corrected proof of the unchanged orbit formula. The supplied finite arithmetic checks were inspected, not run and not used as proof over all fields.

## originality

PASS

The original graph headline has substantive prior implication: in addition to the known quaternion locus, Creedon–Gildea’s proof of Proposition 2.1 gives the characteristic-two square polynomial for dihedral units. Via x ↦ 1+x it gives both noncentral square-zero directions, and the adjacency among those families follows immediately from their representative commutator. The repair credits that coverage and treats the graphs as context rather than a separate distinct claim. The retained result is the uniform unit-orbit size census on the D8 square-zero set. The inspected proof of the unit-group structure includes conjugations on certain subgroups, but not the full unit centralizers in both square-zero branches. The repaired element-centralizer argument yields those indices. This assessment concerns the surviving narrower result, not an originality pass for the original graph headline.

## value

PASS

Restricted to the unit-orbit size census, this is an exact invariant of a natural distinguished nilpotent set in the smallest dihedral modular algebra. It quantifies the reduction from element counts to counts modulo all algebra units uniformly over fields, which a total cardinality or a commuting graph within the nilpotent locus cannot supply. The result identifies central singletons and the precise common noncentral orbit size, not representatives or a classification for larger groups.

The dated certificate retains the supplied scientific assessment, sources and limitations.
