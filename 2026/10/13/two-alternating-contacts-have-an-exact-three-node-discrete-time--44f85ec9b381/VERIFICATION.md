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
The two one-step linearized SIS matrices are multiplied directly to obtain the period propagator
\[
P=M_{23}M_{12}.
\]

The embedded `verify_two_contact_temporal_sis.py` checks, with exact rational arithmetic, the factorization
\[
\det(P-I)
=
\left[
(a-1)^2(a+1)-a\lambda^2
\right]
\left[
(a-1)(a+1)^2-a\lambda^2
\right]
\]
over a grid of rational parameters.

It verifies the exact root
\[
\lambda_{\mathrm{temp}}^2
=
\frac{\mu^2(2-\mu)}{1-\mu}
\]
and the strict comparison
\[
\lambda_{\mathrm{temp}}^2
>
2\mu^2
=
\lambda_{\mathrm{agg}}^2
\]
at \(99\) rational recovery probabilities.

It replays the Perron crossing numerically at three representative recovery values and checks the exact
\[
\mu=\frac14
\]
example.

Run:

`python3 verify_two_contact_temporal_sis.py`

The first output line must be:

`VERIFY_OK`

The all-parameter result is established by the symbolic determinant factorization and Perron monotonicity. The finite checks are reproducibility tests, not an extrapolation from a finite grid.
