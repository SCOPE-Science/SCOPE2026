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

The package contains `verify.cpp`, `crosscheck.py`, and `alpha.csv`. Compile `verify.cpp` using `g++ -std=c++17 -O3 verify.cpp -o verify` and execute `./verify` in the same directory. It should enumerate all length-3 through length-15 exact code maxima and end with `VERIFY_OK`.

Run `python3 crosscheck.py` to reconstruct all direct one-duplication descendant sets for every binary input and solve their exact compatibility graphs for source lengths three through nine, ending with `CROSSCHECK_OK`. This cross-check does not rely on the derivative or composition reduction.

The C++ algorithm generates the same 56 graph types whose exact independence numbers are listed in `alpha.csv`, proves each maximum by an exhaustive color-bound branch-and-bound enumeration, and checks every codeword and every duplicated output of the constructed code. The external-table file is supplied for human inspection, not substituted for executable checking.

No independent scientific or external audit was performed. The exhaustive domain ends at length fifteen. Reproduction depends on a C++17 compiler that supports GCC's bitset set-bit iteration extension; `crosscheck.py` uses the Python standard library.
