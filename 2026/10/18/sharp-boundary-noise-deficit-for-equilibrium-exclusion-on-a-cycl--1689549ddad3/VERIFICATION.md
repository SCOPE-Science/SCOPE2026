---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

For all n>=3, 1<=k,m<n and r>0 the cyclic discrete Poisson equation has periodic increments d_i in (2); the lifted U=sum u_i eta_i/r satisfies -mathcal L U=N_B-km/n for the FULL interacting exclusion generator because exchange exclusion terms cancel on a linear occupation functional. The stationary finite-state martingale M_t=A_t+U(eta_t)-U(eta_0) has predictable bond bracket 2k(n-k)d_i^2/[r n(n-1)] per time, by the hypergeometric adjacent disagreement probability. The bounded corrector contributes o(t) to integrated variance. Squared-gradient identity sum d_i^2=m(n-m)[m(n-m)+2]/(12n) yields exact variance, and strict gradient dominance of two boundary bonds gives the fraction 6m(n-m)/[n(m(n-m)+2)], all-K selection upper bound, n>=12 sharp half-variance cutoff and correlation time. Independent direct construction/inversion of the 10-state full configuration generator for n=5,k=2,m=2,r=3 yielded 0.16, agreeing with the formula; source script independently inspects 94 full SSEP finite systems. The checked finite systems alone cannot prove all n.

## originality

PASS

Best-of-knowledge original contribution is the exactly evaluated finite interacting canonical-density SSEP noise-budget formula and sharp n=12 geometry, NOT stochastic shielding, OU graph edge importance, general martingale resolvents, or instances where hidden edges dominate (all known).

## value

PASS

A contiguous block in equilibrium lattice-gas SSEP is a natural local transport observable, and bond-wise variance allocation determines principled coarse-graining noise budgets. Exact density independence despite interactions and the sharp universal 12-site half-variance failure are structural and practically meaningful: the locally strongest two sources capture a vanishing share as the ring grows. This is more than re-evaluating a known variance because the exact optimal-source spectrum and geometric cutoff are proven for every particle number.

The dated certificate retains the supplied scientific assessment, sources and limitations.
