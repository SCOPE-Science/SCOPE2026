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
# Reproducible verification

Run `python verify.py` using Python 3 with SymPy and NumPy. The checker recreates each weighted adjacency Hamiltonian directly. It computes an exact rational rank using symmetric-commutant equations, independently checks the rank of the spectral-projector average-mixing matrix, and compares both with the all-size formula.

The exact series comprises 180 triples with \(2\le a,b\le7\) and \(g\in\{0,1/2,1,2,3\}\). The separate floating spectral series comprises 288 triples with \(2\le a,b\le7\) and \(g\in\{0,1/4,1/2,1,3/2,2,3,7\}\), comprising 25,008 matrix entries across profiles. The grouping of repeated eigenvalues is essential because the zero eigenvalue is usually degenerate.

Successful output:

```text
VERIFY_OK exact_commutant_cases=180 spectral_profiles=288 spectral_entries=25008 a_b=2..7
```

The proof supplies the full real-coupling result; these finite checks cannot establish it independently for infinitely many sizes and continuously many couplings. No independent audit has been performed.
