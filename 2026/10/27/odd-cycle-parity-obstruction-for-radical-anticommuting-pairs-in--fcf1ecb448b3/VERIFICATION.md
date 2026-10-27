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

# Reproducibility and limits
Execute `python3 check_pair_census.py` using Python 3.8 or newer; no third-party package is required. The checker independently (a) lists directed composable arrow pairs, (b) enumerates all \(q^{2|E|}\) first-layer pairs for each selected quiver and field, (c) tests each path coefficient of both \(xy-yx\) and \(xy+yx\), and (d) compares the result, after the free length-two factor \(q^{2p}\), against the graph-support formulas. It checks 22 field/quiver configurations, including loops, parallel arrows, oriented and acyclic odd-transition cycles, and the nonprime field \(\mathbb F_4\). It also verifies the closed odd-cycle deficit expressions for odd field sizes three and five.

Observed completion marker: `QUIVER_ANTICOMMUTING_PARITY_OK 22 direct exhaustive cases; two algebraic odd-cycle checks`.

The code tests finitely many coefficient assignments; general field sizes and quivers are covered only by the mathematical proof. It does not check absolute publication priority or constitute independent validation.
