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

# Verification record

Two programs were saved as `verify_python.py` and `verify_cpp.cpp`, with their actual execution outputs as `verify_python_output.txt` and `verify_cpp_output.txt`. Source programs were inspected and then run as actual standalone files.

The Python checker evaluates every initial state and proposed output on odd labelled cycles from 3 through 19 vertices, including all inverse fiber sizes, total recurrent states, fixed points, full primitive two-cycle basins and the claimed unique maximum. All assertions passed.

The separately implemented C++ checker uses a different native-bitmask update and integer Fibonacci implementation, and checks the same complete properties through 21 vertices, including 2,097,152 initial states at that maximum size. All assertions passed. Reproduce with `python3 verify_python.py`, `c++ -std=c++17 -O2 verify_cpp.cpp -o check`, and `./check`.

The proof's noncomputational steps are the cyclic step-two reindexing, forced endpoint analysis for each zero run, the Fibonacci path count, the antitone identity \(F^3=F\), and the Fibonacci inequality establishing the strict basin maximum. All are written in RESULT.md. Exhaustive tests for finitely many sizes are checks, not proofs of the all-size theorem.

No external or independent audit was performed. The historical comparison is qualified because one closely relevant finite-cylinder source was available only in abstract.
