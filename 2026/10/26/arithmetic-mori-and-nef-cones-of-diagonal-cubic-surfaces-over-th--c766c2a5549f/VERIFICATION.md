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

Run `python3 verify_diagonal_cubic.py` with `dual_cone_exact.cpp` in the same directory. Requires Python 3, SymPy, C++17. The reproducibility program constructs the line incidence matrix in \(\mathbb F_7\), checks a unimodular geometric Picard basis and all 81 diagonal cube-class coefficient patterns, computes Frobenius orbit sums and their intersections, compiles the integer exact dual-cone enumerator, enumerates every potential dual extremal ray from intersections of \(r-1\) independent supporting hyperplanes, and reproduces all five finite-field point counts. It ends with `VERIFY_OK:`. The exact dual-cone engine visits 296010 sets in the split rank-seven case. The program was executed successfully on the final two source artifacts before packaging.

Finite computations establish exact finite ray numbers because they exhaust the finite active-hyperplane cases and verify the integers exactly; the general reduction from arithmetic nef divisors to these inequalities is given in `RESULT.md`. Finite point enumeration is a cross-check, not an independent proof of the cone theorem. No external or independent audit has been performed.
