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

# Reproducibility and limits

Run `python3 verify_wc_universality.py` using Python 3 and its standard library. Its success line is `WC_UNIVERSAL_VERIFY_OK symmetric_hosts=32199 literal_checks=2647 bivariate_profiles=24 shortest_classifications=10`.

The test independently constructs the involution-fixed words, computes greedy arch counts, tests literal embeddings for every target pattern in the bounded independent-check ranges, expands the all-alphabet rational formula using surjection counts, and enumerates the shortest permutation-block constructions. It checks half lengths 0 through 9 (binary), 0 through 7 (four letters), and 0 through 5 (six letters), and shortest-host classification for ten parameter cases. It does not establish the infinite statement by exhaustion; the rigorous proof is in RESULT.md.

The result uses a fixed-point-free letter pairing. It makes no claim about involutions with fixed symbols. The checked source comparisons do not certify worldwide novelty. Independent scientific audit: not performed.
