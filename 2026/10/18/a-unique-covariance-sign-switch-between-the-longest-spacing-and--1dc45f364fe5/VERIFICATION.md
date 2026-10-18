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

The proof in `RESULT.md` contains the complete analytic derivation and the sign-classification argument for all integers \(m\ge2\) and all real \(t\in[0,1]\).

Run `python verify.py` from this directory after installing SciPy. The checker compares an exact rational finite-sample formula with a separately conditioned integral, verifies boundary identities, and numerically brackets the unique sign-changing root. Its successful reference run yielded 539 exact rational grid evaluations, 44 numerical integral comparisons, 10 root checks, and the endpoint and conditional-mean identities.

The tests do not exhaust real thresholds or all dimensions and therefore are not an independent proof. The principal proof requires the simplex tail identity, exchangeability, convexity of a conditional maximum of affine functions and positivity of the marginal density. Classical references establish the marginal maximum moment used as an input. Independent audit and independent validation have not been performed.
