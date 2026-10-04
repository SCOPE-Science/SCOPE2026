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

The claim is an analytic theorem for every \(0<\omega<1\); no finite computation is used to establish an infinite parameter range.

The lower-bound calculation was checked from the published absolute-norm comparison inequality. On \(0\le t\le1/2\), the convex representative is \(\phi(t)=(1-t)+\omega t\). Cauchy--Schwarz gives \(M_1=\sqrt{1+\omega^2}\), with equality at \(t=\omega/(1+\omega)\). For the reciprocal ratio, the substitution \(u=t/(1-t)\) gives \(R(u)=\sqrt{1+u^2}/(1+\omega u)\) and
\[
\frac{d}{du}\log R(u)^2=\frac{2(u-\omega)}{(1+u^2)(1+\omega u)}.
\]
Hence the maximum occurs at \(u=0\) or \(u=1\), giving \(M_2=\max\{1,\sqrt2/(1+\omega)\}\).

For attainment, set \(a=1/(1+\omega^2)\) and \(b=\omega/(1+\omega^2)\). Exact substitution verifies \(N_\omega(a,b)=1\). The pair \((a,b),(b,a)\) has objective \((1+\omega)^2/[2(1+\omega^2)]\), and the pair \((a,b),(a,-b)\) has objective \(1/(1+\omega^2)\). Each is used on the branch where it matches the comparison lower bound. At \(\omega=\sqrt2-1\), the two expressions coincide.

A supplementary numerical stress test over polygonal unit-sphere edges at parameters on both sides of the transition agreed with the exact formulas. That test is not treated as proof.

The literature comparison inspected the 2022 full text for its general bounds, equality criterion, Lorentz example, and conclusion; the 2023 full text for the closest later Lorentz example; and the 2007 abstract for its stated exponent range. The theorem does not claim the unresolved cases \(1<r<2\) or Gao-type exponents other than \(2\).
