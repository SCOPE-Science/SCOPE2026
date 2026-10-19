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

Two separate standalone standard-library Python checkers were run on their actual packaged source before acceptance. Run `python3 prism_verify.py` and compare its standard output to `prism_verify_output.json`; it directly enumerates colorings and single alternating-cycle switches for every order from 3 to 11. Run `python3 prism_transfer_verify.py` and compare its output to `prism_transfer_verify_output.json`; it independently counts the cyclic words and exceptional off-diagonal configurations for orders 3 to 12. Both returned without failed assertions. The proof of the infinite theorem is the color-recursion and bichromatic-component argument in RESULT.md; the computations are corroboration only. External independent audit has not been performed. The programs do not certify graph diameter or a complete adjacency isomorphism class.
