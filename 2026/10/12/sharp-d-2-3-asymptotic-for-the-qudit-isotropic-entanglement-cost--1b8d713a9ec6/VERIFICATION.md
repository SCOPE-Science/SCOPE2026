---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

PASS: With x=d-1 and u_d=x^(1/3)+x^(-1/3), choose c*=2(u_d-1)^(-2)-1 at Fang's cubic-norm branch boundary and p*=(1-(u_d-1)^(-2))/eta_d, eta_d=1-d^-2. Then 1-p*=[(u_d-1)^(-2)-d^-2]/eta_d~d^-2/3, while 1-p_L~4/d, so for sufficiently large d, p*<p_L and the explicit affine entanglement-of-formation branch applies. Fang's Proposition 12 affine cubic-norm branch yields B_d(c*)=log_2 d-s_d eta_d p*, s_d=3log_2 u_d, hence exact witness difference p*(s_d eta_d-kappa_d), kappa_d=(d²-1)/(d(d-2)) log_2(d-1). Elementary rewriting gives 3eta_d log_2(1+x^(-2/3))-2x(x+2)log_2 x/[(x+1)^2(x-1)]; the first term is 3 x^(-2/3)/ln2+o(x^-2/3), second O(log x/x)=o(x^-2/3). Thus liminf d^(2/3)G_d>=3/ln2, matching Fang's independently inspected Corollary 13 limsup. Independent numerical reconstruction verifies p* in affine region, positive witness below published bound, and convergence at d=10^3,...,10^8. No finite experiment is used to prove the limiting equality.

## originality

PASS

Fang first defines this exact maximum interval-width G_d and proves only the upper bound limsup d^(2/3) G_d <=3/ln2. The reviewed result selects Fang's own nonlinear-to-affine transition c_{*,d} as a witness and proves a matching lower bound, converting a one-sided bound into a sharp leading asymptotic. Terhal–Vollbrecht predates the cubic-norm lower certificate and cannot itself imply its comparison gap. The assertion is explicitly about certificate uncertainty, not true entanglement-cost regularization.

## value

PASS

Fang's general O(d^-2/3) certificate-width upper bound leaves open whether the exponent/constant reflect true uncertainty or loose analysis. The new witness at a canonical bound-branch transition proves both are sharp, giving a meaningful exact leading asymptotic for a natural maximum over noise and ruling out improvement of the certificate-gap bound without changing one of its components. Its value is mathematical sharpness of rigorous bounds, not a claim to solve entanglement cost itself.

The dated certificate retains the supplied scientific assessment, sources and limitations.
