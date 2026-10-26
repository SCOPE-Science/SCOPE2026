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

# Verification details

Analytic checks: the rank-one matrix integral reproduces \(B_{nk}=(n+1)\sqrt{w_n(\beta)/w_k(\alpha)}/(n+k+1)\); the generating identity \(\sum_{k\ge0}r^k/w_k(\alpha)=(1-r)^{-\alpha-2}\) follows from the binomial theorem. For \(1<\beta<2\), the boundary trace-norm growth exponent is \(-1+(\beta-\alpha-2)/2\), and for \(\beta\ge2\) the strict margin \(-\alpha/2>0\) absorbs any logarithm. Thus the choice \(\theta=\min\{\beta-\alpha-2,-\alpha\}/4\) works in all cases. A radius-two Cauchy circle yields the \(4^{-m}\) remainder after order \(2m-1\); positive Gauss–Legendre weights and dyadic tail integration then yield the infinite-dimensional trace-norm estimate.

Finite-section reproduction: run `python check_operator.py` using NumPy and SciPy. For a 100-by-100 section with \((\alpha,\beta)=(-0.5,1.75)\), the operator-norm differences of direct and quadrature matrices at \(J=m=4,6,8,10\) are respectively about 2.26267, 1.34558, 0.502865, and 0.142445. At \((-0.5,2.5)\) they are 1.50927, 0.813571, 0.285884, and 0.0792440. At \((-0.9,1.2)\) they are 1.85162, 1.11233, 0.423287, and 0.120793. The tests provide no lower spectral bound and are not an exhaustive or infinite-dimensional certificate. Independent audit has not been performed.
