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
# Verification of the finite classification

The claim concerns all binary order-four cyclic de Bruijn words; this is a finite complete domain. Source `verify.py` (Python 3, standard library only) reconstructs all \(2^{16}\) binary sixteen-symbol words. A word is retained precisely when its sixteen cyclic length-four factors are distinct; this criterion gives \(256\) rooted words and \(16\) rotation classes.

Run `python verify.py` with `CENSUS.csv` in the same directory. An actual run of the included source returned:

`VERIFY_OK all_binary_16_words=65536 rooted_debruijn=256 cycles=16 unique_four_window_hittings=1 four_roots=192 five_roots=64 orbit_classes_8_12_16=4_8_4 universal_five=verified`

The program first checks all \(\binom{19}{4}\) possible four-position sets to verify that only the positions \(\{3,7,11,15\}\) hit all sixteen length-four windows. It then tests full factor covering directly for each of the \(256\) roots, for factor lengths \(1,\ldots,19\), and separately for lengths up to four, asserting agreement. For each root the four-set qualifies exactly when the full optimum is four; it also explicitly checks that \(\{3,6,9,12,15\}\) covers every full factor. It reconstructs and matches all sixteen certificate rows. These are zero-based positions.

The deductive proof in `RESULT.md` supplies the uniqueness/lower-bound and long-factor reduction; the code and complete certificate supply finite exhaustive classification, not an extrapolation. Verification does not address unindexed priority, higher de Bruijn orders, alternative alphabet sizes, online/circular attractors, or independent external validation.
