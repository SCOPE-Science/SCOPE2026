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

The theorem is analytic. The accompanying checker uses exact rational
arithmetic for the finite identities.

For centered discrete uniforms \(U_m\), it verifies
\[
v_m=\frac{m(m+1)}3
\]
and
\[
q_m=\frac{m(m+1)(3m^2+3m-1)}{15}
=
\frac{9v_m^2-v_m}{5}.
\]

For each tested variance cell \([v_m,v_{m+1}]\), the checker confirms that the
secant through the adjacent moment points lies below every tested grid moment
point outside the cell. It constructs the exact adjacent-uniform mixture at
many rational phases and verifies both the prescribed variance and equality
in the fourth-moment bound.

Random rational mixtures of several centered discrete uniforms are also
tested against the claimed lower envelope.

The asymptotic phase formula is replayed from the exact identity
\[
v\left(\kappa_{\min}(v)-\frac95\right)
=
-\frac15+
\frac9{5v}\theta(1-\theta)(v_{m+1}-v_m)^2.
\]

Finite replay does not replace the universal convex-hull proof.

Independent audit has not been performed.

Exact-rational replay result: `VERIFY_OK moment_checks=1503 chord_checks=80000 equality_checks=5250 random_mix_checks=20000 phase_checks=5269`.
