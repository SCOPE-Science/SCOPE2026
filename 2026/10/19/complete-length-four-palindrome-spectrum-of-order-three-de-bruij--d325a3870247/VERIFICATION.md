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

The program `verify.py` uses the explicit macroedge construction from the proof and checks, for every constructed cyclic word, all cyclic length-three factors (each of the alphabet's \(q^3\) triples must occur once) and palindromic cyclic length-four factors. Tested every spectrum value for integer alphabet sizes \(2\) through \(8\), plus all permitted local transition systems on the ternary alphabet.

The independent C++ checker `check_ternary.cpp` enumerates all cyclic ternary order-three tours with a fixed initial triple, totaling exactly \(373248\). Its counts for 0, 1, 2, and 3 length-four palindromes were respectively 55296, 165888, 124416, and 27648.

Reproduction: `python3 verify.py` and `g++ -O2 -std=c++17 check_ternary.cpp -o check_ternary && ./check_ternary`.

Both programs check finite cases only. Correctness for all alphabet sizes depends on the mathematical argument in RESULT.md. Independent human or external audit has not been performed.
