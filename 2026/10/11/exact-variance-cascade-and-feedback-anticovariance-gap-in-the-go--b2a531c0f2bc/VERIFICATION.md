---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

For any compact-support invariant probability on the nonnegative orthant, invariance of antiderivative f(X), f(Y), f(Z) with arbitrary continuous f yields E[Φ(Z)−k4X|X]=0, E[k2X−k5Y|Y]=0 and E[k3Y−k6Z|Z]=0. Thus speeds are orthogonal regression residuals, giving three exact variance-energy decompositions, including E[Ẋ²]=Var(Φ(Z))−k4²Var X, E[Ẏ²]=k2² Var X−k5² Var Y, E[Ż²]=k3² Var Y−k6² Var Z. Stationarity of centered products XZ and YZ yields relations for covariances; eliminate C_XZ and C_XY to obtain k2 k3 Cov(Z,Φ(Z))=k6(k4+k6)(k5+k6)Var Z−k3²(k4+k5+k6)Var Y. Hill Φ strictly decreases for Z≥0; Cov(Z,Φ(Z))=1/2 E[(Z−Z′)(Φ(Z)−Φ(Z′))]<0 whenever Var Z>0; if Z constant, the stationary equations force all coordinates constant, unique equilibrium. Therefore strict sharpened VarY>k6(k4+k6)(k5+k6)/(k3²(k4+k5+k6)) VarZ for non-equilibrium; its improvement over direct filter k6²/k3² is 1+k4k5/[k6(k4+k5+k6)]>1. Re-derived covariance elimination and factor symbolically, with 9/500 versus 1/100 at printed Ruoff rates and 4/3 for equal downstream rates.

## originality

PASS

Two primary same-model full texts were compared at statement and implication level. Ruoff–Rensing 1996 prints the identical three ODEs with Hill exponent nine and discusses period, phase shifts, temperature compensation, and limit-cycle parameters; its full 11-page text has no covariance/variance or invariant-measure theorem. The complete later Hill-feedback analysis studies onset and persistence of oscillations, not all-invariant-measure conditional regressions or the exact three-stage attenuation factor. Their model equations alone support stationary moment algebra, but no inspected prior stronger moment identity was found; explicit residual risk remains that the computation is known in stationary moment/control literature.

## value

PASS

The direct serial negative-feedback circuit motivates each conditional projection and fluctuation budget, and the strict feedback anticovariance quantifies biologically meaningful attenuation beyond purely linear downstream filters. The result is exact for every compact invariant measure (not just a simulated periodic orbit), identifies equality only at equilibrium, and gives a concrete rate-dependent improvement (9/5 at a published Goodwin parameter set). These are natural structural dynamical invariants, not an arbitrary small numeric perturbation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
