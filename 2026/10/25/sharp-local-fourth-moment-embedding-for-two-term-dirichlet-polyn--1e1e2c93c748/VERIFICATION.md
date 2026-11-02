---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

For P(s)=a m^-s + b n^-s, m<n integers, the global Bohr fourth mean is u^4+4u²v²+v^4. If m>=2, the pointwise bound (u+v)/sqrt2 and factorization 8D-3(1+x)^4=(x-1)^2(5x²-2x+5)>=0 give ratio <=2/3. If m=1,n>=3, pointwise bound u+v/sqrt3 and positive decomposition 3(1+12y²+9y^4)-2(1+y)^4=(1-4y)^2+y²(25y²-8y+8)>0 give ratio <3/2. The 1,2 pair has exact local integral as a cos(phi),cos2phi polynomial; both harmonic coefficients positive, so unique maximizing relative phase phi=0. Its x-ratio derivative numerator is -A x^6/2+(2-2B)x^5-Ax^4-3x^3-5Ax²/2+(2B-8)x+A, strictly decreasing in x>0 since 2<B<3, hence unique positive optimizer xi. F(1/2)>3/2 establishes strict pair rigidity; zero-coefficient cases <=1. Independent symbolic factorization and derivative checks and bisection yield xi=0.4441040639694337, C=1.6076693260885673. No inference about unrestricted C4 is made.

## originality

PASS

Chen et al 2026 solves finiteness for all Dirichlet polynomials at p>=2, not necessarily the SHARP two-term p=4 constant or optimal support. The 127-page full Chen manuscript could not be retrieved through public arXiv/OA paths and Oxford reported vpn_disconnected; its abstract alone cannot establish complete noncoverage. Brevig 2016 is a weighted full-line p=2 embedding constant and explicitly notes unknown sharp local p=2 constant. Prior character-pair Haar fourth moments determine global denominator but not unit-interval critical-line numerator. A qualified best-of-knowledge PASS is appropriate given the distinct exact finite-sparsity claim and explicit high-priority comparison risk.

## value

PASS

A sharp finite-sparsity extremal case for a central local embedding problem provides a rigorously computed C4 lower bound 1.6076693>3/2 and full coefficient/support rigidity. Exact two-mode constants serve as canonical benchmarks for any subsequent unrestricted estimate and are not simply restatements of finiteness or L4 Bohr norm.

The dated certificate retains the supplied scientific assessment, sources and limitations.
