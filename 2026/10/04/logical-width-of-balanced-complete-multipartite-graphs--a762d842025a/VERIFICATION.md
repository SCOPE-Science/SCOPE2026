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

The proof is symbolic. The upper bound explicitly reuses one pool of \(\max\{r,s\}+1\) variable names to enforce complete-multipartite structure, exactly \(r\) parts, and exactly \(s\) vertices in each part. The lower bound gives a permanent Duplicator strategy in the \(\max\{r,s\}\)-pebble game against a nonisomorphic balanced complete multipartite graph.

As a supplementary check, `verify_width.py` constructs atomic partial-tuple types for the two lower-bound witness graphs and verifies the back-and-forth move sets for every parameter pair \(1\le r,s\le4\). Running it with Python 3 produces exactly:

`VERIFY_OK cases=16 r_s_range=1..4 lower_witness_pebble_bisimulation`

This finite computation checks representative small cases of the pebble invariant. It does not extrapolate the theorem; the all-parameter argument is the proof in `RESULT.md`.
