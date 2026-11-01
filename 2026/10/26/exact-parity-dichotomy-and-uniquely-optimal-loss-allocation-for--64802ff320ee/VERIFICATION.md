---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Reconstructed matching conditions at two imaginary potential impurities: t=1/[(1+X)(1+Y)-XY exp(2ikd)], r=[-X(1+Y)-Y(1-X)exp(2ikd)]/denominator. With k=pi/2 and d even the phase is +1 and absorption collapses to 2b/(1+b)^2. For odd d phase -1, transmission denominator D=1+b+2x(b-x)>0 and reflection numerator R=b-2(b+1)x+2x^2, yielding A=1-(1+R^2)/D^2; transmission remains nonzero for every finite b. Differentiating gives A_prime=8P_b(x)/D^3. Under z=x/(b-x) the quartic has negative coefficients for z^4,z^3,z^2, an arbitrary z coefficient and positive constant, so Descartes plus endpoint signs gives exactly one positive root. It strictly increases then decreases and the interior maximizer beats both endpoint splits. The phase-dependence inequality is positive for every split in the interior, so odd optimum strictly outperforms even constant baseline. Substituting asymptotic series into the unique polynomial root yields x*=b/2-b^2/8+O(b^3) near zero, x*=1/2-1/(4b)+1/(4b^2)+O(b^-3) large, with deficit 1/(4b^2)+O(b^-3). Independently verified symbolic quartic derivative and z-conjugacy and eight positive-budget uniqueness cases. Numerical tests are corroboration, not all-budget proof.

## originality

PASS

Best-of-knowledge originality for the stated final claim after direct comparison of prior implications and source materials; foundational methods, source models and matching components are explicitly credited. Exact parity dichotomy and uniquely optimal loss allocation for two absorbing lattice sites is not inferred new merely because an exact phrase search fails. Unindexed equivalent publications remain a disclosed risk.

## value

PASS

A fixed total imaginary onsite loss is a natural resource constraint in two-port wave scattering. Even/odd site separation produces a structural parity switch, while all-budget uniqueness solves a nonconvex allocation problem globally and shows that a two-site arrangement overcomes strong-loss reflection of a single defect. The exact near-perfect scaling and upstream design limit have specific physical and mathematical meaning, while generic near-perfect one-sided absorption is explicitly acknowledged as prior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
