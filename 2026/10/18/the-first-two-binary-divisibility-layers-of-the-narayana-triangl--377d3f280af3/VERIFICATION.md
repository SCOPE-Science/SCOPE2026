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

# Reproduction and limits

Run `python3 artifacts/verify.py` with standard Python 3 from the directory containing `RESULT.md`. No third-party packages, downloaded input, or external services are required. It independently calculates valuations using both exact integer binomial products and the binary digit-sum formula, checks the first 127 complete Narayana rows by both methods, verifies both local formulas for all \(1\le m\le256\), and replays complete dyadic cutoffs through \(L=10\). The expected final line is `VERIFY_OK`.

The proof in `RESULT.md` derives all-length geometric sums by binary-submask counting. Finite replay does not verify infinite quantifiers, originality, or future application. The mathematical literature comparison includes one inaccessible full article; independent audit has not been performed.
