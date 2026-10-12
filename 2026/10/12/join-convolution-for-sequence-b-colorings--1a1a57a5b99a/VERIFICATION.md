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

The analytic proof is the primary evidence.

The script `artifacts/verify.py` performs two independent finite checks.

First, it enumerates every labeled connected graph on one, two, or three vertices. For every ordered pair it forms the join and brute-forces all surjective proper colorings for every possible color count. It computes color-dominating vertices from closed neighborhoods and records the exact non-increasing CDV-count vectors of all b-colorings. The observed profile of each join is compared with the set of sorted concatenations of the two factor profiles.

Second, it enumerates every complete multipartite part profile of total order at most six. It brute-forces all colorings, verifies that b-colorings exist only with exactly the number of partite classes, and compares the direct labeled realization counts for every non-increasing requirement sequence with
\[
\prod_{i=1}^r(c_i-i+1).
\]

The finite search is corroborative only. It does not establish the general theorem, which is proved analytically in `RESULT.md`.
