---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The published Knockoff+ threshold becomes \(P_k-rN_k\ge r\) at \(q=1/r\). Under the exact conditional sign-flip property this is a skip-free random walk with increments \(+1\) and \(-r\), each with probability one half, and selection is exactly first hitting level \(r\). The one-level defective generating function satisfies \(F(z)=z(1+F(z)^{r+1})/2\); strong Markov factorization gives \(F(z)^r\), and Lagrange inversion yields the submitted coefficients. A fresh exact-rational replay independently matched the closed sum to dynamic programming for multiple \(r\) and horizons and reproduced the displayed \(r=2\) and \(r=10\) limits.

## originality

PASS

The foundational knockoff paper gives iid fair null signs and the generic finite-sample FDR guarantee, while later work on whether the '+1' correction is needed studies validity under broader competition configurations. Neither inspected primary source states the complete-null reciprocal-level hitting distribution, its Fuss-Catalan finite formula, or the limiting algebraic root. Targeted Resultary and web searches did not locate an equivalent procedure-specific law. The classical ballot/Lagrange machinery itself is not claimed as new.

## value

PASS

The result gives an exact finite-sample and asymptotic calibration baseline for a widely used FDR procedure and quantifies how far the attained global-null error can sit below the nominal guarantee. The reciprocal-level staircase and explicit \(q=0.1\) limit are natural diagnostic quantities for theory and implementation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
