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

# Reproducibility of bipartite exclusion activity formulas

With Python and SymPy installed according to `verification/requirements.txt`, execute `python verification/verify.py` from the directory containing this file. The script builds the **full** finite configuration space (rather than assuming a one-dimensional reduction), inserts an off-diagonal transition for every occupied--vacant bipartite edge, solves the finite-state counting Poisson equation with exact rational arithmetic, and compares the resulting first two jump-count cumulants with the claimed formulas. It covers 59 triples \((a,b,k)\) with both part sizes in \(\{1,2,3,4\}\), total size at least four, and all strictly intermediate particle inventories.

A separate symbolic calculation reconstructs the variance of the orthogonal degree-two hypergeometric mode from factorial moments up to order four and checks exact equality with the theorem's rational factorization for symbolic parameters. Five further integer examples verify that the predicted joint balance coefficient is numerically approached by increasing graph sizes; these finite examples are illustrative, not an asymptotic proof. The exact full-state comparisons succeeded and the symbolic identity check succeeded in the packaged run.

The code is fully deterministic, uses no network or external data, and requires only the listed dependency. The arbitrary-parameter result follows from the analytic generator and moment calculation in `RESULT.md`; finite experiments alone do not certify arbitrary graph sizes. Nothing here is an independent audit, and an independent verification of historical originality has not been performed.
