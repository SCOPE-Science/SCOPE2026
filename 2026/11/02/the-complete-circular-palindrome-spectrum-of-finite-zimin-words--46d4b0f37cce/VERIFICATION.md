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

`checker.py` is an ordinary, self-contained Python 3 checker. Run with `python3 checker.py`. It constructs each complete finite Zimin word for ranks 1–8, exhaustively enumerates circular factors of all lengths at most the word's length, filters palindromes, and checks set equality against the explicit rank-marked odd language and the seam-centered even family. It additionally checks lengthwise multiplicities and verifies that all predicted odd circular palindromes already occur in the linear word. Observed counts by increasing rank: `1,4,10,22,46,94,190,382`, followed by `CHECK_OK`.

This is finite testing; mathematical validity for arbitrary rank follows from the proof in `RESULT.md`, not the checker. Source access did not permit full-paper historical comparison with Simpson (2014). No independent mathematical assessment has been performed.
