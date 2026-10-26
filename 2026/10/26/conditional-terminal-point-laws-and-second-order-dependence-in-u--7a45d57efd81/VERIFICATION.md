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

# Verification record

The self-contained standard-library `verify.py` was executed with `python3 verify.py` using the exact file packaged with this mathematical claim. It exhaustively traverses all functions \([n]\to[n]\) for integer sizes \(2\le n\le7\); every mapping contributes to its actual cyclic count and indegree-zero count. Rational arithmetic checks the normalized cyclic marginal \(k(n)_{\underline k}/n^{k+1}\), each conditional falling-factorial moment, the terminal-deletion covariance identity, and strict negative sign. Mapping counts are \(4,27,256,3125,46656,823543\) for those successive sizes. The program also performs numerical asymptotic diagnostics at \(n=200,1000,10000,60000\), comparing scaled covariance and correlation with \(-\sqrt{\pi/2}/(2e)\) and its stated correlation coefficient. Its final output is `VERIFY_OK`.

The finite exhaustive check is complete only for the six stated sample sizes. Floating-point limits are diagnostics, not an infinite proof. The unrestricted claims require the combinatorial enumeration, monotonic regression, Gaussian-tail bound, and second-order limiting calculations given in `RESULT.md`. No independent audit has been performed.
