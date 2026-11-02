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

PASS: Direct Legendre-integral evaluation gives A0=(1+e^{-pi a})/(1+a²), A1=(1-e^{-pi a})/(4+a²) and positive two-step recurrence A_{n+2}/A_n=(a²+n²)/(a²+(n+3)²). Using xP_n recurrence, C_n= A_{n-1}(a²+n²+n+1)/(a²+(n+2)²) for n>=1 and C0=A1>0, so Schoenberg signs of A_n+bC_n reduce exactly to b>=-inf_n A_n/C_n. The explicit ratio T_{n+2}/T_n numerator-minus-denominator is 3(2n+3)(3n²+9n-7-7a²); therefore each parity has a single valley with possible tie and only the claimed two candidate degrees need checking, while T2<A0/A1. Boundary zeros occur in finitely many degrees, leaving infinitely many positive Legendre coefficients of each parity; Chen-Menegatto-Sun strictness gives strict positive definiteness. Independently simplified polynomial identity symbolically; numerically quadrature-checked Legendre coefficients for a=.2,1,2,5,10, degrees 0..5 and verified two-candidate minima through 29 degrees. Finite calculations support but do not substitute for the analytic all-degree proof.

## originality

PASS

Best-of-knowledge PASS: standard Schoenberg and strictness theorems and the unmodulated geodesic exponential are acknowledged as prior facts. The two-parameter cosine-modulation has an exact necessary-and-sufficient negative-b threshold and a parity-dependent two-degree selection that are not asserted in the inspected primary families and sufficiency-only Pólya criteria.

## value

PASS

PASS: The sign-changing first-harmonic modulation of a standard sphere covariance kernel is natural, yet generic completely-monotone sufficient conditions fail to decide its negative-b range. The exact all-parameter PSD/strict-PD classification collapses infinitely many Legendre inequalities to two computable degrees with parity-dependent switches. This is a motivated harmonic-analysis classification and practical covariance admissibility criterion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
