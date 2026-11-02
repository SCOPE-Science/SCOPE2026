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

# Verification for the exact binary Lie generating-partner census

The mathematical universe has 256 trace-zero matrices over \(\mathbb F_2\), hence exactly 65,536 ordered pairs. `checks/full_census.cpp` explicitly generates the matrices as nine-bit words, constructs the bracket from binary matrix products, determines every bracket closure, and reports the complete subalgebra-dimension histogram and conjugacy classes. `checks/full_census.py` separately uses an eight-element traceless basis and bilinear structure constants to test all 65,536 ordered pairs. `checks/orbit_census.py` independently enumerates all 168 invertible matrices, checks seven disjoint similarity orbits covering all 256 elements, and checks all 256 partners for each class representative.

The actual replay output files are embedded in `checks/`. All three programs printed `VERIFY_OK`. The class sizes add to 256. The seven products of orbit sizes by conditional partner counts add to 13,440. The dimension histogram sums to 65,536 and has nonzero entries only at dimensions zero through five and eight. No probabilistic sampling or floating-point calculation occurs.

To reproduce, run `python3 checks/full_census.py`, `python3 checks/orbit_census.py`, and compile/run `checks/full_census.cpp` with GNU C++17. Compare stdout bytewise with `checks/full_census_py.out`, `checks/orbit_census.out`, and `checks/full_census_cpp.out`. The C++ checker also writes an informational group-size line to stderr. These tests apply only to the finite binary rank-three algebra; no assertion about arbitrary ranks or coefficient fields is verified.
