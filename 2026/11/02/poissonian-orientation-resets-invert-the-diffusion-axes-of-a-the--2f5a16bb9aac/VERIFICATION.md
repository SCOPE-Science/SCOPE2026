---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

The positive-definite block mobility μ=[K,h;h^T,m] has independent Schur noise E=Θ(K−hh^T/m) and angular diffusion D_r=Θm. Between orientation-only Poisson resets the cross term integrates in Stratonovich form to (R_{φ_S}−I)a, a=−Jh/m, with X fixed at jumps. Independent exponential renewal excursions give v=E[Y]/E[S]=−D_rρa/(1+ρ) and centered diffusion E[(Y−vS)(Y−vS)^T]/(2E S). Harmonic Laplace transforms C1=ρ/(ρ+1), C2=ρ/(ρ+4) give exactly the asserted f_parallel, f_perp and the rotated Schur matrix term. Bounded regenerative remainders yield CLT and asymptotic covariance. Independent symbolic reconstruction of first two angular reward moments and length compensation exactly equals the submitted f_parallel and f_perp for every positive formal ρ. Their derivative factors and difference polynomial prove unique maximum ρ=2 (value 5/27) and unique positive axis switch root ρ³+ρ²+ρ−2=0 in the isotropic-Schur c≠0 subfamily. High-rate tensor equals ΘK, low-rate tensor tr(E)/2 I. This checks the nonstandard random-duration correction, not merely a simulation.

## originality

PASS

Cleuren–Eichhorn arXiv:2603.19430, personally examined in full primary 7-page PDF, gives the general thermally cross-coupled mobility and regular periodic orientation resetting with drift; page 3 equation (8) is fixed-period mean transport, not a random-clock centered diffusion tensor. Chaki–Olsen–Löwen arXiv:2406.17550/2025, read in full public uploaded text, obtains a Poisson orientation-reset diffusion tensor (Section V Eq.64), but equations (1)–(3) have only three diagonal body mobilities and independent angular/translational noises: it equals the h=0 subcase, already known. The submitted h≠0 rank-one additive noise-correlation term and exact rate-optimum/axis-switch are not implied by either prior displayed result. A more general renewal-reward formula may provide a route to the same evaluation and remains priority risk.

## value

PASS

For a natural passive coupled colloid, diffusion anisotropy determines spatial dispersion independently of mean sorting drift. A complete exact mobility-dependent tensor plus a universal axis inversion at ρ≈0.810536 and a different peak at ρ=2 supply substantive controls and a counterexample to monotone orientation-preserving effective diffusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
