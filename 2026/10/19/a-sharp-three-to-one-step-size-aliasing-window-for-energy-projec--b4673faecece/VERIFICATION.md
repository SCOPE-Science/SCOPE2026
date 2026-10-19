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

# Verification of the theorem

The exact stage-chain stability-polynomial identity, phase-derivative numerators, and root signs are proved in `RESULT.md`. The standalone `verify_phase.py` implements the same objects in symbolic exact arithmetic and high-precision arithmetic, using direct Runge–Kutta stages as a separate implementation of the step.

Run from a directory containing the attached files with `python verify_phase.py` and Python 3 with `sympy` and `mpmath` installed. The tested standalone program reported `PASS 754 algebraic / rational / high-precision assertions`.

The script checks polynomial identities at all five degrees, the relevant exact rational signs, 45 positive rational test steps for each of degrees two through five, the actual full-rank stage spans, five phase speeds at five samples each, three independent one-radian phase aliases, and repeated norm preservation. No finite test substitutes for the root-count or all-positive-steps proof. The approximate turning steps and phase angles are diagnostic only.

The scientific claim is restricted to planar linear oscillators and exactly projected Taylor stability polynomials. Existing general invariant-projection and phase-lag frameworks are prior work. Full text of one relevant older projection/dispersion article was unavailable; its possible implication remains a separate originality risk. An independent audit or proof certification has not been performed.
