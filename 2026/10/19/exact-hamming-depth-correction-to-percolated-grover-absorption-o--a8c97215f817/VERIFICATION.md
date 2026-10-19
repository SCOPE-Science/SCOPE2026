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

# Verification of the exact Hamming-shell absorption law

Run `python verify.py` from this directory, with Python, NumPy and SciPy available. The program computes binomial expressions in exact rational arithmetic and independently solves grounded Laplacian systems on each punctured hypercube for all dimension/depth pairs \(3\le d\le8\) and \(1\le k<d\). It also evolves the *averaged* density matrix for the actual percolated Grover quantum channel on the three-cube with two distinct edge-open probabilities; the projector onto the nonsink space is applied at every time step. The latter tests \(600\) iterations per case.

Observed output: `Independent electrical-network checks: 27 maximum error 5.551115123125783e-16`; `Total independent checks: 31 maximum absolute error 6.827871601444713e-15`; `VERIFY_OK`.

These numerical checks verify implementation consistency for the tested finite cases only. The infinite-time convergence and general dimension statement instead rely on the trapping theorem and analytic Laplacian/Green-function argument in the result.
