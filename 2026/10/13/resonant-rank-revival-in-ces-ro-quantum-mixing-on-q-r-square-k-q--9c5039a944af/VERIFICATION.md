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

Run `python3 verify.py` in the directory containing this document. The verifier uses only the Python standard library and needs no external data. Its expected terminal confirmation is:

`VERIFY_OK Fourier_sectors=616 exact_projector_cases=5 first_resonant_rank=29/48 threshold_q6_r3=True`

The code checks \(616\) exact trigonometric-sector coefficients with rational arithmetic over \(1\le r\le8\), \(q\in\{3,4,5,6,8,10,14\}\), including positivity, total nonzero multiplicity and the closed rank law. It constructs the *actual* spectral projectors of five Cartesian graph Hamiltonians: \((r,q)=(1,3),(2,4),(2,6),(3,6),(4,6)\). Equal adjacency energies are merged before the Schur-square sum. Direct row-stochastic and symmetry tests and a rational Gaussian elimination recover the claimed ranks without relying on the Fourier eigenvalue-rank derivation.

The zero-frequency calculation, not a finite numerical table, proves the statement for every \(r\ge1\), \(q\ge3\). Computational cases do not establish novelty and no independent review has been performed.
