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

# Finite verification

Run `python3 verify.py` in a directory containing `verify.py`, `rt9_source.txt` and `certificate.json`; no third-party Python packages are required. The source data are the fifteen published regular-nine-tournament upper-adjacency strings. The certificate contains full nonempty-face matchings and critical faces for each representative.

The verifier performs the following exact checks, reconstructing everything from these files rather than trusting a prerecorded log: the input has fifteen distinct valid 36-bit strings; every decoded tournament is four-out-regular; every pair of decoded tournaments is nonisomorphic by graph-isomorphism backtracking; every face is in the downward closure of nine out-neighborhood facets; every face occurs in exactly one matched pair or as a critical cell; every matched pair is a cover relation; the directed Hasse graph is acyclic; the critical multiplicities match the claimed homotopy types; and independently reconstructed signed simplicial boundary matrices give the same rational and binary ranks in every dimension.

The most delicate homotopy case is catalogue index 9. The verified Morse matching leaves exactly one zero-cell, one one-cell and one two-cell. Exact rational homology in degree two has dimension one, so the attaching degree is exactly zero over the integers. This proves its wedge decomposition; finite-field rank agreement alone would not be enough for that step.

The execution output in `verification_output.txt` records fifteen completed rows and the final pass marker `REGULAR_NINE_TOURNAMENT_NEIGHBORHOOD_FULL_HOMOTOPY_CENSUS_OK`. The catalogue's exhaustiveness is an externally sourced mathematical input, not a consequence of the verification script. This check is not independent external validation.
