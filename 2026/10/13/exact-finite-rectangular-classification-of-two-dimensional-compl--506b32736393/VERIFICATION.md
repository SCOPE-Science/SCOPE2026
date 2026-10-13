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

# Exact computations and limitations

Compile and execute the embedded `verify.cpp` using `c++ -std=c++17 -O2 verify.cpp -o verify && ./verify 5`. The check is exhaustive for each of the fifteen integer-coordinate rectangles \(1\le a\le b\le5\). It prints each lowest feasible cardinality and terminates with `VERIFY_OK rectangles=15 max_span=5 M2(6,6)=15` only when these all equal the asserted entries. The enumeration stores every difference class in a 64-bit mask, has no randomized search and uses safe pair-count pruning proved in RESULT.md. Use `python3 check_witnesses.py` to replay the independent complete coverage check of all fifteen witnesses stored in `witnesses.json`.

The correctness argument depends on the stated reduction and exhaustive execution of the included program. Numeric leaf counts shown by the program exclude branches eliminated by the proved pruning rule. The verifier does not certify all optimal configurations or values for larger grids; no external or independent audit has occurred. Full publisher text for at least one related planar-coarray engineering paper was unavailable, and literature priority risk remains.
