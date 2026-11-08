---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

Decomposition AW=WT+UF and independent Gaussian blocks gives G^{-1}HF. Conditional on all but the ith Gaussian column of G, each error entry is ||f_j|| times the ratio of independent complex N(0,1) variables. The ratio density is 1/[π(1+|z|^2)^2]; a real component has CDF [1+x/sqrt(1+x²)]/2. The transformed median-of-three component is 3(1-u²)du/4 and has variance 1/2; summing real and imaginary component variances yields one per entry. No independence across different entries is assumed. For the m+1-row sketch, the two-dimensional Schur complement is Gamma(2,1) and E inverse is 1, yielding expected trace m. Direct independent symbolic rational calculation checks the median moment. If E=0, all errors vanish; otherwise the square ratio has logarithmically divergent second moment.

## originality

PASS

The identical exact compression-matrix risk under median robustification versus one extra Gaussian row is not the previously established generic sketched Ritz stability or the classical stand-alone Gaussian ratio moment.

## value

PASS

The natural square Gaussian Ritz sketch has infinite Frobenius risk; a minimal three-replicate median restores finite risk and exactly matches one extra least-squares row. Exact efficiency/robustness benchmark of practical numerical linear algebra relevance, with explicit cost caveat.

The dated certificate retains the supplied scientific assessment, sources and limitations.
