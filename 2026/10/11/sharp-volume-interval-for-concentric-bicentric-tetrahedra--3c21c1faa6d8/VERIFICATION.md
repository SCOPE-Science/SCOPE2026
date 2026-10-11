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

The theorem is proved for every real \(R/\rho\ge3\) in `RESULT.md`; finite computation is only corroborative.

The bundled `verify.py` performs two independent consistency checks using only the Python standard library. First, it enumerates positive rational triples \((a,b,c)\) with \(a+b+c=1\) on several denominator grids, reconstructs \(Q=1/a+1/b+1/c\), computes the corresponding squared tetrahedral volume, and checks that it lies between the two claimed radical bounds. Second, for integer \(Q\) values it checks the double-root endpoint parameterization against the radical product endpoints and rechecks the volume conversion.

Expected replay output:

`VERIFY_OK concentric-bicentric-tetrahedra triples=3640 endpoint_cases=192`

These checks do not establish literature noncoverage and do not replace the discriminant proof.
