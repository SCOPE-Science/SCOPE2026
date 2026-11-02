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

# Reproducible finite verification

Place `certificates.json`, `verify.py`, and `verify_independent.cpp` together. Run `python3 verify.py` using Python 3.9 or later. It recomputes all candidate vertices, overlap and Hamming constraints, a rigorous coloring-bounded exact clique search, and verifies 55 explicit witnesses, printing `VERIFY_OK 55 exact finite parameter pairs` on success.

Independently compile the C++17 implementation with `c++ -O3 -std=c++17 verify_independent.cpp -o check` and run `./check`. Its 55 CSV rows of `n,d,size` were compared with the supplied certificate; the complete comparison returned `CROSSCHECK_OK 55`.

The search is exhaustive only over binary code lengths 2 through 11 and distances 2 through the code length. Computational repetition supports the finite claims, not an all-length theorem or independent external validation.
