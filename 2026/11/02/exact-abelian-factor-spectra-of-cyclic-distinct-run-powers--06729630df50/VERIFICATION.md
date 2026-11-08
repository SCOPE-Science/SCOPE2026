---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For q>=3, a length-h linear window within distinct letter runs can have a repeated Parikh profile only for consecutive starts; its shift transition count is the linear window formula. For circular windows, proper support determines first/last runs or a single-run contiguous plateau, and full-alphabet support can be reduced to a complementary window missing a letter, proving the analogous circular contiguity lemma. Thus distinct cyclic Parikh profiles equal unequal adjacent-window shift count, computed from same-letter overlaps in runs; length blocks of P^k consist of k-1 full circular sets and one terminal linear set. Summing finite overlap formulas gives p+(2k-1)S+(k-1), including k=1 and full-length h=p. Independent literal factor-set enumeration matched all 11,856 length profiles across 723 finite instances; proof handles every allowed run length.

## originality

PASS

Afshar–Amir–Goodrich–Matias study jumbled-index algorithms and periodic string reconstruction, not the exact cardinality spectrum of distinct-run period powers. General Abelian complexity surveys and automatic-sequence results are not proved to imply this family formula; non-ultimately-periodic hypotheses of Parikh-collinear fixed-point results differ. Resultary matches concern Parikh-matrix unambiguity or other sequences, not this spectrum. An older elementary cyclic run count may exist, retained as residual risk.

## value

PASS

Parikh-vector factor counting is an invariant directly relevant to Abelian complexity and jumbled indexing. The complete by-length and total spectra for a natural compressed periodic distinct-run family, with constant per-copy increment and q>=3 boundary, are exact structural results rather than arbitrarily chosen small examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.
