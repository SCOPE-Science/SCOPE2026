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
# Verification

The homotopy theorem for every integer \(n\geq3\) is proved by the tetrahedral face decomposition and dominated-vertex collapses, not by extrapolating finite results. The integral module follows from the canonical Mayer–Vietoris connecting map and an explicit simplicial contiguity argument.

Run `python3 verify.py` with the standard Python library. The script enumerates all vertex subsets of crown graphs for parameter values \(n=3,4,5,6\); for each subset it compares an induced-degree test to an independently coded tetrahedron-cover test, then checks the face-vector formula and mod-two boundary ranks. For all \(2n!\) graph automorphisms in each tested case, it compares the exact signed simplicial Lefschetz number to the integral exterior-square-and-swap character formula. The runs checked respectively 12, 48, 240 and 1,440 group elements.

The recorded output is in `verification_output.txt` and ends in `ALL_CHECKS_PASS`. The finite computations test the proof's premises and character formula, but cannot by themselves prove the infinite-family assertion, exclude publication priority overlap, or certify independent validation.
