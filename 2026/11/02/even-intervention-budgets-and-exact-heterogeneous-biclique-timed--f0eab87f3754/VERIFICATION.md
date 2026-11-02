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

# Verification notes

The included `verify.py` uses only the Python standard library. Executing `python verify.py` tested:

- 168 biclique threshold-multiset instances, independently comparing the compressed alternating count-state shortest path against full-state shortest path over all intervention subsets;
- 3860 labeled bipartite graph / threshold instances on at most five vertices, checking the even-minimum consequence with no parity or count compression in the verifier;
- 3025 uniform-threshold biclique parameter combinations, checking the closed formula.

All tests passed. The full-state method enumerates active configurations and all possible added targeted vertices at each transition, so it is independent of the claimed count compression. These finite tests are not infinite proofs and do not establish originality. The mathematical arguments in `RESULT.md` are necessary for the unrestricted-size claims. The code does not require any external package and does not make web requests.

Primary source date 2023-07-18 was taken from the first public arXiv posting, not the later journal appearance. Relevant source comparison: https://arxiv.org/abs/2307.09111 . No independent external audit or formal certification has been performed.
