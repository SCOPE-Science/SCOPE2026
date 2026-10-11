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

# Verification of the equiradial-star Dudley formula

The theorem is established by the analytic proof in `RESULT.md`; there is no dependency on a finite or numerical certificate for correctness. The critical identity \(\mathrm{Lip}(f)=\rho^{-1}\sup_i|f(v_i)-f(o)|\) follows directly from the star distances. Translation invariance follows from the zero total mass. Range centering achieves the smallest supremum norm, and the remaining two-edge fractional maximization has derivatives of constant sign. Three explicit unit-ball witnesses attain the proposed values. All arguments allow countably infinite absolutely summable coefficient sequences.

A separately formulated linear program was tested for \(|I|\in\{1,2,3,5,8\}\) and \(\rho\in\{0.1,0.3,1,2,7,20\}\), with 50 pseudorandom signed coefficient families per pair (1,500 cases). Its optima agreed with the formula to within \(10^{-7}\). Reproduce with `python checks/test_star_lp.py` after installing the packages in `checks/requirements.txt`. This verifies only the sampled finite cases and cannot establish the universal or infinite assertions.

Source comparison included Hille–Theewis arXiv:2206.12234v2 Section 6 (general finite molecular linear program) and Hille–Theewis arXiv:2305.08500v1 Sections 2, 5 and 6 (general extremal-function/norming theory), with differences explained in `RESULT.md`. The older Sriperumbudur et al. empirical-computation paper was identified as relevant and remains an uninspected full-text risk.
