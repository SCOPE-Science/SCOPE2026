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
Run `python3 verify.py` from the extracted package. The script uses only Python's standard library and compares a directly orthogonalized projected-resolvent computation with the spectral-interpolation formula. It verifies exact rational moments for a three-rate sample, an exact sign inequality, and the explicit positive stiff-limit value; it also checks 1,400 fixed-seed multi-dimensional parameter choices and ordinary-Lanczos comparison asymptotics. Package replay completed with 65,143 checks.

The proof of the universal threshold, strict maximal-eigenvalue first crossing, and \(L\to\infty\) asymptotics is in `RESULT.md`. No finite set of tests proves these universal statements. The algorithm tested is the inverse of the compressed shifted resolvent, **not** the compression of the original generator. Other shift-invert approximants may behave differently. Independent audit has not been performed.
