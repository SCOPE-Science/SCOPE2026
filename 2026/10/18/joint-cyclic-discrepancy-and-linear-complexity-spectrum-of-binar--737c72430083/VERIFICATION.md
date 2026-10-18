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

# Reproducibility

Run `python3 verify_joint.py` with Python 3.8 or newer and the two accompanying Python source files in the same directory. There are no additional dependencies. The first method visits all 65536 nonsingular feedback tables; the second traverses every rooted Euler tour of the order-four binary de Bruijn directed graph. Both methods require only a small finite amount of memory.

The first method calculates cyclic discrepancy from balanced prefix-range identities and linear complexity by repeated division of the binary sequence polynomial by `1+X`. The second directly enumerates every cyclic factor and uses a Berlekamp–Massey recurrence on two repeated periods. The driver checks every reference cell including zeros, both totals, and the joint optimum count 92. Neither method assumes any unverified experimental reduction beyond proved bijections.

The mathematical result is finite (order five). The supplied exhaustive enumerations do not prove generalizations to larger orders. The scientific literature comparison in the accompanying review is not a proof of publication priority. Independent audit has not been performed.
