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

Run `python3 check_C5.py` in a directory containing the supplied standalone checker. It uses the standard library only and checks all 243 averaging-mask assignments modulo all ten dihedral symmetries. For each of the 38 nonoptimal classes, it proves \(qI-A^\mathsf{T}A\) positive definite at the exact rational threshold \(q=1463/1000\) using five positive integer leading principal determinants. The unique candidate orbit has five members and a rational vector with Rayleigh quotient \(17141/11700>q\). Newton trace identities verify the characteristic polynomial of the optimal averaging matrix, and exact rational sign tests isolate the dominant root.

The run completed successfully. The mathematical reduction from nonlinear maximal averaging to a finite maximum of spectral norms, and the Perron argument classifying all equality cases, are given in RESULT.md. The finite certificate is exhaustive only for this five-vertex graph; no longer-cycle or other-exponent assertion is inferred from it. Independent audit has not been performed.
