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

The proof is analytic. The accompanying checker uses exact rational arithmetic.

For randomly generated rational Poisson-binomial backgrounds it computes the
background pmf by convolution, forms
\[
c_j=\sum_k a_k a_{k+j},
\]
and verifies directly that
\[
2(3c_0-4c_1+c_2)
=
\sum_k(a_k-2a_{k-1}+a_{k-2})^2.
\]

It then compares the autocorrelation formula for collision probability with a
direct convolution of the full Bernoulli sum and checks
\[
Q(r)-Q(r_0)=2D(r-r_0)^2
\]
exactly.

For many rational fixed sums the checker evaluates the projected product
optimizer and verifies that every sampled feasible product has at least as
large a collision probability.

The two-coin regimes are tested with exact inequalities. The irrational
transition
\[
1-\frac1{\sqrt3}
\]
is represented by the equivalent polynomial condition
\[
3(1-u)^2=1,
\]
so no floating-point approximation is used to certify the phase split.

Finite tests support the algebra but are not used to infer the universal
claim.

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK convolution_checks=22415 energy_checks=12000 quadratic_checks=12000 projection_checks=252000 two_coin_phase_checks=401`.
