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

# Reproducibility and verification scope

The exact claims are proved in `RESULT.md`; `verify.py` supplies two independent finite corroborations. Use Python 3 standard library and run `python3 verify.py` from the package directory. Expected output: `VERIFY_OK`.

The script enumerates the complete 64-case six-input/four-output table of Rule 184 and the 32-case five-input central-output table of Rule 184 composed after Rule 226. It then compares the actual Rule-184 image with circular `1100` avoidance for every indexed binary ring of lengths 1–13 and checks the reflected-rule predecessor criterion on all these inputs. It independently evaluates fixed-weight inclusion–exclusion and weighted four-state matrix traces for lengths 1–18; the two expressions agree coefficientwise, and the unweighted totals satisfy the stated recurrence.

The exhaustive computations are finite and do **not** claim coverage of larger ring lengths; the locally complete truth tables, gap-counting argument and transfer-matrix proof give the all-length result. The verified output concerns ideal synchronous cyclic updates, not noisy or asynchronous traffic dynamics. No independent audit has been performed.
