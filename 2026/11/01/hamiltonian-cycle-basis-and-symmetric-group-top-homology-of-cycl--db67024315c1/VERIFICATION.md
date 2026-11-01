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

# Reproducibility and boundaries

Run `python verify.py` using Python 3.8 or newer; no external packages are needed. The script enumerates top Hamiltonian-path simplices for \(3\le n\le6\), computes every signed incidence in their codimension-one boundary matrix, constructs all oriented Hamiltonian-cycle boundaries, confirms that each is an integral kernel vector supported on a distinct set of facets, and checks that the mod-two rank is \(n!-(n-1)!\). The generator completeness for arbitrary \(n\) follows from the two-coface equations proved in `RESULT.md`; mod-two computations alone do not prove integer assertions.

The checker also enumerates each permutation of the \(n\) original vertices, records its signed trace on the cycle basis, and averages characters for invariants of \(S_n\) and \(A_n\). The parity predictions are independently justified by the induction and Frobenius-reciprocity argument, not by finite extrapolation. The terminal marker is `HAMILTONIAN_TOP_CYCLE_INTEGRAL_AND_SYMMETRY_CHECK_OK`.

The package contains the exact program used for this test and `verification_output.txt` from its execution. No independent audit, integral orbit-space torsion calculation or lower-homology computation is asserted.
