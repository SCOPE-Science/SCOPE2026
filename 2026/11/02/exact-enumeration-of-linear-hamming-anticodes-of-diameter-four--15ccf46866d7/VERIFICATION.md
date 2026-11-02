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

The standalone Python 3 program `census_linear_d4.py` was run successfully from the supplied file. The exact output is embedded as `census_linear_d4.stdout`. It enumerates every RREF generator on all support lengths remaining after the proved strict mean-weight cutoff, tests full support, and checks all codewords rather than a sample. It independently compares the total number of RREF matrices with Gaussian-binomial counts and checks the short-support symbolic formula.

The support cutoff and coordinate decomposition are proved in `RESULT.md`. Finite testing alone would not establish a theorem for arbitrary ambient length; those structural arguments supply that step. The length-seven simplex identification is also proved by an independent moment calculation. The script is an exhaustive finite combinatorial certificate, not an external theorem prover, and no independent mathematical audit has been performed. Its conclusions are restricted to the explicit finite supports; the general field and ambient-length assertions use the separate mathematical arguments.
