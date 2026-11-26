---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

At ad=bc the column generator Q has stationary weights (1,1,r)/(r+2) and satisfies detailed balance after forgetting channel labels. Let x=e_g-e_i, y=e_i-e_e/r, P(s)=exp(Qs). Pairing the two orders of distinct marked jumps and using symmetry of P(s)diag(1,1,r) gives the covariance kernel w(u+rv)y^T P(s)x/(r+2); there is no same-jump mixed term and the work mean is zero. Since x has zero total mass, f=-y^T P(s)x has f(0)=1, f'(0)=-K and satisfies the scalar ODE with the two nonzero decay eigenvalues of Q (sum of decay rates T, product Z). Reversibility makes those rates positive real, and a sum of two real decaying modes has at most one sign change; a repeated eigenvalue does not create a problem. Its integral is (T-K)/Z=(r+2)b/Z>0. The primitive rises initially and, if it later falls, remains above its positive limit. Integrating again gives G(t)>0 for each t>0, not a mere asymptotic sign. G(t)/t tends to (r+2)b/Z; the leak mean and covariance recover u-rv and u+rv and hence both rates with known aggregate parameters. Independently for the work variance rate, the same-jump contribution is 2w/(r+2); the paired-jump term is -2w^2/(r+2) times the integral of x^T P(s)x. On zero-total-mass vectors the integrated semigroup is (T Id+Q)/Z by Cayley–Hamilton, giving integral (r+2)(b+d)/Z and variance rate 2wrbd/Z. RESULT.md, VERIFICATION.md, and verify.py were read; the frozen code was not executed. The calculation is an exact stationary ensemble result, not a finite-sample estimation guarantee or a quantum-dynamics result.

## originality

PASS

The source engine and its mean currents are prior, as are tilted-generator counting methods. The supported distinct contribution is the strict sign of the finite-duration covariance of these two signed, separately labelled currents even when the leak mean is zero or changes sign, with its use in identifying both microscopic leak rates. The inspected comparisons do not establish this result by a parameter substitution or specialization of a stronger sign theorem.

## value

PASS

At work stall neither the work mean nor the leak mean can distinguish increased bidirectional leak traffic from mere changes in net flux. A strictly nonvanishing mixed covariance identifies the missing symmetric rate combination at any positive duration. The all-duration sign is more informative than a long-time noise calculation, and the small-t scaling warns against assuming statistical conditioning at short times. Value is for the stated channel-resolved stationary rate model with known aggregate parameters.

The dated certificate retains the supplied scientific assessment, sources and limitations.
