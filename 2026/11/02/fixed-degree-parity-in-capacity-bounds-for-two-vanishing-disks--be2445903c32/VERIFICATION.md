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

# Verification

The analytic argument proves every fixed index without computational extrapolation. It uses (i) logarithmic-energy bounds obtained from equilibrium circles and cross-distance estimates, (ii) the exact disk Taylor norm formula, (iii) uniqueness/parity of monic planar \(L^2\) minimizers, and (iv) invertibility of finitely many jets to control coefficients as \(r\downarrow0\). Normalization is unweighted area \(dA=dx\,dy\).

Run `python3 CHECK.py` using Python 3 and the standard library to reproduce exact Gram-system calculations for \(a=1\) and indices 1 through 6 at rational radii. The checker confirms explicit formulas for the first three indices and numerical approach of the remaining coefficients using exact rational arithmetic. It is supplementary evidence only: it does not prove the universal fixed-degree asymptotics, which are established in `RESULT.md`.

Scientific limitations: no assertion is uniform in the polynomial index, and potential implicit coverage in older multi-island asymptotic literature has not been fully eliminated. Independent mathematical audit has not been performed.
