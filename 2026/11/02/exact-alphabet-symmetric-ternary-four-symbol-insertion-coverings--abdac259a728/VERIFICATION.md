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

## Reproducible checks

The executable `verify.py` uses only the Python standard library. The independently implemented `verify_independent.cpp` uses C++17 with no third-party libraries. Both generate all \(81\) possible source words and all \(243\) target words, calculate deletion subsequences, reduce the word sets to \(14\) and \(41\) symbol-permutation orbits, and exhaustively check all \(2380\) candidate choices with fewer than six nonconstant source orbits and all \(1716\) candidate choices with exactly six. Both report zero smaller coverings, exactly \(37\) equal-sized symmetric coverings, five reversal-fixed optima and sixteen reversal pairs, and valid coverage by the explicit \(31\)-word asymmetric witness. The recorded direct execution results are in `verification_output.txt`.

Commands: `python3 verify.py`; `c++ -std=c++17 -O2 verify_independent.cpp -o verify_independent && ./verify_independent`.

The proof depends on complete finite enumeration within the established orbit reduction, not on extrapolation from partial enumeration. The checks do not certify a value for the unrestricted optimum or any larger blocklength. Independent external audit has not been performed.
