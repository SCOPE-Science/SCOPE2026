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

# Mathematical verification record

The exhaustive C++17 program `verify.cpp` was compiled with GNU C++ using `-O3 -DNDEBUG` and independently with Clang. Both executables returned `VERIFY_OK` with the following exact key outputs: \(2^{25}=33{,}554{,}432\) directed loop-allowed labeled graphs, \(291{,}968\) unlabeled graphs, \(199{,}957\) orbit representatives admitting directed cycle covers, exactly one orbit with product \(155\) and exactly one with product \(126\), and no product greater than \(155\). The printed maximizer masks decode to directed cycles of lengths \(5\) and \(2+3\), respectively.

A run with GNU C++ address and undefined-behavior sanitizers completed and returned `VERIFY_OK`. The optional independent `crosscheck.py` used integer Hermite normal forms to compute the diagonal-group lattice index on a deterministic collection of \(305\) graphs; it independently computed graph-permutation stabilizers and the full unlabeled-graph count by Burnside's lemma, returning `CROSSCHECK_OK`.

The C++ verifier is deterministic and uses only integer operations. The proof also requires the stated mathematical reduction from perfect evolution algebras to cycle-covered directed supports and coefficient normalization over \(\mathbb C\). The finite enumeration is exhaustive at five vertices, but it does not imply the higher-dimensional conjecture. Independent mathematical audit remains unperformed.
