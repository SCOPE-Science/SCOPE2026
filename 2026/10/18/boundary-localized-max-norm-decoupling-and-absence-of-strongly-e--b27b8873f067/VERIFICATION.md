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

# Mathematical verification and limits

The primary derivation uses the centered Poisson \(L^2\) norm and exact inner-function variance. For \(h_a=b_a-a\), verify directly that \(\|h_a\|_G=1\) and \(\Phi_{h_a}(z)=1-\rho(a,z)^2\). The upper bound splits the disk into \(\rho(a,z)\le s\) and its complement, then takes \(a\to\zeta\) before \(s\uparrow1\). The lower bound for \(\|f\|_G\) holds at each fixed interior \(z\), while the lower bound for \(|t|\) is attained asymptotically at \(z=a\). The ordinary Lebesgue differentiation theorem supplies a common boundary point for \(f\) and \(|f|^2\). No interchange of a supremum with a limit is used for the lower bound.

For a symbolic check using \(f(z)=z\), \(a=r\in(0,1)\), the covariance of \(f\) and \(h_r\) under Poisson probability at \(z\) is \( -(1-r^2)(1-|z|^2)/(1-r\overline z)\). The resulting exact variance formula agrees with the maximal limit \(\|z\pm h_r\|_G\to1\). This check is illustrative; the proof covers all complex BMO functions and all fixed complex \(t\).

Completeness limits: The finding concerns the exact Poisson-variance Garsia norm on circle BMO modulo constants; it makes no claim about equivalent alternative BMO norms or ordinary extreme point classification. No independent audit or independent validation was performed. Historical priority is subject to unindexed literature.
