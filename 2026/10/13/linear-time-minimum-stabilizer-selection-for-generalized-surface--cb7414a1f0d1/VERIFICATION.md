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

The proof was checked at the level of definitions, quantifiers, and boundary cases.

For the vertex sector, the restricted row relation on an erased edge \(uv\) is \(y_u+y_v=0\), with \(y=0\) imposed at omitted/open vertex rows. Therefore exactly one dependency survives on each connected erased-edge component containing no omitted vertex, and no dependency survives on a component touching one. This yields \(\ell_Z=|V_I^\circ|-c_Z(I)\).

For the face sector, a two-face erased edge equates two relation coefficients, whereas an erased boundary edge forces its incident face coefficient to zero. Therefore exactly one dependency survives on each face component that has no erased boundary edge, yielding \(\ell_X=|F_I|-c_X(I)\).

The basis construction was checked directly against these dependency spaces. Omitting one row from each unpinned component removes every and only row dependence; pinned components retain all rows.

The asymptotic complexity uses only the local incidence bound: each erased surface edge has at most two endpoints and at most two incident faces, so the involved primal and dual graphs have size \(O(|I|)\). Standard component search is therefore linear in \(|I|\) once the cellulation incidence lists are available.

The included `artifacts/verify.py` performs exact binary Gaussian elimination on generated finite instances and compares matrix ranks with both component formulas and the constructive selected-row ranks. This is a reproducibility check, not an exhaustive proof of the infinite claim.

Unproved limits: the result does not address arbitrary stabilizer matrices, minimum measured-qubit support, nonlocal joint observables, noisy measurement scheduling, or correctability of the erasure pattern itself.
