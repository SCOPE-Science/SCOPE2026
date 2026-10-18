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

# Reproducibility and scope

The complete, standalone `verify.cpp` reconstructs the cycle and its private leaves, assigns all four two-color subsets to each vertex, and directly checks the independence of empty vertices and the full two-color union at every empty vertex. It exhaustively enumerates all assignments for orders 3 through 6, comprising 17,895,424 individual assignments. There is no assumption of the transfer-matrix theorem inside its feasibility predicate.

The program separately computes exact integer 3-by-3 matrix powers and checks agreement with the two-state characteristic recurrence up to order 51. Compile using `g++ -std=c++17 -O3 verify.cpp -o verify` and run `./verify`. The captured successful output is in `verify_output.txt`.

The independent exhaustive check is finite and does not establish the infinite-family theorem by itself. The general proof follows from the pair-weight inequality, the equality-case classification, maximum independent sets of cycles, and the transfer enumeration. No external independent audit has been performed.
