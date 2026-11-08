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

The normalized basis e_n=sqrt(n+1)z^n gives A_nm=2sqrt((n+1)(m+1))/((n+m+1)(n+m+2)) for n+m even, zero otherwise. Weighted Schur row ratios for n>=1, w_n=(n+1)^(-1/2), are bounded strictly below1 by (n+1)log((n+2)/(n+1)) (odd) or (n+1)log((n+3)/(n+2)) (even); hence no nonzero equality in the compressed subspace. A00=1 and A02=sqrt3/6 show a 2x2 compression eigenvalue 3/5+sqrt219/30>1. The coupling vector has norm squared 4log2-1-pi²/6 by partial fractions; the compact rank-two coupling bounds the norm and essential spectrum. A normalized even-degree vector supported on 2i for i=M..M² has Rayleigh quotient tending1, weak limit zero, proving essential norm >=1 (while the compression/coupling gives <=1). The codimension-one variational argument forces exactly one simple eigenvalue above1. Independently checked b² partial sums and M=8,16,32,64 Rayleigh ratios, and analytic constants; finite checks do not substitute for the Weyl-sequence proof.

## originality

PASS

Best-of-knowledge originality from actual published mathematical searches and inspected primary scientific material; relevant exact known cases and stronger-coverage risks are compared, not merely title-matched. No directly implication-equivalent theorem identified in inspected statements; not a historical priority guarantee.

## value

PASS

A sharp spectral dichotomy for a natural diameter trace: the constant mode creates one genuinely isolated supercontractive direction while all mean-zero-at-origin analytic functions have a sharp unattained bound and the remaining essential spectrum reaches exactly1. This is nontrivial infinite-dimensional operator structure, not merely a routine finite truncation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
