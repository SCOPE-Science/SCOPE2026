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

# Reproducibility and verification

The finite-tree model, exact definitions, complete quantifiers, and mathematical proof are in `RESULT.md`. Execute `python3 checker.py` in any standard Python 3 interpreter. No external packages, data sets, or downloaded papers are needed to reproduce the finite checks. `checker_output.txt` contains the output from the packaged checker run.

The checker constructs adjacency vectors by iterating the graph neighbors and uses Gaussian elimination modulo each of the two prime moduli \(1000003\) and \(1000033\). It tests eleven combinations of branching factors and depths, all representative distances, seven additional leaf pair placements, and an excluded binary case. Its modular ranks alone are not exact rational ranks or infinite-depth proofs; correctness for all parameters follows from the analytic eigenvector and spectral-projection argument, not a finite computational sample.

The claim uses a non-Hermitian absorbing Hamiltonian with two strictly positive rates. The asymptotic captured population is the initial bright-projector weight, not the instantaneous trapping probability and not an estimate of its approach speed. The separate spectral dimension proof uses ordinary (not graph-Laplacian) adjacency, and the identified binary counterexample confirms that the branching restriction is substantive. Historical priority and implementation robustness remain unverified by independent assessment.
