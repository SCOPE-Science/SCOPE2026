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
The embedded `verify_popular_rankmax_boundary.py` is an exact finite replay using only the Python standard library.

Popularity is computed twice:
1. direct head-to-head majority comparison against every perfect matching;
2. the strict-list structural characterization using first-choice posts and each applicant's most-preferred non-first-choice post.

Rank-maximality is computed twice:
1. direct lexicographic comparison of rank signatures;
2. an independent exact steep-base integer objective with base \(n+1\).

The verifier exhausts all \(4\) complete strict \(2\times2\) profiles and all \(216\) complete strict \(3\times3\) profiles. It confirms:
- \(R(I)=P(I)\) for every \(2\times2\) profile;
- exactly \(138\) three-applicant profiles with \(R(I)=P(I)\);
- exactly \(72\) with \(R(I)\subsetneq P(I)\);
- exactly \(6\) with \(P(I)=\varnothing\);
- those six are exactly the identical-preference profiles.

It also checks all \(24\) perfect matchings of the displayed \(4\times4\) witness and confirms four rank-maximal matchings of common signature \((2,1,1,0)\), exactly two of which are popular.

Run:

`python3 verify_popular_rankmax_boundary.py`

The first output line must be:

`VERIFY_OK`

No larger-market universal statement is inferred from the finite computations.
