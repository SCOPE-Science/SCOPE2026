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

Use Python 3 with no third-party packages. In a directory containing `RESULT.md` and `verify.py`, run `python3 verify.py`. It prints `VERIFY_OK` when all checks succeed.

The checker computes the first 65,535 positive terms from the original recurrence, verifies the binary high-bit formula on 32,768 odd terms, reduces every positive index to its odd part, checks the exact four-class dyadic census for each exponent from one through sixteen, checks the matrix fourth power, and compares the rational coefficient formulas with the independently computed digital sums. These are finite reproducibility checks only.

The unrestricted proof uses parity recurrences, induction on binary digits, two exact matrix identities, Cauchy--Schwarz bounds on arbitrary aligned binary intervals, and an explicit family of sharp dyadic examples. No independent audit has been performed. Priority and extensions outside modulus eight remain open to external assessment.
