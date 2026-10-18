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

All checks are finite and independently reproducible from the files adjacent to this document.

The `certificate.py --verify` command recomputes and byte-compares three included finite certificates: 38,760 reachable-target masks for all distributions of weight at most six, the 161 minimum solvable distributions, and the 42 local-relocation edges. The recurrence holds because a lossy pebbling move reduces total weight by one.

The compiled `verify_dp.cpp` program independently builds the cyclic Fano incidence graph and recomputes the complete dynamic-program state lattice and the geometric/equivalence classes. `verify_bfs.py` builds the binary-XOR Fano plane and conducts literal breadth-first graph search for every possible initial distribution up to weight six, without relying on the dynamic-program cache. `verify_symmetry.py` verifies all 336 automorphisms and the four orbit sizes. Recorded outputs are supplied as accompanying files. The proof establishes a finite exact claim, not a statement about untested graphs or a general infinite family.

The package provides deterministic self-review only; independent external scientific audit and replication have not been performed.
