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
The accompanying exact symbolic checker reconstructs a Sylvester cubic surface and its Hessian quartic over \(\mathbb Q\). It verifies the Hessian determinant identity, smoothness of the cubic surface in all four projective charts, the ten explicit ordinary Hessian nodes, and the Hilbert functions of the quartic gradient quotient and the reduced ten-point node scheme.

The replayed values are
\[
H_{R/K}=(1,4,10,16,19,16,10,10,10),
\]
and
\[
H_{R/I}=(1,4,10,10,10,10,10,10,10),
\]
so the saturation defect is supported in degrees \(3,4,5\) with dimensions \((6,9,6)\) and length \(21\). A separate dehomogenizing linear form avoids all ten nodes and gives an exact quotient of length \(10\), checking that no additional projective gradient point is present in the witness.

Run `python artifacts/verify.py` with Python 3 and SymPy 1.14 or a compatible recent release. Expected first line: `VERIFY_OK`.

The finite computation certifies the witness. Passage to a nonempty Zariski-open family uses the proof’s algebraic maximal-rank argument; the script does not enumerate the whole parameter space. Special cyclic cubics with extra Hessian degeneracies are outside the claim.
