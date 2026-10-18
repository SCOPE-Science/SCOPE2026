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
# Verification and reproducibility

Use Python 3 with NumPy and SymPy. Execute `python reproduce.py`. A recorded independent execution of the included program returned:

`PASS 231 symbolic family and Krylov checks; 1320 random-frame bound checks`

The program checks exact orthonormality, explicit submatrix spectra and the Krylov construction for each integer dimension from 5 through 15, with symbolic radicals. It independently tests the analytic leverage bound on 1,320 random orthonormal frames. These are finite checks. The general assertion, equivalence at uniform leverage and unbounded family are established by the exact proof in RESULT.md, not by the observed finite checks. The published dimension-dependent worst-case separation is credited and not considered new; the newly reviewed claim is its leverage-sensitive complement.

No full technical comparison was possible with the 2022 related sensor-design conference article. No solver runtime, floating-point accuracy, or end-to-end Krylov convergence claim was experimentally tested or proved.
