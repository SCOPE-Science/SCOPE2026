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

# Verification evidence

The infinite proof is given explicitly in `RESULT.md`. Two independent finite tests complement that proof without substituting enumeration for its all-orders statement.

Execute `python3 verify_exact_cover.py` to exhaustively list edge-neighborhood exact covers in \(GP(n,2)\) for \(5\le n\le30\). Output is stored in `exact_cover_output.txt`; success ends with `EXACT_COVER_OK`.

Execute `python3 verify_local_states.py` to exhaustively enumerate cyclic outer black/white patterns, determine inner states, and check every black vertex has precisely one black neighbor while every white vertex has no white neighbor, for \(5\le n\le20\). Output is stored in `vertex_states_output.txt`; success ends with `VERTEX_STATES_OK`.

Both checks have been executed and their full outputs captured. The exact-cover script tests the complete predicted edge sets and their partition when \(5\mid n\), rather than only matching counts. The second checks an independently constructed vertex-adjacency model. Neither finite run establishes the infinite theorem alone; the gap-alternation argument provides the all-orders proof.

Scientific limitations: the full 2018 Yang–Wu article was inaccessible, leaving an explicit residual prior-art comparison risk. Independent external scientific audit: not performed.
