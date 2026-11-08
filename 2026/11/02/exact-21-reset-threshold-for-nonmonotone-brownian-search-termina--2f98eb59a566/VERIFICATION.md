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

Independent-cycle decomposition gives E[min(τ,E_r)]=q/r and T_μ=(q+...+q^(μ+1))/r for q=1-e^-z and z=a sqrt(r/D). Differentiating yields derivative sign f(q)E_(μ+1)(q)-2. Index-mean E_n increases in n and q, while f decreases. For n=21 the low/high q analytic estimates and the exact 80-subinterval rational bound over [1/2,19/20] prove globally negative derivative; the independent exact-rational check reproduced 159 nodes and 80 leaves. At n=22, seven-term atanh lower bound for log7 and a rational weighted-index inequality prove positive derivative at q=6/7, propagating to higher n; endpoint signs are negative. The strict analyticity argument yields at least one minimum and later maximum, not unique extrema. Important primary-reference correction: the frozen text says Eq 5.37 of Bressloff for finite-budget mean, whereas full paper Eq 5.38 is finite-budget and Eq 5.37 unbounded-reset; the formula and proof itself are correct.

## originality

PASS

Bressloff 2023/2024 gives the identical Brownian finite-reset mean in Eq (5.38) and Fig 4 qualitative small-versus-large budget examples (not a sharp integer 21 or an all-budget proof). The frozen package cites Eq (5.37) incorrectly—its scientific formula nevertheless matches Eq (5.38). Biroli–Majumdar–Schehr study a critical number of independent walkers with resets, not a one-walker finite reset budget with fatal event. The exact derivative sign threshold is additional; bounded risk of an earlier implicit threshold computation remains.

## value

PASS

The original finite reset allowance is an actual resource in the model and prior work observed a nonmonotone effect numerically. Proving the first precise allowance 21, uniformly in distance and diffusion, is a motivated phase-boundary theorem; exact rational covering of the delicate low-budget range is substantive, though no unique stationary-point count claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
