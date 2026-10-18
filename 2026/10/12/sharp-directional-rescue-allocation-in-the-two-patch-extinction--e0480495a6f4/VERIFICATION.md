---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

For CTMC states 11,10,01 and absorbing 00 with extinction a,b>0, rescue directions x,y≥0 and x+y=C>0, exact first-step equations (a+b)t11=1+b t10+a t01, (a+x)t10=1+x t11, (b+y)t01=1+y t11 give common denominator D=ab(a+b+x+y) and rational numerators specified in source. Weighting independent initial probabilities w11,w10,w01 and substituting y=C-x gives T(x)=[K+(C+a w10-b w01)x-x²]/[ab(a+b+C)]. This is globally strictly concave, so x*=clip_[0,C]((C+a w10-b w01)/2) uniquely. Exact comparison (x-z)²-(x*-z)² proves globality including boundary; initial all-11 yields symmetric C/2 regardless of a,b. Independently reconstructed 3×3 linear system and symbolic numerator and curvature.

## originality

PASS

Directional connection simulations in Vuilleumier–Possingham 2006 concern large metapopulations and finite-horizon persistence, not this two-patch CTMC with exact fixed directed colonization sum and arbitrary initial occupancy. Ross–Pollett budget management splits scalar colonization and extinction rates, not opposing directed flows x/y at fixed x+y. Etienne–Heesterbeek winking-patch rules use a different stochastic model/criterion. Only accessible abstracts for some relevant sources, so fully unreviewed papers remain a bibliographic risk, not reason to reject a correctly derived specific optimizer.

## value

PASS

With management resources allocated between opposite directed rescue flows, which direction to favor is a motivated metapopulation decision. The exact universal optimizer, saturation thresholds and counterintuitive fact that fully occupied starts favor equal directions even under unequal local extinction supply concrete structural insight absent from general scalar-investment heuristics. The result is model-specific and not a field-prediction claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
