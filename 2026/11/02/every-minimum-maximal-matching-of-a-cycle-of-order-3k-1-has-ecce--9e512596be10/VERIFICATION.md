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

# Verification record

The accompanying files `verify_direct.py` and `verify_two_token.py` run under ordinary Python 3 with no third-party libraries. Both programs were executed and completed without assertion failures.

The direct cycle-edge enumerator checked all minimum maximal matching configurations, all replacement edges, the bracelet-coordinate bijection and all eccentricities for cycle orders \(7,10,13,16,19,22\); the last line was `CYCLE_MATCHING_DIRECT_ALL_PASS`.

The independent separated-pair implementation checked every vertex's eccentricity and each explicit farthest-configuration witness for the cycle orders \(3k+1\) with \(2\le k\le20\); its final line was `TWO_TOKEN_ALL_ECCENTRICITIES_PASS`. For the tested orders at most 25 it additionally compared distances against a more general circular-transportation formula, but no unproved infinite assertion of this formula is included.

The proof in `RESULT.md` establishes the infinite theorem by a complete three-case upper-bound construction and a universal transportation lower-bound witness. The computations provide reproducible finite checks, not an independent scholarly audit or a formal proof certificate.
