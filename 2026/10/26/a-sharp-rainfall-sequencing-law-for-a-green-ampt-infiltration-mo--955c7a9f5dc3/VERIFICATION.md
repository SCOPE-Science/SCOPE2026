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

# Computational and analytic verification

The analytical proof uses a high-intensity time change, a monotone low-to-high speed ratio, an exact flow derivative, and adjacent-interchange plus \(L^1\) continuity. Its quantifiers cover all bounded nonnegative measurable rates over a finite horizon. The strictness criterion is only for two strictly positive distinct rates of strictly positive durations; its equality surfaces are included.

Run `python3 infiltration_order_checker.py` to reproduce deterministic checks. This script solves each constant-rate segment using the Green–Ampt primitive \(H(F)=F-B\log(1+F/B)\), whose derivative is \(F/(F+B)>0\) for positive \(F\), and interval bisection. The capacity threshold is handled analytically, with no explicit time-step approximation. A deterministic seed of 1978 drives 3000 random tests. All 3000 satisfied the weak order, and all tests flagged as exact equalities passed numerical tolerance. Three constructed equalities were also checked.

For \(K=B=1\), \(F_0=0.25\), rate pair \((\ell,h)=(1.5,3)\), and both durations \(0.2\), the script printed final states \(F_{HL}=1.097721698953\), \(F_{LH}=1.009760758368\), with difference \(0.087960940585\). The exact strictness cutoffs are \(F_h=0.5\), \(F_\ell=2\), and the available rainfall reaches beyond the high-rate cutoff.

These finite checks are not a proof for arbitrary measurable hyetographs. The independent audit has not been performed; neither its status nor its evidence is inferred from the above calculations.
