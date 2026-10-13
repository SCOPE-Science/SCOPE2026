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

# Verification of the folded-hypercube price frontier

The attached standalone script `verify_folded.py` uses only standard Python and `fractions.Fraction`. Running `python3 verify_folded.py` on the actual embedded file yielded:

`VERIFY_OK 32256 exact Walsh component equations; 7500 exact character Rayleigh computations; 600 individually irregular feasible allocations; 12 critical-family spectra`

The script checks dimensions four through six, rational prices and critical allocations, all Walsh eigenvector component identities, rational character Rayleigh bounds, and irregular individually weighted feasible allocations. These **finite** checks are diagnostic and do not prove the arbitrary-dimensional theorem.

The full proof uses the exact Laplacian Rayleigh form, first- and second-degree Walsh characters, a two-parameter sharp relaxation, and pointwise equality conditions from the min–max theorem. Strict and threshold price cases are treated separately. The edge-normalization condition includes each undirected edge exactly once. The computed eigenvalues concern the unnormalized generator \(-L\), and no guarantee is made for normalized discrete-time mixing.

Scientific review of correctness, originality and value has passed at the same-model level. Independent audit and external validation have not been performed.
