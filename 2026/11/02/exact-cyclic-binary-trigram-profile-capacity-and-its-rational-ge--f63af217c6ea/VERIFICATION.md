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

# Verification instructions

The proof is symbolic for the stated range of lengths at least three; finite programs serve as independent error checks.

Run `python3 verify.py`. It compares the rational coefficients with the disjoint connected-support case sums at all orders 3–80, enumerates balanced connected de Bruijn edge multisets at 3–22, and directly enumerates all binary words at 3–16. Successful output is `VERIFY_OK: 78 rational/case coefficients, 20 graph-connectivity counts, 14 direct word censuses`.

For a separate implementation, compile `crosscheck.cpp` using `c++ -std=c++17 -O3 -o checker crosscheck.cpp` and run `./checker`. It uses bit-packed independent profile keys and exhaustive inputs at orders 3–21. Successful output is `CROSSCHECK_OK: all binary cyclic words length 3..21`.

The CSV `counts.csv` lists the expected exact coefficients from order 3 through 50. All programs require only standard facilities. Tests do not establish historical priority and finite enumeration does not replace the all-length argument.
