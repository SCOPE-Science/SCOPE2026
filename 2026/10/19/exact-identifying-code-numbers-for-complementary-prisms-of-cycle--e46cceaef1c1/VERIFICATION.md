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

## Local verification
Compile `finite_lower.cpp` and `upper_and_direct.cpp` using a C++17 compiler with optimization enabled and run both executables. `lower_output.txt` and `direct_output.txt` record the results of the included source files. The two source files do not depend on data omitted from the package.

The lower-bound program explicitly builds 256 four-column states, 857 legal transitions, and their 4608-state, 14706-edge length-residue/defect lift. It computes an integer feasible potential for every reduced-cost edge and checks all potential inequalities, then performs nonnegative reduced-cost shortest-path calculations to establish nine exact lower-bound offsets for *all* cycle lengths. Shortest paths use exact integer arithmetic and are not truncated at a chosen graph length.

The second program checks all nine seed pairs by direct closed-neighborhood calculations and tests every specified period-nine concatenation through cycle length 89. It additionally enumerates every vertex subset for cycles of lengths nine and ten, independently establishing minima seven and eight with 90 and 425 optimal codes, respectively. These finite direct checks corroborate but are not substituted for the all-length lower proof.

## Unverified aspects
Independent external scientific audit and external originality certification have not been performed. The claim is limited to the stated complementary prisms and closed-neighborhood identifying codes.
