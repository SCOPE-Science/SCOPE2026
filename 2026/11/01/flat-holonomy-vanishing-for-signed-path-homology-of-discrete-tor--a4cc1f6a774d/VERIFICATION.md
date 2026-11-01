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

# Verification instructions

Run `python3 verify.py` using the Python standard library only. The program reproduces the signed seam models and tests all holonomy patterns in sample one-, two-, and three-dimensional Cartesian products of long cycles, computing cubical local-system boundary ranks modulo two distinct large primes. It checks square flatness, explicitly realizes the signed double cover as a quotient of a longer product, and verifies connectedness in unbalanced cases. It additionally builds the actual signed GLMY allowed path and nonallowed-shortcut matrices in degrees zero through two in twelve models, and verifies the predicted degree-zero and degree-one ranks. The last lines should include `VERIFY_OK 22 signed_tori 8030 cubical_cells` and `GLMY_DIRECT_VERIFY_OK 12 signed models`.

The cubical computations do not themselves establish arbitrary-degree GLMY homology. The direct GLMY calculations do not themselves establish degrees two and above. The unrestricted result follows from the detailed square-faithful lifting lemma plus the published path Künneth theorem and the deck-action argument in RESULT.md. Independent mathematical auditing has not been performed.
