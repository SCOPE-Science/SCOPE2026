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

# Finite checks and limits

Run the Python 3 program `check_python.py` without nonstandard packages and compare its single JSON line with `certificate.json`. Its loops visit every subset of the two specified Paley graphs, implement secure-total and double domination using independent direct predicates, list all size-five optima, build their token-jump and token-slide graphs, compute every connected component and every source's within-component shortest-path histogram, and enumerate affine orbits. The exact complete certificate is included.

Compile `check_cpp.cpp` with `c++ -O2 -std=c++17 check_cpp.cpp -o check_cpp` and run the executable. Compare standard output with `checked_cpp.txt`. This second implementation reconstructs graph neighborhoods from modular quadratic-residue tests, enumerates all subset masks, checks total and secure replacement conditions and double domination, and independently computes exchange graph component sizes and eccentricities. Both implementations obtain zero disagreements between the two domination predicates and exact matching polynomials.

Recomputation establishes the finite statements only; it neither constitutes an infinite-order theorem nor an independent scientific audit. Published priority cannot be proved by a finite computation. The 2008 foundational paper full PDF was not available for complete inspection, so overlap risk persists.
