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

Run `python3 VERIFY.py` from the same directory as this document and the other files. The script generates the finite Thue–Morse words from the substitution, exhaustively enumerates factor sets and minimal absent words for orders 3 through 9, compares their exact length distributions to the formula, and checks uniqueness at the threshold lengths. It separately compares infinite-context pair patterns in a length-4096 iterate through substitution level five. The program prints `VERIFY_OK` on success.

These finite computations do not establish the result for every order. The unrestricted mathematical proof and its dependence on the known bispecial-factor classification are given in `RESULT.md`. The cited primary factor-graph source was read in its author-hosted full text; its graphical portions were not essential for any new proof step. Independent audit has not been performed.
