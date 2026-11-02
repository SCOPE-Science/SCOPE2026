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

# Verification details

The static claim and all formulae were checked by an analytic proof reconstructing run-length necessity and sufficiency, the marked-run composition factor, and the six-state transfer matrix with a primitive Perron root.

`CHECKER.py` depends only on the Python standard library. Running `python3 CHECKER.py` prints `PASS 134474 assertions`. It independently enumerates every binary word of lengths 5 through 16, tests the local four-neighbor satisfaction rule, compares the complete population-resolved count with the formula, and verifies every allowed run pattern. It also compares matrix traces and closed counts through length 50, and checks the polynomial matrix identity \(T^6-2T^5+T^4-I=0\).

The exhaustive verification is confined to the explicitly tested lengths. The proof of the statement for all \(n\ge5\) does not rely on extrapolation from a finite computation.

Literature comparisons distinguish the new enumeration from known sufficient long-run fixed-point structures and from results about dynamical absorption. Historical priority and independent validation remain unperformed.
