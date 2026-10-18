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

Use Python 3 with its standard library and run `python check.py` from a directory containing the included standalone checker. Its successful output terminates in `VERIFY_OK`; all tests are exact rational linear algebra, finite-set combinatorics, and integral-vector identities, with no floating-point tolerance or external downloads.

For \(n=4,5,6,7\), the checker enumerates all disjoint nonempty ordered index-set pairs, evaluates the rank of the corresponding root incidence vectors, verifies nonsimplicial-cone criteria and the covering property of square faces, counts minimal singular squares, checks star-fan maximal-cone extensions, and checks the primitive four-ray parallelogram relation. It outputs minimal-square counts \(6,30,90,210\), star maximal-cone counts \(1,2,4,8\), and combined anticanonical degrees \(6,30,180,1260\).

This exhaustive bounded enumeration verifies neither arbitrary \(n\) nor any unpublished literature novelty. The all-\(n\) proof uses explicit face classifications, saturated lattice bases, a dual-semigroup calculation, and the polar-cube description in RESULT.md. The local equation describes the completed transverse generic orbit singularity only. The nilpotent structure of the Jacobian singular scheme and completed germs at intersections of singular components are not calculated.
