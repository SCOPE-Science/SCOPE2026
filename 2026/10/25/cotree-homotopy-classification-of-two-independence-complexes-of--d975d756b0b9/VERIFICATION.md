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
# Verification and scientific limits

The proof uses exact simplicial identifications for disjoint union and graph join, plus the standard join–smash relation and the one-cell attachment formula. No computational output is needed to infer the infinite-family statement. To independently sanity-check the recurrence on small graphs, run `python3 verify_cograph_ind2.py`. This stdlib-only checker independently generates 240 random cographs on one through ten vertices from cotrees; it then enumerates all allowed faces and computes reduced homology via mod-two boundary matrices, comparing each result to the cotree recurrence. A ninth-order mixed-dimensional example is checked as well. Expected terminal line: `REPLAY_OK: 240 cotrees with 1..10 vertices plus a 9-vertex mixed-dimensional example.` This checks only these finite instances and does not verify infinite quantifiers or exhaustive originality. Full reconstruction of the proof is in RESULT.md; the scope and comparison limits are in REVIEW.md.
