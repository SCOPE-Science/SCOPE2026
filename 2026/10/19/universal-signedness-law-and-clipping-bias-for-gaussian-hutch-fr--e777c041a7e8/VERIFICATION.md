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

Reassessed repairs/3/RESULT.md. In the singular-value basis the squared-norm terms each converge to 1 in L² with variance 2/(rR_j). The vectorized Gaussian cross term has covariance I_(r²); its fourth norm moment sum is E(||X||⁴||Y||⁴)/R_j, so multivariate Lyapunov applies at fixed r even with changing dimensions. This yields 2-chi²_(r²)/r² and gives sign convergence at the continuity point zero. From H-F=-tr(L A M A^T) for the independent centered Wisharts, conditioning and the diagonal/off-diagonal variances give exactly 2(F²+tr((A^TA)²))/r². This yields the uniform integrability needed for clipping, followed by x f_k=k f_(k+2). The repaired tail proof after rescaling u=2+t/k is dominated by exp(-t/4)/2, yielding (pi k)^(-1/2)exp(-k I(2)), k=r². The removed stand-alone rank-one result was not false: in the original proof the saddle is at u=2 with J''(2)=3/4 and prefactor 1/(4pi); the complementary integral is exponentially smaller by the gamma Chernoff bound and coercivity. It remains a credited comparison only. The uploaded script was inspected, not run; its finite Monte Carlo tests cannot certify either asymptotic regime.

## originality

PASS

Narrowed the originality claim in repairs/3/RESULT.md to the high-effective-rank signed law and clipping bias, with the q_r tail as a chi-square consequence. The original stand-alone rank-one law and sharp tail have exact coverage in the weighted Resultary result at alpha=1; its catalogue date does not settle historical priority. The corrected file treats this only as credited context. The compared estimator and probability papers do not supply the high-effective-rank Hutch# signed/clipped limit.

## value

PASS

The repaired theorem identifies a non-Gaussian signed limit for a natural unbiased estimator of a nonnegative target, uniformly in the sense of arbitrary sequences satisfying the effective-rank condition. It gives the exact upward penalty of the practical clipping operation and shows this cost persists even as spectral concentration vanishes at fixed budget. Neither the variance alone nor qualitative sign failure gives this information; the claim is worthwhile without relying on the overlapping rank-one result.

The dated certificate retains the supplied scientific assessment, sources and limitations.
