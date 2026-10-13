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

# Reproduction

Compile and run `verify.cpp` with `g++ -O2 -std=c++20 verify.cpp -o verify && ./verify`. Separately run `python3 verify.py` (Python standard library only).

Both build the complete relation between all 32 five-bit centers and all 64 six-bit targets, check insertion balls each have 7 distinct targets, and exhaustively rule out every covering of size at most 11. They independently enumerate the six coverings of size 12 and check every received word is covered in each code. Complementing all bits and reversing all five positions partitions the six codes into three two-member orbits.

The C++ search reports `optimal_size=12 labeled_optima=6 complement_reversal_orbits=3 nodes=10955 VERIFY_OK`; the independent Python implementation reports `optimal_size=12 labeled_optima=6 complement_reversal_orbits=3 nodes= 10841 VERIFY_OK`. State counts refer to recursion calls under different exhaustive branching orders; they are **not** a certification channel or probabilistic inference. Every pruning condition is explained and justified in `RESULT.md`.

# Limitations

The verification is finite and exhaustive only for this exact alphabet, center length and insertion radius. No conclusions are made for larger lengths or alphabets. Independent external validation has not been performed.
