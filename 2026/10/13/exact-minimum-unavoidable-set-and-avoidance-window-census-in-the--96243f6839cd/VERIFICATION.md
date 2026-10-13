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

# Reproducibility checks

On a standard Python 3 installation, run `python3 verify_python.py`. On a C++17 compiler, run `g++ -std=c++17 -O2 -o verify_cpp verify_cpp.cpp && ./verify_cpp`. Both independently visit all possible one-per-necklace transversals and independently compute the remaining directed longest paths. The Python checker also loads `optimizers.tsv`, verifies its complete exact contents, and prints `VERIFY_OK` on success. The same results were independently checked by catalogue comparison between a Kahn topological algorithm and a DFS cycle-search algorithm. This is a finite exhaustive computation, not an infinite-length theorem. No third-party programs, network access or specialized solver is required. An independent scientific audit has not yet been performed.
