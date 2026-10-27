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

# Reproducibility and verification

The attached `verify.py` implements the parallel Rule-184 Boolean update directly, detects the first entrance into the appropriate free-moving terminal regime, and compares both the exact Catalan extremal count and the strict-record witness with finite enumeration. It runs using Python 3 standard library only.

Run `python verify.py` from the directory containing the attached verifier. The recorded output from this package's source was:

```text
VERIFY_OK exhaustive_n=3..16 random_cases=10500 checks=289999 ring_sizes=14
```

Every binary configuration of sizes \(3\) through \(16\) was processed; 10,500 configurations on larger rings were sampled deterministically. The proof's unrestricted \(n\) claim depends on the min-plus/strict-record/Catalan argument, not the experiments. No independent audit or certification has been conducted. External historical-priority uncertainty remains.
