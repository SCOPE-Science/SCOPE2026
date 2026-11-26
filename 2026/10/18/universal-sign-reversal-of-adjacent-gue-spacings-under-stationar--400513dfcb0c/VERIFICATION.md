---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Integrating out the center from the explicit ordered GUE density gives the gap weight a^2 b^2 (a+b)^2 exp(-(a^2+ab+b^2)/3). For independent evaluation of the decisive moments, put (a+b)/2=rho cos(theta), (a-b)/2=sqrt(3) rho sin(theta), with |theta|<pi/6. The gap weight with Jacobian becomes 8sqrt(3) rho^7 exp(-rho^2) cos^2(3theta). In the angular integral an extra a contributes rho cos(theta), its odd part vanishing; an extra ab contributes rho^2(2cos(2theta)-1). The three angular integrals are pi/6, 18/35, and 9sqrt(3)/16-pi/6. Gamma integration gives I00=4pi sqrt(3), I10=(27/2)sqrt(3pi), I11=162-16pi sqrt(3), yielding the stated m and h. Conditional on the independent equilibrium age, the gaps scale by sqrt(A); the containing interval has length-biased law and the observation is uniform within it, including for deterministic or lattice durations. Thus EA=EW^2/(2EW), E sqrt(A)=2EW^(3/2)/(3EW), where the powers inside E are powers of W. The covariance identity follows by integrating the conditional moments. Cauchy–Schwarz gives the sharp 8/9 bound on (E sqrt(A))^2/EA, with equality exactly for constant W since W>0. The frozen rational sign bounds verify h-m^2<0<h-(8/9)m^2. For exponential intervals the age is exponential, hence the ratio is pi/4 and 4+729/256=1753/256 in the Poisson coefficient.

## originality

PASS

Support is for the specific finite 3-by-3 GUE sign reversal for all stationary renewal clocks in scope, including its sharp lower coefficient and equality case, not for the finite-N GUE density, age mixture, or Cauchy–Schwarz optimization in isolation. The Poisson and fixed-age moments are derivable from known laws and do not independently carry the originality verdict. The closest verified material overlaps supply these ingredients or a sharp normalized gap correlation for a different ensemble and limit; none supplies the stated GUE renewal sign and sharp coefficient.

## value

PASS

This resolves a natural competition: a common random age induces positive co-movement but at fixed age the two GUE gaps are anticorrelated. The proof shows that under every stationary renewal clock of finite second moment, age variability outweighs the negative term, and identifies the extremal clock and exact positive minimum per unit mean age. The conclusion involves an entire class of protocols and is more informative than a finite moment table or a single Poisson example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
