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

# Reproduce the finite certificates

Keep `verify.py` beside `witnesses.tsv`, then run `python3 verify.py` with an ordinary Python 3 interpreter (standard library only). A successful run prints `VERIFY_OK normalized_candidates=80 failed_strict=80 failed_plus=76 surviving_plus=4 finite_source_words=22 boundaries=8/3,5/2`.

The certificate is a TSV containing one finite input word and one output factor forbidden at the relevant boundary for each excluded normalized image. Each row specifies image length, rational threshold, strict/weak flag, image of zero, source word, zero-based factor start, factor length, factor period and the factor itself. The verifier regenerates the rows, checks source admissibility and output violation by exhaustive factor-period search, compares all rows exactly, and tests the listed four positive survivors against the finite conditions of Kobayashi's sufficient criterion as stated in [1, Theorem 4]. In a second path it calculates maximal finite-word exponents using exact rational arithmetic.

Every strict failure and every weak failure has a finite violating input of at most four letters. The positive global conclusion is conditional on the published theorem: finite tests alone do not establish preservation for arbitrary input length. No independent audit was performed. Scope limitations and literature comparisons appear in `RESULT.md` and `REVIEW.md`.

Reference: Shallit, Shur and Zorcic, *Power-free Complementary Binary Morphisms*, arXiv:2310.15064 (2023), Theorem 4, https://arxiv.org/abs/2310.15064 .
