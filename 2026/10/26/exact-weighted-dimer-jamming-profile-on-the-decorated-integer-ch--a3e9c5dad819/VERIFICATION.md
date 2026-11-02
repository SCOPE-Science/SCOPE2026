---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

Reconstructed independent first-arrival competition on the acyclic decorated path. The one-sided failure F_l obeys F_l(t)=1-α∫_0^t exp[-(α+β)s]F_(l-1)(s)ds and F_0=1, so with x=g(1-e^(-(α+β)t)) gives F_l=Σ_{j=0}^l(-x)^j/j!. Integrating βe^-βt F_(i-1)F_(L-i) and beta factorial identity a B(j+k+1,a)=(j+k)!/∏_{h=1}^{j+k}(a+h) proves the exact finite sum. Alternating-series remainder on 0≤gu≤1 bounds each branch by (gu)^ell+1/(ell+1)!, giving the printed two-side factorial bound; dominated convergence yields the bulk confluent hypergeometric integral. Coupling/exponential representation in ratio b=β/α gives strict increase, limit e^-2 as b↓0, strong-b 1-1/b+O(b^-2), and t=u/β limit e^-2(1-e^-u), distinct from exactly β=0. Independently exact CTMC first-success recursion reproduced 84 cases (L<=6, three rate pairs, every site). Local infinite-volume influence paths are factorially suppressed on bounded-degree graph. No infinite claim inferred from the finite tests.

## originality

PASS

Qualified PASS: Penrose–Sudbury 2005 arXiv:math/0503519 develops general deposition/annihilation on bounded-degree graphs and explicit regular Bethe-tree results; its examined graph formulas do not evaluate separately weighted pendant and spine edges of the nonregular comb. Evans 1984 regular Cayley/Bethe trees and Evans–Nord 1992 infinite two-rail ladders differ in geometry and rates. Gouet–Sudbury 2008 full text was inaccessible and may contain a relevant specialized tree law; retain this risk.

## value

PASS

Weighted dimer RSA on a decorated path is a natural exactly soluble nonregular tree substrate: finite-site occupation, factorial boundary correction, sharp rate response and singular slow-pendant time scale are useful for comparing local versus bulk jamming and discontinuous zero-rate limits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
