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

# Reproducibility

Run `python3 check_normalizer.py` from this directory using Python 3 and no external packages. It independently generates all reduced-row-echelon finite-field subspaces, computes Lie commutators directly in a basis of the free class-two algebra, evaluates normalizer constraints, and compares every observed stratum with the theorem. It checks all three- and six-dimensional cases listed in the proof over prime fields, along with a six-dimensional center's Gaussian intersection distribution.

The finite tests conclude with `ALL_NORMALIZER_STRATA_VERIFIED`. They verify the stated cases only; the general proof in `RESULT.md` is independent of these tests. The code does not cover nonprime fields, although the algebraic argument covers every prime power. Independent audit has not been performed.
