---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For uniform initial [0,1), exact dyadic shell probabilities obey the stated reset biased-walk recurrence. Kernel cancellation at r=z(p+q r^2) yields M_p(z)=r/[z(1-r)(2p-qr)] and Lagrange/ballot coefficients give the stated finite binomial mean. With p_n=1/2+alpha/sqrt(n) and c_n=q_n/(2p_n)->1/2, the tail correction E[S^+ c_n^S] is O(1); triangular-array CLT plus uniform integrability gives sqrt(n) E X_n -> 2 E[(Z+2alpha)^+] = sqrt(2/pi)exp(-2alpha^2)+4alpha Phi(2alpha). Independently coded rational dyadic-shell integration and ballot expectation agree in 32 cases. The proof does not infer the all-n limit from those cases.

## originality

PASS

Monthus (2024) derives the full shell transient propagator and formulae for physical coordinate for the exact same Pelikan map, so those ingredients and the finite-time representation are not original. The asserted residual contribution is the *moving-parameter* p=1/2+alpha/sqrt(n) asymptotic with the complete Gaussian crossover function. Relevant primary full-text portions on Eq. 66 and Eqs. 157–159 were compared; they work at fixed p/critical point, not a uniform matched p_n window. This is a close priority comparison because a sufficiently strong unexamined uniform consequence of the prior propagator could imply the crossover; the claim is not certified historically.

## value

PASS

The width n^{-1/2} near the intermittent threshold is natural for a biased random-walk crossover. The explicit entire Gaussian positive-part curve for a physical coordinate quantifies a genuinely nonstationary finite-observation transition with fixed sharp coefficient, rather than a parameter-renaming or one-number calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
