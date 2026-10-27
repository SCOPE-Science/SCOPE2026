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

Run `python3 check_rankings.py` with Python 3.9 or later. The script has no external dependencies or network interactions.

It builds all 120 strict rankings of five candidates, all nondecreasing index triples of these rankings (exactly 295240 output multisets), and the integer quotas for positional, pairwise, and exact-prefix-set proportionality. Independently of the lower-quota code path, it checks each displayed witness by looping over all integer thresholds in the original axioms. The exact multiset counts are 5 for positional+pairwise, 44 for positional+PSC, 6 for pairwise+PSC, and 0 for all three. It checks the eleven support counts used by the analytic contradiction and selected replicated/padded instances.

# Verification scope

The analytic contradiction in `RESULT.md` is the proof of impossibility; the exhaustive enumeration independently corroborates the finite base case and supplies exact counts. The replication and padding arguments, rather than the bounded tests, establish the infinite family. No separate independent review has been performed. No minimality or probabilistic claims are made.
