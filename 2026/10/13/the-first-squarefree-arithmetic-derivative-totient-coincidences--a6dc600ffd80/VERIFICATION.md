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

Run `python3 verify.py`; no external dependencies are required. The seven rational final-prime candidates are recomputed with exact fractions, then checked for integrality and primality. A direct comparison on all squarefree inputs \(1\le n\le20,000\) is a supplemental finite check. The infinite theorem rests on the written parity and inequality proof, not on this bound. The verification is a self-review; independent audit has not been performed.
