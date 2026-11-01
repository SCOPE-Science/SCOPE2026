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

# Reproduction

Run `python verify.py` with a standard Python 3.10+ installation. The program reconstructs complete multipartite graph examples, enumerates every face directly from maximum-part counts, computes forbidden-path membership independently using exact path dynamic programming when N <= 9, reproduces the pivot matching, and tests every directed Hasse edge for acyclicity via topological sorting. It also computes exact mod-two boundary ranks for examples with at most nine vertices, reduced Euler characteristics, and the claimed closed binomial formula.

In particular it reports B=306 for parts (4,4,4) and threshold 5; B=378 for the same parts and threshold 6; and finishes with ALL_VERIFY_OK.

# Scientific limits

The executable tests finitely many parameters and supplies no infinite verification certificate. Universal correctness follows from the mathematical proof in RESULT.md; the computation is a reproducible stress test. The closest preprint full text was inaccessible in the literature check; its abstract was read. No independent mathematical audit has been performed.
