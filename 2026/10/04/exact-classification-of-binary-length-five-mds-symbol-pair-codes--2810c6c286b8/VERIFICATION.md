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
# Verification

Run `python verify.py` with a standard Python 3 interpreter. The script has no third-party dependencies. It rebuilds the entire finite instance instead of trusting `maxima.json`.

The verification steps are:

1. Generate all \(32\) binary words of length \(5\).
2. Recompute cyclic symbol-pair distance directly from adjacent ordered pairs.
3. Build the compatibility graph for threshold \(d_{\mathrm p}\ge4\).
4. Exhaustively enumerate all maximal cliques by Bron–Kerbosch recursion with an exact size bound; obtain \(118\) maximal cliques, largest size \(8\), and exactly \(20\) maxima.
5. Translate every maximum inside \(\mathbb F_2^5\) and test additive closure; obtain \(20\) affine maxima, five direction subspaces, and four cosets per direction.
6. Verify that the five directions are exactly the five cyclic shifts of the displayed base direction.
7. Exhaust the stated \(320\)-element pair-metric isometry subgroup; its orbit on one maximum is the complete set of \(20\) maxima, and the directly counted stabilizer has order \(16\).
8. Recheck every pair of words in every maximum directly against the distance definition.

Expected final output:

`VERIFY_OK maximum=8 labeled_maxima=20 maximal_cliques=118 affine_maxima=20 direction_subspaces=5 cosets_per_direction=4 orbit_size=20 stabilizer=16 group_size=320`

The proof is a complete finite search over the specified domain. It does not establish corresponding classifications for other lengths, alphabets, or distance thresholds.
