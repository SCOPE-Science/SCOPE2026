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
The embedded `verify_rankmax_sexequal_stable_marriage.py` performs an exact finite replay using only the Python standard library.

It covers complete strict Stable Marriage markets with one, two, and three agents per side.

Stability is checked independently by:
1. precomputed rank maps;
2. direct preference-list positions.

Rank-maximality is checked independently by:
1. exact lexicographic comparison of the two-sided rank profile;
2. a steep-base integer objective with base \(2n+1\).

Sex equality is checked independently by:
1. absolute difference of the aggregate partner-rank sums of men and women;
2. absolute difference of the numbers of opposite-side agents preferred to the assigned partners, using \(r-1\) for an assigned rank \(r\).

The verifier confirms:
- equality of the two optimum sets for the one-agent market;
- equality on all \(16\) two-by-two profiles;
- stable-count marginal \(34080,11484,1092\) for the three-by-three domain;
- \(39084\) equality profiles;
- \(6204\) profiles with disjoint optimum sets;
- \(864\) profiles with \(X(I)\subsetneq R(I)\);
- \(504\) profiles with \(R(I)\subsetneq X(I)\);
- no nonempty nonnested overlap;
- total disagreement incidence \(631/3888\);
- disjoint incidence \(517/3888\);
- the displayed disjoint witness.

Run:

`python3 verify_rankmax_sexequal_stable_marriage.py`

The first output line must be:

`VERIFY_OK`

The computation proves only the stated first conflict layer through three agents per side.
