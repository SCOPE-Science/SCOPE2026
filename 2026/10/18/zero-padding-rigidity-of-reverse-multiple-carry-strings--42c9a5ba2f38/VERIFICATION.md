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
# Verification information

The central exact proof is in `RESULT.md`. Reproduce all finite checks with `python3 verify.py` (Python 3 standard library only). The script re-derives carries directly from grade-school base multiplication rather than accepting the displayed digit–carry identity as an oracle; it enumerates every allowed digit string in bases \(3\) through \(16\) and lengths \(2\) through \(5\), tests all candidates for multiplier \(2\le n<b\), and checks the boundary claim on the valid strings. It separately checks the two necessary divisibilities for every base \(3\) through \(35\) and valid interior carry pair. Expected successful counts: 3,103,793 digit strings; 150 valid palintiples; 56 with highest carry zero; and 117,810 modular tuples.

These are finite regression checks only. The infinite statement follows from the exact identity and divisibility contradiction in the proof, not from the absence of counterexamples in these finite ranges. The mathematical conclusion is restricted to intact contiguous source strings with only outer zero padding. Independent assessment has not been performed.
