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

# Reproduction and limits

Execute `python verify.py` with the versions of SymPy, NumPy, and SciPy satisfying `requirements.txt`. The program checks exact symbolic factorization of the equilibrium quadratic and the mean–variance shell; it then integrates the published 2022 oscillatory example at \(R=3\), \(\mu=1\), \(K=4\), \(\zeta=19/2\) and compares cycle quadratures to five independent identities.

The proof in `RESULT.md` is exact. Numerically traced cycles cannot certify all parameter values or measures, and the output is not a rigorous enclosure of the cycle. The source establishes cycle existence in its stated parameter region. The physical root conditions and compact interior support are necessary assumptions for the strong prevalence comparison; the theorem does not cover boundary-supported stationary distributions.

The performed computational checks passed with residuals below \(6\times10^{-12}\) in the example; double precision is not claimed as a mathematical certificate. Independent audit: not performed.
