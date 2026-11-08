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

Run `python verify.py` in the directory containing this document and `RESULT.md`, using Python 3.9 or newer. The checker uses only the standard library. It builds the exact transition kernel on all macro-states `(u,v,k)` for the four even leaf counts `2,4,6,8`, uses rational linear algebra to solve for terminal-class probabilities and first two moments of the first terminal-class entrance time, and checks the analytic formulas for every state. The observed result was `VERIFY_OK 480 exact-rational state identities`.

The theorem's all-even-size validity rests on the case-by-case mathematical proof in `RESULT.md`. The finite checks do not establish a universal theorem, and no conclusion is claimed for odd leaf counts, asynchronous rules, or other tie conventions. Literature priority was checked on a best-knowledge basis and is not independently certified.

Independent external audit: not performed.
