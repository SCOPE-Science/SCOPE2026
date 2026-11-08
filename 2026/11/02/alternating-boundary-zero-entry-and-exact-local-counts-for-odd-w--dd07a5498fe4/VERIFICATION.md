---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

With m=4k and alpha=m-2, beta-moment monomial norms give K=H_{m,beta}(s)/(1-s)^m, and odd numerator F=(1+s)^m H(s)-(1-s)^m H(-s). At beta=0, finite simple roots are s=i tan(pi j/m), with exactly 2k-1 strictly interior and the two critical ±i on |s|=1. Differentiation of the numerator at (0,i) gives s_+'(0)=2i S_{4k}/m, where S_{4k}=sum_{j<k}(-4)^j[1/(4j+1)+2/(4j+2)+2/(4j+3)]. Positive block magnitudes 4^j A_j strictly increase, including j=0→1, so the alternating sum has sign (-1)^(k-1) for all k; root continuity proves inward/outward crossing and exact disk count 2k+(-1)^(k-1) for sufficiently small beta<0. Independently recomputed S_{4k} with Fraction arithmetic for k=1..8, including slope -16/105 for k=2. The origin is a numerator zero, not an attainable nonzero scalar for two punctured-disk points; count of fibers is one less. Finite checks do not prove the infinite sign law.

## originality

PASS

Qualified PASS: Ghiloufi–Snoun establish the rational odd kernel and unperturbed roots but exclude precisely alpha≡2 mod4 critical cases with ±i boundary zeros. Their η>1 enlarged-disk statement does not imply the unscaled η=1 count. The explicit analytic transversality and alternating inward/outward family supplies a negative answer for even k and a complete local count. Further priority risk from subsequent meromorphic-kernel or zero-crossing literature.

## value

PASS

The critical boundary case arises intrinsically because odd kernel roots sit exactly at ±i when m divisible by four; continuity alone cannot decide inclusion. Resolving direction for the entire infinite congruence family answers a specific near-endpoint question in an existing theorem and supplies infinitely many concrete counterexamples to an attractive stronger η=1 inclusion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
