---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For any a<b with separation Δ, only cost atoms c<Δ participate and left/right turnout masses are sums w V((a+b-c)/2) and w[1-V((a+b+c)/2)], respectively. At positive turnout, moving the left candidate slightly toward the right preserves the finite active-cost set but strictly increases each V term, disproving any active pure equilibrium for strictly increasing V. Zero-turnout profiles are equilibria exactly when each opponent location lies in I_c*=[0,1]∩[1-c*,c*], else an endpoint deviation generates positive votes. Thus PNE=I_c*², with correct c*<1/2, =1/2, >1/2, >=1 boundaries. The empirical uniform m-grid costs have Kolmogorov error 1/(m+1), whence candidate payoffs differ uniformly by at most that amount. Integrating the limiting uniform game confirms quartile best responses, and the two-sided perturbation bound yields 2/(m+1)-equilibria. Independent exact checks reproduced cdf discrepancies for m=2,3,5,10,100; infinite distribution argument rests on the proof.

## originality

PASS

PASS qualified: Wolf–Meir (September 2026) is the directly relevant participation model and establishes polarized equilibria for density-based costs; the exact finite-atom all-voter-CDF Nash classification and discontinuity of exact equilibrium under uniform payoff approximation are not stated in the accessible abstract. Full preprint inaccessible, so historical coverage risk remains explicit.

## value

PASS

Sharp and robust nonexistence for every positive-turnout pure equilibrium under finite cost spectra, plus discontinuous stability of equilibria under arbitrarily small uniform payoff perturbations, is meaningful for participation-game discretization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
