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

The package contains the two complete, standalone source files `verify_circular_pal_lengths.py` and `verify_circular_pal_lengths.cpp`; they do not rely on downloaded tables or third-party libraries. Their inputs are exactly the order-five binary state graph and the definitions of palindromes and de Bruijn cycles in `RESULT.md`.

Run `python3 verify_circular_pal_lengths.py`. The program independently constructs the cycle set by full feedback-table enumeration and by Euler-tour enumeration, then compares interval-palindrome dynamic programming with center-expansion shortest paths across all 65,536 roots. Its successful output begins with `VERIFY_OK` and includes the full rooted, best-root and joint spectra.

Compile `c++ -O2 -std=c++17 verify_circular_pal_lengths.cpp -o verify_pal` and run `./verify_pal`. The separate C++17 program independently enumerates Euler tours and repeats all spectrum and extremal assertions. It too returned `VERIFY_OK` on execution.

The finite coverage argument is: all \(2^{16}\) feedback tables are tested, every de Bruijn cycle yields exactly one such full-period feedback table, and all 32 possible cuts of every accepted cycle are evaluated. The center-expansion and interval recurrence are exact integer algorithms, not Monte Carlo approximations. No external solver certificates, analytic continuation, or unbounded inference are required.

These checks establish reproducibility of the specified finite computation. They do not by themselves establish novelty beyond all historical literature or independent external validation. No higher-order or other-alphabet result is certified.
