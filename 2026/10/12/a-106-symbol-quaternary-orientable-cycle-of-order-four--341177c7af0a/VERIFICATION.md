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
# Reproducing the finite witness

The witness consists of exactly \(106\) digits in `witness.txt`, read cyclically. No generation algorithm or unverified optimization solver is needed to verify the mathematical existence result.

With a Python 3 interpreter, run `python3 verify.py` from the directory containing the files (the script locates the witness beside itself). This builds all cyclic four-windows, checks no window equals its reversal, checks all \(106\) reversal-orbit identifiers are different, enumerates the complete \(120\)-class nonpalindromic universe, and checks the list of \(14\) omitted orbits. Expected output: `VERIFY_OK period=106 windows=106 reversal_orbits=106 unused_orbits=14`.

With a conforming C11 compiler, run `cc -std=c11 -O2 -Wall -Wextra -pedantic -o verify_c verify.c && ./verify_c` while in the directory containing `witness.txt`. The independently written program checks each of the \(106\) windows is not a palindrome and that all \(\binom{106}{2}=5565\) distinct-position pairs differ in either orientation. Expected output: `VERIFY_OK cyclic_length=106 all_5565_factor_pairs_distinct_under_reversal`.

The mathematical implication requires only the definition of an order-four orientable cycle: since every cyclic factor occurs at most once in either direction, its period provides a lower bound for \(M_4(4)\). Neither checker proves an upper bound or global maximality. Independent scientific auditing has not been performed.
