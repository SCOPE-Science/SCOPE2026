---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

PASS. For centrally symmetric ellipsoid Q=b²I+A e1e1^T+B e2e2^T, the orthogonal-shadow squared half-diameter is the top eigenvalue of compression to U-perp, equivalently b² plus top eigenvalue of T=[[A(1−U1²),−sqrt(AB)U1U2],[-sqrt(AB)U1U2,B(1−U2²)]]. Since the lower eigenvalue<=B and t in(B,A), the condition for Lambda<=t reduces exactly to A(t−B)U1²−B(A−t)U2² >= (A−t)(t−B). With S=U1²+U2²~Beta(1,(d−2)/2), independent uniform angle, angular integration gives the all-d CDF and strict monotonic decrease in d. In d=4 exponent1 integrates as an elementary arctanh term; differentiation yields tilted arcsine f_W(w)=(1−k+2kw)/(pi sqrt(w(1−w))) with valid 0<k<1, hence beta mixture weights (1−k)/2 and (1+k)/2. Fixed A>B perturbation Lambda=A−A U1²+O(U1^4+U2^4+U1²U2²) and dU1²=>chi1² imply the limit. Source verify_projection.py checks exact rational determinant identities, independent matrix eigenspectra, numerical quadratures and sampling, not replacing analytic proof.

## originality

PASS

PASS best of knowledge for exact Haar hyperplane ORTHOGONAL PROJECTION maximum-radius two-spike law and especially evaluated d=4 skew-arcsine beta mixture. Hinrichs et al arXiv:1901.06639 analyzes random SECTIONS and information recovery, not this maximum of projected quadratic form; published Resultary one-spike exact beta SECTION law also differs in rank and statistic. General random eigenvalue compression/interlacing theory may be stronger and could imply a distribution by integration, but inspected statements did not supply this two-spike explicit mixture; targeted searches under projection, shadow, spectral compression and arcsine aliases found no exact equivalent. Residual priority risk includes Dixon–Anderson/orbital eigenvalue laws.

## value

PASS

PASS. The rank-two anisotropic ellipsoid is a natural first genuinely two-spike case after the classical one-spike beta reduction. Its exact all-dimensional distribution, dimension stochastic ordering, and unexpected skew-arcsine two-beta mixture in d=4 are motivated geometric probability facts beyond trivial single-eigenvalue compression.

The dated certificate retains the supplied scientific assessment, sources and limitations.
