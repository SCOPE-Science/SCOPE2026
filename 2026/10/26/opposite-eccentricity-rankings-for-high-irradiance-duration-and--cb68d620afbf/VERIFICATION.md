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

## Reproduction
Run `python verify.py` with Python 3's standard library. The script directly integrates the full eccentric anomaly using the exact physical-time weighting and compares both quantities to their closed forms at 90 seeded random admissible cases, checks the calculated unique duration maximum using two bracketing eccentricities in each case, checks increasing excess dose, and evaluates a deterministic illustrative threshold. This is not a machine certification of the universal proof.

## Analytical checks
The proof uses the Kepler phase element \(dt/P=(1-e\cos E)dE/(2\pi)\). The strict super-circular flux threshold gives \(e\cos E>\delta\), with \(\delta=1-\eta^{-1/2}\in(0,1)\). For \(e>\delta\) the threshold crossings occur at \(\pm\arccos(\delta/e)\). The derivative of the exact duration expression has sign \(\operatorname{sgn}(\delta-e^2)\); the derivative of the excess integrand has a strictly positive integral because threshold crossings occur before eccentric anomaly \(\pi/2\). Endpoint contributions vanish for the excess dose since its integrand is zero at the crossing.

## Scope limits
The numerical checks are finite and do not substitute for proof. The formulas concern an idealized fixed-semimajor-axis inverse-square stellar flux and do not include radiative climate response, finite stellar radius, multiple-body perturbations, occultation, or an evolutionary mechanism that changes orbital eccentricity. The results do not quantify actual habitability. No independent mathematical audit has been performed.
