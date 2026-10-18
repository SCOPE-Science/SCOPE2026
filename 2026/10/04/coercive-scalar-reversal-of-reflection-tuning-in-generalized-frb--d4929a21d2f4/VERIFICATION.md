---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-14.md",
      "INDEPENDENT_AUDIT_2026-10-14.json"
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

Substituting g=0 and F(x)=ax, a>0, in the two-step constant-reflection scheme gives A=1-(1+alpha)t and B=alpha*t with t=a*tau>0, x[k+1]=A x[k]+B x[k-1]. The monic polynomial z^2-Az-B has one positive and one negative real root; Jury inequalities 1-A-B=t>0, 1+A-B=2-(1+2alpha)t>0 and 1+B>0 give exact Schur stability 0<t<2/(1+2alpha). For x[-1]=x[0]!=0, x1/x0=1-t cannot equal a root since p(1-t)=-alpha*t^2!=0, so the unstable boundary mode cannot cancel. The spectral factor is (sqrt(A^2+4B)+|A|)/2. For A>=0 the dominant root derivative has sign alpha-(1+alpha)q, negative because its root is strictly greater than alpha/(1+alpha) (evaluate polynomial there). For A<=0 derivative is positive. Thus the unique minimizer is t*=1/(1+alpha), q*=sqrt(alpha/(1+alpha)); the scalar stability ceiling decreases and the optimal factor increases with alpha. Independent numerical checks for alpha=0.501,0.7,1,2,4 and boundary/near-optimal steps corroborate the algebra; no finite test proves all alpha.

## originality

PASS

The alpha=1 scalar FRB case and ordinary Schur/Jury tests are prior elementary calculations. The claimed remainder is the exact alpha-variable scalar phase diagram and optimal rate contrasting the general monotone/skew-motivated reflection choice. Resultary returned split-skew robust tuning (different operator), fixed-reflection affine reflected gradient (only alpha=1), and averaged proximal reflected gradient (different scheme). The originating September 2026 source abstract confirms the variable alpha and alpha>1/2 boundary; its full primary PDF was inaccessible in this run, so an equivalent modal calculation therein remains a specific priority risk, not automatically a failure.

## value

PASS

Positive scalar aI is the canonical pure coercive mode, and alpha is the central adjustable parameter of the generalized method. An exact all-alpha stability/rate frontier quantifies a meaningful geometry-dependent reversal relative to robust monotone/skew tuning. It does not claim to improve the general convergence guarantee.

The dated certificate retains the supplied scientific assessment, sources and limitations.
