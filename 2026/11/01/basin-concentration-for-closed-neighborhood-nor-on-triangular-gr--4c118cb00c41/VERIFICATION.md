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

# Reproducible checks

Run `python3 verify_closed_nor.py` using the Python standard library to exhaustively enumerate all states for \(n=4,5,6\). This uses the literal closed neighborhoods of the triangular graph, separately from the base-support formula in the proof. The program checks the cycle relation, absence of fixed points, exact orbit classification, the sharp first-entry-time census, and every basin size. Its output is included in `closed_nor_python_output.txt`.

Compile the separate C++ checker with `g++ -std=c++17 -O2 verify_closed_nor.cpp -o check` and run `./check`. This program uses an explicit edge-support map to generate successor states, exhaustively enumerates every state for \(n=4,5,6,7\), and matches the exact formulas against every observed cycle basin. Its output is included in `closed_nor_cpp_output.txt`.

The two checkers used different update implementations and reproduced the formulas. For \(n=7\), the C++ program enumerated all \(2^{21}=2,097,152\) initial configurations. The algebraic and combinatorial proof, not the checked instances, establishes the unrestricted \(n\ge4\) result. No external validation was performed.
