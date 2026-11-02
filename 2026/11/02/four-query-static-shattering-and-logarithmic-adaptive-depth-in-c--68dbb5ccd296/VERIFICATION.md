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

# Verification instructions and boundaries

Execute `python3 verify.py` using Python 3.10 or later, no dependencies. It checks all 945 perfect matchings of ten ordered points using two distinct response computations (direct interval membership and prefix endpoint parity), checks the complete distribution of realized signatures with maximum 30, confirms a four-query shattered support at seven vertices, and matches independent cut and partition-label encodings for two through sixteen vertices. It also exhaustively computes small VC values and finite Littlestone dimensions via the standard minimax recurrence, and constructs/replays a complete adaptive tree for each small case.

`four_query_witnesses.json` supplies the 16 cut-pair witnesses for the four-query support. `depth_three_certificate.json` supplies a complete depth-three online decision tree for five vertices. The script regenerates the tree independently rather than treating JSON text as proof.

The universal VC upper bound is a finite exhaustive sublemma **plus** the endpoint-separation mathematical reduction in `RESULT.md`. The all-size adaptive lower bound is the mathematical threshold embedding, not an extrapolation of finite computations. No claim of a full exact adaptive formula beyond sixteen vertices, historical uniqueness or independent audit is made.
