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

Run `python verify_rank8.py` with Python 3. The checker uses only the standard library and confirms three differential annihilator identities, all three Buchberger pairs for the eight-point ideal, and the explicit ideal-inclusion certificate. A successful run prints `VERIFY_OK`.

The exact eight-point count uses the homogeneous leading ideal \((XY,Y^3,X^6)\) and the eight distinct points on \(Z=1\). The seven-point impossibility is a universal geometric argument written in RESULT.md, not a finite computational certificate. Self-review is reported separately; an independent audit has not been performed.
