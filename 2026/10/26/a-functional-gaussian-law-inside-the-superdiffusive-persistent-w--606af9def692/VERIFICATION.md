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

# Verification and scope

The published model's flip regression was independently reconstructed from its two-state transition law. The proof uses exact conditional moments \(\mathbb E[\eta_k\mid\mathcal F_{k-1}]=0\) and \(\mathbb E[\eta_k^2\mid\mathcal F_{k-1}]=4p_k(1-p_k)\), followed by the deterministic bracket and Lindeberg bounds. Abel summation supplies an exact pathwise displacement–martingale error bounded by \(2+n^\alpha/c\). For \(\alpha\in(0,1)\), this bound divided by \(n^{(1+\alpha)/2}\) vanishes. These are symbolic analytic checks rather than machine enumeration; no external computational artifacts are required. The process-level limit additionally invokes the classical martingale functional central limit theorem. Independent audit has not been performed. Literature completeness and generality beyond the stated parameter range have not been independently certified.
