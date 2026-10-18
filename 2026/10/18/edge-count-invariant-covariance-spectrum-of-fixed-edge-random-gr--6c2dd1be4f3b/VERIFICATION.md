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
# Reproducible mathematical verification

Run the included standalone `verify.py` using Python 3 with the standard library only. It independently computes degree-histogram covariance matrices by exhaustive labeled-graph enumeration and by a hypergeometric three-region law, then evaluates rational orthogonal-polynomial spectral identities. Checks cover every \(1\le m<\binom n2\) for \(n=4,5,6\). Expected final output: `VERIFY_OK 56 independent graph-enumeration and hypergeometric-pair cases`.

Finite checks establish no all-size theorem by themselves. The all-size argument is the conditional factorial-moment and self-adjoint polynomial-regression proof in `RESULT.md`. No numerical floating-point tolerance, external solver, unrecorded data file, or independent audit is used.
