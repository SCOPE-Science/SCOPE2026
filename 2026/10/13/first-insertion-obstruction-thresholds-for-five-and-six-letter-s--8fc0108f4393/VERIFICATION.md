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

Compile `verify.cpp` with a C++17 compiler and run it. It exhaustively enumerates every canonical square-free word up through each threshold and recomputes all blocked insertion gaps. No third-party code or solver is required. Example: `g++ -O3 -std=c++17 verify.cpp -o verify && ./verify`. Expect `VERIFY_OK first_nonbifurcate_lengths_2_through_6`.

Run `python3 check_witnesses.py` beside `witnesses.json` for an independently implemented direct test of squarefreeness and all insertions for each witness; expect `VERIFY_OK direct_witness_insertions`.

The executable certificate for the lower bounds consists of exhaustive restricted-growth generation and the proved square-completion mask criterion; checking only the explicit witnesses certifies upper bounds but not minimality. The general construction is established mathematically in RESULT.md. No independent audit has been performed, and no assertion for alphabet sizes above six is computationally certified.
