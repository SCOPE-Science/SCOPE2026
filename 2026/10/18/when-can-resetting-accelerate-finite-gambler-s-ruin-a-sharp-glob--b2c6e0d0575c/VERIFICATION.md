---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-23.md",
      "INDEPENDENT_AUDIT_2026-10-23.json"
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

With q=1-gamma, solving the killed simple-walk resolvent gives F(q)=E[q^T]=cosh(|N-2i|theta/2)/cosh(Ntheta/2), cosh theta=1/q. Restart renewal yields M=(1-F)/(gamma F), including reset time. For y=(1-gamma)^-1=1+z, A(y)/B(y) is the Chebyshev even/half-integer numerator ratio, and sign of M-Delta (Delta=i(N-i)) is W(z)=(1+z)(A-B)-Delta z B. Both constant and linear W coefficients vanish; its z^2 coefficient is Delta/24*[N^2-5(N-2i)^2+20]. Negative value gives a beneficial infinitesimal rate. To prove global necessity, coefficients of A,B are nonnegative, with recurrence c_j/c_(j-1)=(lambda^2-(j-1+s)^2)/(j(2j-1)); when the z^2 coefficient is >=0 the ratio a_k/b_k grows by at least U/V>=3 and the positivity threshold Q_k grows by at most 14/5, so every higher W coefficient is >=0, and the top one strictly positive. Thus M>Delta for all positive rates at nonnegative threshold. At gamma->1, F->0 and M->infinity, so benefit for small gamma entails interior minimum. Even/odd N and mu=s exceptional B=1 are handled explicitly. Independent exact polynomial coefficient checks for all N<=30 and all i confirmed the predicted coefficients and sign regimes; this finite evidence does not prove the universal inequalities.

## originality

PASS

Best-of-knowledge statement-level originality is limited to the differentiated new result, with credited general tools, broader prior coverage, and recorded access risks. Existing first-derivative reset threshold does not logically establish the strict global converse.

## value

PASS

An exact necessary-and-sufficient global criterion is a structural improvement over known infinitesimal-reset sufficiency: in a finite absorbing chain a local no-benefit test need not generally exclude an advantageous intermediate reset rate. The theorem proves this exclusion specifically for every symmetric nearest-neighbor gambler's ruin instance, including the zero-derivative boundary, resolving a natural protocol-sensitive phase diagram and a meaningful finite-size correction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
