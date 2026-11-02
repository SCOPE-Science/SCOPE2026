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
# Verification of the crown-graph precision result

Run `python3 verify_crown.py` using Python 3.10 or later. The standard-library-only checker reports **4030 exact checks passed**; there is no floating-point comparison in the assertions. Its checks include exact polynomial expansion of \(E_n\) at \(2\le n\le6\) and exhaustive summation of independent-set configurations for the rational fugacities \(1/5,1/2,1,3,10\). It verifies partition functions, moment classes, covariance-matrix inverses, and the matched-entry formula.

The proof of the strict sign inequalities for all real \(\lambda>0\) uses these integer polynomial identities together with Descartes' rule of signs and elementary positivity; it is not inferred from finitely many numerical sample points. Positive definiteness comes from the distribution's empty and singleton support. There has been no independent audit; historical priority is not certified. Nonlinear conditional independence is a separate graphical-model property, not an assertion inferred from the inverse covariance.
