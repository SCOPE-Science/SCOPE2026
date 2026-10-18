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

# Verification scope

**Analytic checks.** Normalization is the beta-integral identity \(m_n=\Gamma(n+1)\Gamma(\alpha+2)/\Gamma(n+\alpha+2)\), and the cross block is exactly the outer product of its stated vectors. The full generating-function evaluation is \(S_\alpha(r)=(1-r^2)^{-(\alpha+2)}\). The residual analytic/co-analytic blocks are bounded by \(C_\alpha\sum_{k\ge1}r^{k-1}(k+1)^{(\alpha+1)/2}\), which is lower order for \(\alpha>-1\). Spectral lower and upper bounds independently give the exact exterior value.

**Reproducibility.** The companion `check.py` is a deterministic finite-section diagnostic requiring NumPy and SciPy. It tests \(\alpha\in\{-1/2,0,2\}\) and three radii, numerically checks rank one and its closed-form norm, and compares finite-section full norms. Exact analytic proofs are in RESULT.md; finite tests do not prove uniform-in-dimension or boundary-limit statements.

**Limits.** The full motivating preprint and two older likely relevant articles were not accessible in full; their abstract-level comparisons do not establish exhaustive publication priority. No independent audit has been performed.
