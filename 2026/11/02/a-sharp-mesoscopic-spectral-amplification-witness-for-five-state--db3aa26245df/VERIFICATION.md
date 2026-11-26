---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The constant stationary flux is J=epsilon/(2+3epsilon), and the centered observable has mean subtraction m=J(x+y+z). For u solving (i omega−Q)u=f (using the centered Poisson equation at zero), stationarity and the two-sided Fourier convention give G=2 Re⟨u,f⟩_pi=J sum_j |u_j−u_{j+1}|², cyclically. At zero, u_j−u_{j+1}=f_j/r_j where r_j is the exit rate; thus G(0)/epsilon tends to (x²+y²+z²)/2+(x+y+z)²/4. At positive frequencies in the stated window, the two slow-step resolvent prefactors and slow centered forcing tend to zero, the three fast-step prefactors tend to one, and one tour has feedback tending to zero. The unique solution stays bounded and tends to (0,x,0,y+z,z); summing its squared jumps gives the asserted A after the flux factor. This works along every scale with epsilon/omega→0 and omega→0. B is strictly positive for nonzero triples and 12B−5A=[(4x+3y+3z)²+7(y−z)²]/4, giving exactly the line through (−3,2,2) as equality. For this observable, omega=√epsilon yields the limiting witness 7/12 via Gmax≥G(√epsilon). The proof gives a global lower bound only, not frequency-global sharpness for all amplitudes, finite-rate attainment, or an equality for eta_5*. The frozen rational-check script was inspected, not executed.

## originality

PASS

The closest accessible result uses the identical efficiency definition and gives a five-state upper bound, but no lower witness of this strength; its established small-N equalities do not do so either. The indexed related results concern different observables or smaller cycles. The supported distinction is the sharp mesoscopic/DC ratio in the stated family and the resulting constructive lower bound, not the general spectral or regenerative method.

## value

PASS

The construction surpasses the sharp four-state benchmark 1/2 by 1/12 in a concrete five-state limit, narrowing a genuine gap in the known efficiency bounds. The amplitude extremizer makes this a sharp benchmark for one motivated family, not a numerical instance or an arbitrary choice of weighted observable. It sheds light on the contribution of fast excursions at frequencies above the slow transitions and makes no finite-dissipation or unrestricted optimality claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
