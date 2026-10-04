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

`verify_schur_spectrum.py` uses only Python's standard library. It represents \(\mathbf Q(i,\sqrt3)\) exactly on the basis \(1,i,\sqrt3,i\sqrt3\), reconstructs the 16 first-type and 48 second-type Schur lines from the published Bauer--Schmitz formulas, and tests all \(2016\) unordered line pairs by exact determinant.

The resulting graph has 64 vertices, 576 edges, degree 18 at every vertex, and diameter two. Exact squaring gives the complete common-neighbor census. For the spectrum, exact integer matrix multiplication verifies
\[
(A-18I)(A-2I)(A+4I)(A+6I)(A+10I)=0,
\]
and computes
\[
(\operatorname{tr}(A^0),\ldots,\operatorname{tr}(A^4))=(64,0,1152,1728,139392).
\]
Because \(A\) is symmetric and the five roots of the annihilator are distinct, these traces uniquely determine multiplicities \((1,44,8,9,2)\). No floating-point spectral calculation is used.

The companion `verification_output.txt` records the deterministic run and terminates with `VERIFY_OK`.

Limits: the verifier certifies the exact finite Schur-line configuration described in the cited parametrization. It does not search the literature and does not classify automorphism orbits of line pairs.
