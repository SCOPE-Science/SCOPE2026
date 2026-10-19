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

Run `python verify.py` with Python 3's standard-library decimal module. It directly constructs truncated Parry-series weights and integrates the step densities to obtain invariant means and total-variation probabilities. Calculations cover bases \(b\in\{2,3,5\}\) and deficits \(arepsilon\in\{10^{-5},10^{-10},10^{-20},10^{-35}\}\). The checker prints normalized quantities and `VERIFY_OK` only after consistency and approach-to-limit assertions succeed.

The analytic proof is independent of finite numerical evidence: (i) the explicit transfer operator gives the invariant Parry series; (ii) a maximal-digit cutoff at \(m_eta\) controls the leading log deficit; (iii) the remaining orbit tail is geometrically small; (iv) the defect concentrates at the right endpoint; (v) the positive-part formula determines the exact total variation. Finite precision and truncated sums cannot certify the limiting theorem; all nonstandard limit estimates are derived in RESULT.md. Reproducibility requires only this package and a Python 3 interpreter.

The classical density formula is prior work. The source-access restriction concerning the 2007 generalized-beta paper leaves a nonzero historical-priority risk. No independent review has been performed.
