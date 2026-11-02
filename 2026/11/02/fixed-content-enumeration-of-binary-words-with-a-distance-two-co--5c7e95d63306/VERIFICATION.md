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

# Reproducibility

Execute `python3 verify.py` with Python 3.8 or newer. No external packages or file inputs are required. A successful execution prints `VERIFY_OK` and selected complete coefficient arrays. For one specified length, execute `python3 verify.py 12` to print the coefficients in increasing weight.

The program checks the exact symbolic polynomial coefficients against **independent direct rotation/Hamming-distance enumeration** for all lengths 2 through 17. It checks the entire earliest-successful-shift weight distribution for all lengths 2 through 14; the 42 unweighted OEIS A179674 totals at lengths 2 through 43; the prime-weight equidistribution at sixteen odd primes through 59; coefficient positivity and complement symmetry; and divisibility of each coefficient by the length. Direct exhaustive testing beyond the stated finite ranges was not attempted. The all-length theorem is proved in `RESULT.md`, relying for the double-shift intersection characterization on the explicitly credited and inspected literature.

The only available review is self-review. No independent audit or external certification has been conducted.
