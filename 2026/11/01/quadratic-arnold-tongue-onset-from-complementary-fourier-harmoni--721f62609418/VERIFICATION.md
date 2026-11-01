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

# Verification of the stated asymptotic result

The exact proof consists of the uniform second-order composition expansion, the geometric-sum identity for every Fourier pair, the coefficient calculations for the constant and \(q\)-harmonic terms, and the rotation-number/return-fixed-point characterization. No software certificate is needed for these algebraic and dynamical steps.

The provided standard-library `CHECK.py` was executed from the current package source and returned `PASS: 306 direct harmonic/return/threshold finite checks`. It computes both the double-sum and the Fourier prediction independently, tests error scaling at three small forcing amplitudes, and estimates the actual tongue width by finding detunings for 600 phases. The checker uses floating-point trigonometry and is confirmatory only; it cannot prove a claim for infinitely many rational denominators.

The leading-term error is understood for each fixed parameter tuple, not uniformly across denominators. The odd-denominator selection rule does not claim that noncomplementary harmonics never produce rational locking. The first verified public date of the motivating paper is its explicitly stated journal release date of 2022-09-06; an earlier public manuscript was not established in the inspected sources.
