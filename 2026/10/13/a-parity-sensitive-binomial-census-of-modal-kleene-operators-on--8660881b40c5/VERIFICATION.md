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

Run `python3 verify_kleene_chain.py` using Python 3 standard library. The script exhaustively enumerates \(\binom{2m-1}{m}\) monotone maps for each \(1\le m\le10\); it tests positivity and consistency by direct quantification for every enumerated map, compares the four derived binomial formulas, and prints `VERIFY_OK` only if all comparisons pass. The check was run against the packaged source code and returned `VERIFY_OK`. No external datasets or prior-run output are required.

The proof covers arbitrary positive integer chain size through a complete low/high normal form and binomial identities. These finite enumerations do not independently establish the all-size conclusion. The 2026 primary preprint's full text could not be inspected; scientific comparison is limited to its accessible abstract, detailed secondary synopsis, and targeted searches, so full-text originality checking remains open. Independent audit has not been performed.
