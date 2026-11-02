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

Run `python3 VERIFY.py` using a standard Python 3 interpreter. Expected line: `VERIFY_OK mid_states=354 mid_policy=172 mid_leaves=17 high_states=431 high_policy=210 high_leaves=24 upper_paths=243`.

`mid` verifies one strategy simultaneously at \(H=1,2,4\). Affine inequalities on \([1,2]\), and monotone-quadratic/self-high versus affine/other-high inequalities on \([2,4]\), extend these endpoints to all real \(H\) in the intervals. `high` uses a stronger high-value-independent predicate sufficient for all real \(H\ge4\). The upper-bound adversary is exhaustively replayed for every one of the 27 three-step allocator histories and nine subsequent choice pairs, and each final path supplies a single pairwise envy inequality valid over the whole interval \([2,4]\) and another valid for \([4,\infty)\).

These exact finite-game calculations establish the stated finite horizon. The script does not verify novelty in literature or generalize to other horizons. No independent audit has been performed.
