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

Each length-m equality pattern with l unequal edges is realized by q(q−1)^l words, giving independent Bernoulli edges. Dropping equal-letter swaps and comparing the first edge on which two effective matchings differ proves injection; each one-run of length l has F_{l+2} matchings. Renewal at the first zero gives the stated moment generating series A_t(z)/(1−hzA_t(z)), including the no-zero term. For all real t, Binet gives a positive limiting geometric coefficient, so A_t diverges at its positive convergence radius, even for negative t. The positive denominator root r is strictly inside that radius and simple; equality in the triangle bound on |z|=r together with the positive z coefficient excludes another zero there. A slightly larger disk with this single pole also works locally for complex t; subtracting c(t)/(1−z/r(t)) and using Cauchy gives the exponential error with c=A_t(r)/(hr[A_t(r)+r A'_t(r)])>0 on the real line. Tilt differentiation gives E_t R/E_t T and E_t[(R−P'_q(t)T)^2]/E_t T, strictly positive by the l=0,1 cycles, with E T=1/h at t=0. The analytic log-MGF expansion proves the CLT and O(1) cumulant errors; small positive and negative tilts give summable Chernoff bounds and hence almost-sure convergence in the prefix coupling, or any common coupling with the stated marginals. Bounded normalized log-volume and differentiability on the whole real line give the full good LDP. The annealed recurrence gives its stated root. For the alphabet limit write R=T log phi−d+e_L with e_l geometrically decaying. Then h E e_L=O(h^2), e_L=o_{L^2}(1), and hT has second moment tending to two and mean one. Thus R−mu T=d(hT−1)+o_{L^2}(1), giving the variance coefficient. Expanding the annealed root and using log u>1−1/u for u=sqrt(5)/phi proves the positive gap coefficient. The supplied script and output were inspected, not executed; finite ball and moment regressions do not prove the limit laws.

## originality

PASS

Credit the unified explicit all-real pressure with locally analytic pole asymptotics, the LDP for uniform-center log ball volume and the large-alphabet entropy, variance and annealed-gap coefficients. The known Fibonacci ball product and arithmetic mean are not new. In addition, a distinct indexed result already covers the exact LLN and Gaussian constants and strict typical/mean gap; these are not credited as distinct by themselves. The frozen result as a whole is not a corollary of the indexed result or of the published channel formulas, since the full pressure, its rate function and alphabet asymptotics survive comparison. This is a coverage judgment, not a claim of historical precedence between records.

## value

PASS

Uniform-center ball volume is a natural geometric statistic of a specified channel. The exact all-real pressure distinguishes typical behavior, tails and arithmetic moments, and the explicit alphabet coefficients quantify how the gap closes. These provide information not available from mean volume, isolated Gaussian constants, or capacity bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
