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

With `verify_power_pair.py` adjacent to the scientific result, run `python verify_power_pair.py` using Python 3. The script computes expected nearest-facility costs from all six unordered pairs of four *indexed* agents using `fractions.Fraction` and compares with the closed-form formula on 805 exact inputs. It checks 322 exact local non-manipulation inequalities at integer exponents one and two, the cubic deviation improvement \(4/3705\), polynomial sign witnesses, and 1001 exact positive-report polynomial inequalities. No numerical floating-point tolerance is required.

The independent proofs for every real exponent in the stated ranges are given in RESULT.md: exponent-convexity for \(0<lpha\le2\), exponent-monotonicity for \(lpha\ge3\), and exact polynomial signs for the cubic interval. The finite grid is not an exhaustive test of real reports or exponents and does not by itself establish the universal claims.

Independent audit: not performed.
