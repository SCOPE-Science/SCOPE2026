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

`verify.py` runs using Python 3 with only standard-library modules. It independently enumerates every nonempty triple \((A,B,C)\) satisfying the all-to-all arcs defining the regular CW cells for each odd target order \(3,5,\ldots,19\). It compares each cellular count against the theorem's binomial polynomial and separately against the six-parameter weighted sum. For orders up to 15 it explicitly constructs the unique cyclic anchor for every cell and tests every nonidentity target rotation for nonstabilization. Both independent count methods and every anchor and rotation test pass; `verify_output.txt` records exact counts and the terminal success marker.

The proof's all-order quantifier relies on the parameter bijection and generating-function algebra in `RESULT.md`, not on finite extrapolation. The verifier does not compute homotopy groups, prove circle homotopy, or make claims about quotient regularity. Independent audit has not been performed.
