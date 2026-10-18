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

The attached `verify.py` exhaustively enumerates the row sequences of 1–3 attributes and 0–4 objects, integrates the full symmetric Dirichlet law by exact rational rising factorials, and checks all formal closures directly. The result is `VERIFY_OK exact_cases=45 contexts=15159`. This verifies the finite exact identity and coatom reduction for the tested cases, not the infinite-dimensional limits, which follow from beta asymptotics and elementary concentration in the proof.

Critical analytic checks: the Dirichlet marginal of the size-\(m-1\) category is \(\mathrm{Beta}(\beta_m/(m+1),m\beta_m/(m+1))\); conditional on that category mass the coatom types each have probability \(R_m/m\); the beta negative first moment is finite exactly when its first shape exceeds one; when \(\beta_m=m+1\), \(mR_m\) converges to a unit-rate exponential; when \(\beta_m=\beta\) is fixed, \(-\log R_m/m\) has an exponential limit. Uniform conditional coupon bounds transfer these facts to the stopping time.

The prior coin-toss coupon-collector criterion and the Dirichlet model itself are not newly asserted. Model precision differs in the two asymptotic regimes. Full-text comparison with one later paper about random concept counting remains unresolved; no claim of external independent validation is made.
