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
# Verification

The claim is proved analytically in `RESULT.md`. `verify.py` performs exact-rational bookkeeping checks only.

Verified steps: the source logistic functions imply \(Y_A\le y_1/2+y_2\) and \(Y_J\ge y_1/2\); integrating the renewal PDE gives the total-predator balance; the cross coefficients in \(V'=x'+cy'\) are \(s+c(k-g)/2\) and \(-b+ck\); their joint nonpositivity is feasible exactly under \(g>k\) and \(2sk\le b(g-k)\); then \(V'\le\max\{r,\|\widetilde B\|_\infty\}V\). The source's local-Lipschitz construction and compact finite-horizon age support permit continuation while this norm stays finite.

Unproved limits: no uniform long-time boundedness, persistence, extinction, attractor classification, or blow-up claim outside the displayed region is asserted.
