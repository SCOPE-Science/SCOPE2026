---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

The real smooth ell_3^2 Birkhoff criterion x1|x1|y1+x2|x2|y2=0 reduces all unit orthogonal pairs, modulo signed-coordinate isometries and tangent orientation, to x=(t,1)/(1+t^3)^(1/3), y=±(1,-t²)/(1+t⁶)^(1/3), t>=1, together with axis pairs of value 1. After signed scaled lambda s the cubed ratio is F(t,s)=[1+t³+|s|³(1+t⁶)]/[|t+s|³+|1-s t²|³]. Independent exact expansion verifies all three eliminated sign-region denominators-minus-numerator: for 0<=s<=t^-2, s²t[3(t³+1)-2s t^5]>0; for -t<=s<=0, v=-s, v²(3t^4+3t-2v)>0; for s<=-t, v=-s, t[3v²(t³-1)+6tv-2t²]>0. On s>=t^-2, u=t³>=1, h=s t²>=1 gives exact R(u,h)=[u²(1+u)+h³(1+u²)]/[(u+h)³+u²(h-1)³]. Both finite boundary values are <1 and the explicit difference D-N=-u[3h²(u-1)-6hu+2u] proves R->1 on every unbounded path, by cases h bounded, u>=h³, and u<h³ with h->infinity. R(16,5)=36477/25645>1, so an interior maximizer exists. Independently derived both derivative numerator polynomials and exact resultant factor 4u^13(u+1)^4 Q(u)P(u), with Q>0; exact Sturm root count gives exactly one u>=1 root of degree-ten P, isolated (16.1428,16.1429). Independently checked the linear subresultant 4A(u)h-B(u) modulo P, rational interval positivity A>0,B-16A>0,20A-B>0 and derivative divisibility after h=B/(4A). The unique admissible stationary point is the global maximum, rho=1.4225104283683517897..., mu3=rho^(1/3)=1.124652845212756113... . Finite numerical checks were not used for the universal result.

## originality

PASS

Best-of-knowledge after substantial implication-level search and reading, the exact cubic planar generalized rectangular constant and isolated unique orbit were not covered by inspected prior mathematics. The 2021 primary paper defines precisely mu_p and proves only broad estimates; Theorem 5.6 gives mu_3(ell_3)<=3^(1/3), a nonsharp upper bound. The strongest published exact same-invariant neighbor covers p=4, and the same-space classical mu_1(ell_3^2), T_perp and isosceles findings use different functionals; the L4 generalized mu2 theorem has different exponent and a quartic moment envelope. No reported table or stronger arbitrary-exponent classification covers the degree-ten cubic target. Resultary exact match is the assigned work itself and is not treated as independent priority evidence. The 1970 initiating paper remained inaccessible after appropriate routes, so residual historical risk is recorded, not treated as automatic originality failure.

## value

PASS

The Gastinel–Joly generalized rectangular constant is a standard, geometrically motivated invariant of Birkhoff–James orthogonality. The real cubic Banach plane is the first non-Hilbert smooth odd-integer exponent and a natural exact benchmark, not an arbitrary parameter slice. The full cubic exact value is not implied by published p=3 classical mu1, p=4 generalized mu4, nor the nonsharp general estimates. Its extremizer is genuinely interior and unique modulo natural sign/permutation normalizations, requiring a substantive semialgebraic global certificate (factorized resultant, Sturm count, subresultant, escape control). A future geometric-constant researcher could use this exact planar value and tangent orbit for quantitative comparisons and benchmarks, despite its narrow two-dimensional scope. A paper-sized general theorem is not required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
