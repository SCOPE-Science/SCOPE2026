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
The included `verify.py` calculates the claimed closed rank distribution over finite fields and independently enumerates all compatible Lie maps through matrix brackets in three small cases. It performs exact modular Gaussian elimination to obtain each image rank and compares distributions. Run `python verify.py`; a successful run prints `VERIFY_OK`. Checked examples: `m=1,q=2` gives `[1,21,18,24]`, `m=1,q=3` gives `[1,104,192,432]`, and `m=2,q=2` gives `[1,465,15750,37800,0,11520]`. The program also checks the zero-rank gap in selected larger parameters. The infinite formula and fixed-field asymptotic rely on the written proof, not the finite computations. No independent audit is claimed.
