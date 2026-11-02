---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

Adjacent forbidden inequalities cannot co-occur when 2ell<=a; weighted inclusion-exclusion is indexed by matchings of cyclic C_s. The isolated-variable exponential integral b(t)=(e^{at}-1)/t and forbidden-edge integral d(t)=e^{at}(cosh(ell*t)-1)/t^2 give Z_s(t)=lambda_+(t)^s+lambda_-(t)^s, where lambda± are roots of lambda²-b lambda+d. The discriminant is strictly positive because d/b²<=ell²/(2a²)<=1/8. Centering by e^{-ast/2} makes the roots even, proving mean sa/2. Second derivatives yield Var(S_s)=s[a²/12+epsilon*(1-rho^{s-1})/(1+rho^s)]; rho in (0,1) makes inflation and dimension monotonicity strict. Analytic dominant eigenvalue gives CLT and differentiable scaled log MGF gives the stated full compact-support LDP. Independent exact-rational matching and centered-moment enumeration for a=1,ell=1/2, s=3..12 matched the formula. The infinite claims rest on the transfer identity, not those finite checks.

## originality

PASS

The original 2022 full primary article by Kantarcı Oğuz, Özel, Ravichandran defines the same chainlink polytope and in Proposition 6.8 gives its unweighted volume as a cycle-matching trace; it also proves complementary fixed-sum section-volume and Ehrhart symmetry. Its sections 1, 6 and 7, reviewed in full accessible HTML, do not present the nonzero exponential tilt, exact finite coordinate-sum variance, strict variance inflation/monotonicity, Gaussian limit, or Legendre rate function.

## value

PASS

The coordinate sum is the canonical linear functional defining complementary chainlink sections. Determining its full finite-volume distribution transform, strict variance amplification relative to the cube, concentration scale, Gaussian fluctuations and LDP provides substantive continuous geometric invariants of a natural enumerative-combinatorial polytope family.

The dated certificate retains the supplied scientific assessment, sources and limitations.
