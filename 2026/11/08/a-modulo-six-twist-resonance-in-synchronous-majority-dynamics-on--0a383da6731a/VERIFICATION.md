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

# Reproducibility record

Compile the accompanying `verify_exhaustive.cpp` and `verify_transfer.cpp` using a C++17 compiler with optimization, and run the resulting executables. The exact commands, also shown in `RESULT.md`, are `g++ -O3 -std=c++17 verify_exhaustive.cpp -o verify_exhaustive` and `g++ -O3 -std=c++17 verify_transfer.cpp -o verify_transfer`. Each executable prints the exact counts and ends with an explicit `PASS` marker if every internal equality holds. The files `exhaustive.txt` and `transfer.txt` are the captured complete outputs from these commands.

The first program enumerates all labelled binary configurations of both graphs for every circumference from three through twelve, compares one-step and two-step recurrence and complete flipping, and prints the primitive two-cycle census. The second program independently counts admissible cyclic space-time words by constructing 4- and 16-column-alphabet transfer operators and applying either identity or layer-swap closure for circumferences three through twenty-two. These are separate computational methods. Neither finite calculation proves recurrence for every length; that conclusion rests on the algebraic and graph-theoretic proof in `RESULT.md`.

No external validation has been performed. The known 1980 general period theorem is not claimed as independently rediscovered; the proof includes a self-contained cubic-degree version.
