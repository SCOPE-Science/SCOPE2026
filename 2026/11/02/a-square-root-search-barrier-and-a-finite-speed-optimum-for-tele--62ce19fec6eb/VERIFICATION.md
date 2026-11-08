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

Phase-preserving position resets with symmetric switch rate nu produce coupled backward equations D m0 double prime+nu(m1-m0)=-1 and D m1 double prime+nu(m0-m1)+rho(m1(0)-m1)=-1. B=[[nu,-nu],[-nu,nu+rho]], E=exp[-a sqrt(B/D)], H=(I-E)B^-1, e=E 1,h=H 1 give m1(0)=h1/e1 and m0(0)=h0+(1-e0)h1/e1. Eigenvalues b_±=nu+rho/2 ±sqrt(nu²+rho²/4) prove M~a/(2 sqrt(D nu)) as nu↓0 and M=T(rho/2)-(rho²/(8 nu))T prime(rho/2)+O(nu^-2) as nu→∞ with T(s)=(exp(a sqrt(s/D))-1)/s. T prime changes sign at z*=1.593624..., so z>z* yields some finite nu below infinite-speed limit and a global finite minimizer by continuity/coercivity. No uniqueness or converse claimed. Independent 2x2 eigenchecks verify fast correction and slow sqrt singularity; slow check requires sufficiently tiny nu due to large regular part.

## originality

PASS

Related switching diffusion papers solve MFPT under resetting, but in the inspected Bressloff model the Brownian diffusion coefficient switches and position reset also redraws the phase, whereas the assessed model switches reset *intensity* and preserves phase. Arutkin–Reuveni treat intensity modulation but analyze stationary position laws and list first passage as further direction. Qualified PASS with higher priority risk for uninspected Markov-modulated first-passage works.

## value

PASS

The exact 2x2 matrix MFPT formula and fast-switching sign criterion establish a provable finite optimal switching speed despite diverging low-switching mean; the square-root barrier is a natural singular-stochastic-search invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
