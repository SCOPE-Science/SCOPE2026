---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

Two wild poles of order 3 give genus three by Artin–Schreier Riemann–Hurwitz. The Klein four involutions yield genus-one quotient y²+y=t³+t and genus-two complementary quotient z²+z=t³+t+t^(-1), with rational full quotient, so Kani–Rosen character idempotents split the Jacobian isogeny. The F2, F4, F8 trace counts (N1,N2,N3)=(4,8,4) determine the first three Hasse–Weil coefficients via Newton identities; the genus-three functional equation determines the remaining coefficients, factoring into (1+2T+2T²)(1-2T+2T²)(1+T+2T²). The corresponding elliptic Frobenius traces -2,+2,-1 are valid by explicit elliptic models and Tate. Verified independently via finite-field bit arithmetic and polynomial multiplication; supplemental n=4..6 counts in package are consistency checks, not infinite sampling.

## originality

PASS

Best-of-knowledge exact arithmetic Frobenius decomposition at the canonical first m=3, c=1 characteristic-two wild-boundary model is additional to published genus/geometric action classification. The latest Kazemifard–Tafazolian preprint was accessible at abstract/metadata level only; an equivalent zeta-table or alternate Artin–Schreier form remains a real priority risk.

## value

PASS

For the first genus-three member of a geometrically classified two-wild-pole C6 family, determining all Frobenius factors and ordinary/supersingular composition is a natural arithmetic invariant not implied by genus or geometric cyclic action. The exact rational isogeny type and group order provide a reproducible benchmark for later higher-exponent work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
