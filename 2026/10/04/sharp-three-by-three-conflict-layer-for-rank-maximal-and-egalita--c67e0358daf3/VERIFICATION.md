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
The embedded `verify_rankmax_egalitarian_stable_marriage.py` is an exact finite replay using only the Python standard library.

It exhausts all complete strict \(2\times2\) and \(3\times3\) profiles and every perfect matching in each profile.

Stability is checked independently by:
1. precomputed rank maps;
2. direct preference-list positions.

Rank-maximality is checked independently by:
1. lexicographic comparison of the two-sided rank profile;
2. a steep-base exact integer objective with base \(2n+1\).

Egalitarian optimality is checked independently by:
1. direct total partner-rank cost;
2. the profile identity \(c(M)=\sum_k k\,p_k(M)\).

The verifier confirms:
- equality of the two optimum sets on all \(16\) two-by-two profiles;
- stable-count marginal \(34080,11484,1092\) for the three-by-three domain;
- \(42756\) equality profiles;
- \(2928\) strict \(R(I)\subsetneq E(I)\) profiles;
- \(972\) disjoint profiles;
- no reverse containment and no nonnested overlap;
- exact disjoint incidence \(1/48\);
- the displayed disjoint witness.

Run:

`python3 verify_rankmax_egalitarian_stable_marriage.py`

The first output line must be:

`VERIFY_OK`

The computation proves only the stated two-by-two lower bound and complete three-by-three first conflict layer.
