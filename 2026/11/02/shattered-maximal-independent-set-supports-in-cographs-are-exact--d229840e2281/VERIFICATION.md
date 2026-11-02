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

# Verification and limits

Execute `python3 verify_cograph.py` with Python 3. The script enumerates every graph on zero through five labeled vertices, constructs maximal independent sets by checking both independence and maximality, enumerates all trace supports and orientations of every induced matching, and checks their equality for every cograph. It also checks cotree polynomial recurrences, strict-inequality exceptions, and permutation-isomorphism classes. The success markers are `COGRAPH_COMPLETE_SMALL_GRAPH_CENSUS_PASS`, `INDUCED_MATCHING_SUPPORTS_AND_POLYNOMIALS_PASS`, and `SMALLEST_FIVE_VERTEX_GAP_PASS`.

The finite check does not establish the theorem for arbitrarily many vertices. The mathematical proof uses the cograph union/join induction, especially the missing-empty-trace lemma. No independent audit or external validation has been performed; bibliographic priority is not certified.
