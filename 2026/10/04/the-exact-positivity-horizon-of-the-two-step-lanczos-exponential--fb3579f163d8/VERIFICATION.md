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
The packaged checker uses exact rational arithmetic and no external dependencies.

For the witness with eigenvalues
\[
1,2,4
\]
and squared starting-vector entries
\[
5,15,1,
\]
it reconstructs the normalized spectral moments and the two-step Lanczos coefficients. It verifies that the resulting \(2\times2\) Ritz matrix has characteristic polynomial
\[
z^2-\frac92z+\frac92
\]
and therefore Ritz values \(3/2\) and \(3\).

For
\[
t_0=\frac23\log4,
\]
the two Ritz-exponential values are exactly \(1/4\) and \(1/16\). The checker reconstructs the affine interpolation polynomial
\[
q_{t_0}(\lambda)=\frac{7-2\lambda}{16}
\]
and verifies the positive, positive, negative coordinate multipliers
\[
5/16,\quad 3/16,\quad -1/16.
\]

The checker also verifies the strict ordering of the witness time beyond the theoretical horizon through the equivalent exact comparison
\[
4>\frac52.
\]

The general finite-horizon classification, the strict Ritz bounds, and minimal-dimension statement are analytic arguments in RESULT.md and are not inferred from finite experimentation.
