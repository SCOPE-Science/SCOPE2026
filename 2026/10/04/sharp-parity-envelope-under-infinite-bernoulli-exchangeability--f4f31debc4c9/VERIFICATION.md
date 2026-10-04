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

The proof is analytic. The accompanying checker uses high-precision decimal
arithmetic only to replay the formulas.

For odd \(n\), it obtains \(c_n\) by bisection from
\[
c_n^{\,n-1}[n+(n-1)c_n]=1,
\]
checks the tangent-through-\((1,1)\) identity, evaluates the upper and lower
power envelopes on a dense grid in \([-1,1]\), and reconstructs the endpoint
two-atom laws to check their means and \(n\)-th moments.

For even \(n\), it checks the convex lower bound and the constant upper bound
on the same grid.

The script also checks the exact special value
\[
c_3=\frac12
\]
and samples the fair-marginal odd sequence to confirm numerically that the
parity-bias amplitude tends toward \(1/2\).

Finite numerical checks are not used as a proof of the universal envelopes.
The proof in `RESULT.md` establishes them for all allowed \(n\) and \(\mu\).

Independent audit has not been performed.

Exact replay result: `VERIFY_OK odd_envelope_checks=300150 endpoint_atom_checks=187884 even_envelope_checks=300150 root_checks=50 fair_asymptotic_checks=5`.
