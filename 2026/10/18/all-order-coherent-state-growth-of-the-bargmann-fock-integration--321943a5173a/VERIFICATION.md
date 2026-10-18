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

# Analytic verification and limits

The standard Bargmann–Fock basis gives \(J\phi_j=\phi_{j+1}/\sqrt{j+1}\) and \(\|J^k\|=1/\sqrt{k!}\). The normalized resolvent column identity is exact for every \(j\) and every \(t>0\); no truncation is required. The coherent state has norm exactly one.

A direct Poisson mean-variance computation and weighted Cauchy–Schwarz establish a uniform bound for \(e^{-t^2/2}\sum_{n\ge0}t^n/\sqrt{n!}\), allowing the operator-norm tail estimate \(O_m(t^{-m+1/2})\). The required fixed-order expansion follows by choosing \(m=2N+3\) and estimating the omitted finite factorial terms. The radius formula follows by inversion of the exact resolvent relation and the first coefficients of the proven expansion.

Run `python checker.py` with NumPy and SciPy installed to reproduce 51 finite tests of the resolvent matrix, finite-section norms, tail estimate and Poisson bound. The checker does not prove the infinite-dimensional estimate or the asymptotic error; its diagnostics are strictly supporting evidence. An independent audit or publication-priority verification has not been performed.
