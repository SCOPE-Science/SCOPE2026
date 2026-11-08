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

For one-dimensional Brownian half-line absorption, no-reset survival S1(t,z)=erf(z/√(4Dt)) has strictly negative second z-derivative for z>0; for exterior absorption at sphere radius a, S3(t,z)=1-(a/z)erfc((z-a)/√(4Dt)), and S3,zz=-a(E″/z-2E′/z²+2E/z³)<0 because E>0,E′<0,E″>0. Hence convex-order spreads decrease free-cycle survival strictly, and Jensen/chord yield unique extremal laws Q_end supported at ell,u and δ_m for fixed mean m. Coupling iid post-reset cycle hitting times via common increasing quantiles and common iid positive finite renewal deadlines, with the same initial hit time, gives almost sure ordered total completion times for any independent reset clock (not necessarily exponential or finite mean). Success probabilities per cycle are positive since reset radii stay in a compact interval strictly outside the absorber and every deadline is >0; absorption is almost sure even when a free 3D hit can be infinity. Strict concavity and a positive chance to reset before initial absorption imply distributions differ for distinct convex-ordered laws; not every t is strictly ordered. Under Eσ<∞ the separate renewal reward gives b0+q0 bQ/pQ. These prove full-law and all-increasing-cost extremality, not only Poisson MFPT.

## originality

PASS

Julián-Salgado et al. 2023 and Méndez et al. 2024 treat random reset positions but optimize or compare mean times with exponential reset clocks. The 2025 compact-support follow-up also optimizes Poisson rate. Those formulas already imply parts of the Poisson mean convexity by Jensen, so that special case is not credited as new. The complete stochastic order for all strictly positive independent renewal clocks together with defective 3D sphere free-hit laws is the assessed additional claim. A general convex-order composition/restart theorem may have the same implication, which is a real priority risk.

## value

PASS

Full distributional control of Brownian search time, uniform over renewal-clock laws, is a motivated reset-policy optimisation problem: it orders all increasing time costs and tail risks, stronger than mean optimisation. Sharp unique extremisers under mean-distance and support constraints answer a natural exact design question in both certain- and defective-hitting geometries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
