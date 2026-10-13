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
The embedded `verify_rankmax_minregret_boundary.py` performs an exact finite replay using only the Python standard library.

It exhausts all
\[
(2!)^4=16
\]
complete strict \(2\times2\) profiles and all
\[
(3!)^6=46656
\]
complete strict \(3\times3\) profiles.

Every perfect matching is tested for stability independently by:
1. precomputed rank-table blocking-pair checks;
2. preference-list-position scans.

Every stable matching's two-sided rank profile and regret are independently computed by:
1. precomputed rank dictionaries;
2. direct list-position lookup.

The implementations agree on every tested matching.

The replay verifies:
- \(P(I)=G(I)\) for all \(16\) two-couple profiles;
- three-couple relation counts \(37716\) equality, \(6984\) proper \(P(I)\subsetneq G(I)\), and \(1956\) disjoint;
- no proper \(G(I)\subsetneq P(I)\) case and no nonnested overlap;
- three-couple stable-matching-count distribution \(34080,11484,1092\);
- every incompatible profile has a unique minimum-regret optimizer;
- incompatible profiles split as \(1728\) with two stable matchings and \(228\) with three;
- rank-maximal optimizer sizes \(1872\) singleton and \(84\) doubleton within the incompatible set;
- \(29\) incompatible isomorphism classes under all independent side relabelings and side exchange;
- orbit-size distribution \(26\) of size \(72\), \(2\) of size \(36\), and \(1\) of size \(12\);
- the displayed witness.

Run:

`python3 verify_rankmax_minregret_boundary.py`

The first output line must be:

`VERIFY_OK`

The exhaustive statement stops at \(3\times3\).
