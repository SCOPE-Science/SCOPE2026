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

The proof is analytic. The accompanying checker uses exact rational
arithmetic for finitely supported spectral measures.

For thousands of random rational probability measures on rational spectral
points in \([-1,1]\), it forms the weighted squared pushforward \(G\), recovers
the sign-splitting parameter, reconstructs the original spectral measure, and
checks normalization together with paired moments through lag twenty.

It verifies the compatibility inequality
\[
\int\frac{G(dx)}{1+\sqrt{x}}\le1
\]
whenever the square roots are rational in the generated test family.

The checker separately verifies the explicit measures
\[
\nu_A=
\frac13\delta_{1/2}
+\frac1{12}\delta_{1/3}
+\frac7{12}\delta_{-1/3}
\]
and
\[
\nu_B=
\frac3{16}\delta_{1/2}
+\frac7{16}\delta_{-1/2}
+\frac38\delta_{1/3}.
\]
It confirms identical paired moments, different second and third
autocorrelations, common normalized asymptotic variance \(35/24\), and the
two distinct three-step sample-mean variances.

Finally it checks the two-state eigenfunction identity for every rational
spectral point used in the finite-state constructions.

Finite replay does not replace the measure-theoretic inversion proof.

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK fiber_reconstruction_checks=12002 paired_moment_checks=264080 compatibility_checks=12002 two_state_eigen_checks=42015 explicit_alias_pair=passed`.
