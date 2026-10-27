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

# Reproducibility and scope

On a system with Python 3 and a C++17 compiler, run `python3 verify.py`. It independently builds `count.cpp` and `count_reverse.cpp`, runs their complete enumerations, checks identical count tables, asserts \(9,765,625\) total transition pairs, and brute-forces all reset words up to the length-13 extremal witness. It independently constructs all state-conjugate and alphabet-swapped witnesses and checks the 240-element orbit.

Observed reproduction: all numerical assertions passed, including \(8,063,385\) synchronizing, \(1,702,240\) nonsynchronizing, \(5,071,440\) with one shortest reset word, and the sharp \(64\) maximum attained by \(240\) automata.

This finite exhaustive computation does not establish a formula for larger state counts or certify priority. No external independent audit has been performed.
