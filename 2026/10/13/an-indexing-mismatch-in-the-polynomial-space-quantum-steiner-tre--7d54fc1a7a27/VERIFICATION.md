---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Proof 4 of arXiv:2510.09911v1 prints the bottom-level amplitude product and evaluates its exponent using the top-level geometric sum. For k=2^m, r=m-j gives the factors binom(2^(r+1),2^r), 0<=r<ell, and the actual sum is 2^ell-1. The substituted value k(1-2^(-ell)) is strictly larger for ell<m and equal for ell=m. Thus the printed equality is false in general, although the larger expression can still be used as a loose upper bound. At fixed ell, the amplitude logarithm is constant, Stirling gives kH(2^(-ell))+o(k), and the classical-plus-encoding term contributes k*2^(-ell)*log C+o(k). With s=2^ell, the bounds log binom(k,k/s)<=(k/s)log(es) and log T_aa<=(s-1)log 2 yield the claimed logarithmic cost at a dyadic s comparable to sqrt(k log k), which is admissible for large dyadic k. This checks the literal printed cost model, not the complete algorithm or failure of its published upper bound. Verification is analytic; the frozen script and notes were inspected, not executed.

## originality

PASS

The checked earlier top-level analysis supplies the structurally related product but not the diagnosis of the later displayed equation or the asymptotics of its literal bottom-level model. Bounded catalogue and literature checks did not supply a covering correction or equivalent statement.

## value

PASS

This is not just a typo report: it diagnoses which recursion levels make the amplification cost exponential at fixed depth and quantifies the qualitatively different tradeoff forced by the printed model at growing depth. That distinction matters to readers reconstructing the polynomial-space algorithm. Neither the finding nor this assessment claims a subexponential implementation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
