---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification record

## Proof-critical analytic checks

The kernel identities \(u=1/(r+1)\) and \(f(u)=1/((r+1)(r^2+1))\) use \(r>1\) and retain all strict temperature endpoints. The numerator of the exact second derivative has positive factors on \(0<u<1/2\), proving strict Jensen convexity. The upper gap is positive at every interior temperature. The two-point chord family has limiting ordinates \(u/2\) and \(f(u)\); continuity gives a finite, strictly positive two-component reconstruction for any intermediate ordinate. These steps, not a finite parameter search, prove the theorem.

## Reproducibility

Run `python verify.py` with Python 3 and SymPy. The embedded code checked three symbolic identities, 1,200 rationally parametrized mixtures (including equality diagnostics), 400 two-temperature chord reconstructions to absolute tolerance below \(2\times10^{-13}\), and the exact rational example. The embedded version passed 4,008 assertions. The randomized rational checks use a fixed numerical seed for reproducibility. Inputs include only finite rational test parameters; no numerical test establishes the uncountable parameter-space claim.

## Limits

All results apply only to exact monochromatic fluxes at \(\nu,2\nu,4\nu\) with a specified, identical emissivity index, strictly positive finite temperatures and coefficients, and optically thin thermal emission. Independent scientific validation and a separate historical-priority audit have not been performed.
