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

The complete proof is contained in `RESULT.md`. Re-run the actual standalone file `VERIFY.py` with Python 3 using `python VERIFY.py`; it requires only the Python standard library. A successful run prints `VERIFY_OK` and the counted frequencies.

The checker tests every candidate prime pair in the near-Mersenne strip for all \(1\le k\le10\), comparing the theorem's rational interval and modular condition with direct coefficient-based subset-sum testing. It additionally reproduces all unrestricted published counts for these ten exponents, checks the bound for each eligible weird number, and for \(k\le3\) independently enumerates subset sums from the actual proper divisors. The near-strip comparison encompasses 186282 candidate prime pairs.

The substantive infinite proof is the short-residue contradiction in Step 2 of `RESULT.md`. The finite checker verifies instances but cannot alone prove the theorem. No independent audit has been performed, and an equivalent statement in unindexed literature remains a possible originality risk.
