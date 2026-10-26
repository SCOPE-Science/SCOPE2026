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

The mathematical certificate `certificates/path_radau_coefficients.json` records every exact common-denominator polynomial for the upper triangle of the Radau heat matrix for path orders two through six. The verifier `verify.py` recomputes the full certificate from the definitions of the Laplacians and Radau rational function using symbolic exact arithmetic, checks every coefficient and row sum, verifies the exceptional endpoint formula and the fifth-order Taylor term, and confirms an exact weighted-path example.

Executed from the same directory as the enclosed files with SymPy 1.14.0:

`python verify.py`

Result:

`VERIFY_OK 55 independent path entries, exact denominators, unique P6 root, Radau coefficient, root-isolation and weighted-path checks`

The arbitrary-graph statement follows from a proof by graph distance and spectral convergence, not finite enumeration. The rational interval for the six-path root is exact, and the displayed decimal is an approximation. Stagewise positivity and arbitrary-graph intermediate-timestep classification are not asserted.
