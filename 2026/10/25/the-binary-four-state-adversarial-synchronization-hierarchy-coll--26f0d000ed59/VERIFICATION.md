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

# Reproduction and proof boundaries

Run `sh run_checks.sh` from the directory containing the extracted files. The script compiles `verify_alicefirst.cpp` with a C++17 compiler and runs `verify_bobfirst.py` and `verify_orbits.py` with Python 3; no third-party packages are required. `check_output.txt` contains the captured output of all three checks.

The C++ implementation enumerates every ordered pair of maps on each of three and four labeled states and evaluates Alice's choice before every bounded reply. Python independently evaluates Bob's choice before Alice's response using a quantified least fixed point, and explicitly checks the reachability closure of unbounded replies. A separate symmetry program enumerates all twenty-four state permutations and both alphabet orders, independently reconstructing the orbit partition.

Complete four-state results: \(14{,}016\) nonsynchronizing automata, \(26{,}160\) in the first but not second game class, \(2{,}976\) in the second but not third, and \(22{,}384\) in the unrestricted winning class. The corresponding quotient has \(359,551,62,502\) orbits. The exact total is \(65{,}536\) labeled tables and \(1{,}474\) symmetry classes.

Finite enumeration is exhaustive for the explicitly specified four-state, two-letter universe. Nothing is claimed about larger alphabets, additional states, or a general stabilization law. The game-to-pair equivalence is supplied mathematically in `RESULT.md` and the cited source, not inferred from program execution. The status above records absence of an independent external audit, not an assessment of one.
