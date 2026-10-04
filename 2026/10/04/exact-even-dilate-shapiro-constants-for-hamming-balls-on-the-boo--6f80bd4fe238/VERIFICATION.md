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

The proof was replayed from the finite Walsh transform with the convention
\[
\widehat f(\xi)=\sum_x f(x)(-1)^{\xi\cdot x}.
\]
For an even-radius Hamming ball \(B\), the critical combinatorial step is that every nonzero character has at least \(O\) negative-sign points in \(B\), where \(O\) is the number of odd-weight points of \(B\). This is certified by the explicit parity-toggle injection in `RESULT.md`.

The accompanying `verify.py` checks, in exact integer arithmetic, every character for
\[
1\le d\le10,\qquad 1\le r\le6.
\]
It verifies
\[
\widehat{1_B}(\xi)\le E-O
\]
for every nonzero \(\xi\), the affine majorant
\[
\widehat{1_B}(\xi)\le E+\frac{O}{d}(d-2|\xi|),
\]
the combinatorial inequality \(O\le dE\), and exact attainment by the even-parity subgroup indicator. The executable returns `VERIFY_OK`.

The finite replay is not used to infer the universal theorem. All dimensions and all even dilation parameters are covered by the analytic injection and Fourier argument in `RESULT.md`.
