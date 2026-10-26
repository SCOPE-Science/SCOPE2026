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

# Reproduction of exact finite certificate

Run `python3 verify.py` from a directory containing the enclosed files. Python's standard library suffices. The standalone program generates all local center-column configurations from the original \(\{-1,1,2,3\}\) conditions, verifies the equivalence of the equality predicate with feasibility and discharge equalities, and builds the 256-state directed transfer graph without tables of undocumented constants.

It computes all strongly connected components, confirms that only components of sizes \(22,4,4,4,2\) carry cycles, and constructs the 22-by-22 core adjacency matrix. An integer Newton-identity implementation computes every coefficient of its characteristic polynomial, checking exactly \(t^{14}(t^8-7t^4+1)\). The other four cyclic components are checked directly. It separately counts unrestricted optimal configurations for orders \(4,6,8\) by a min-cost transfer, brute-forces the 4-prism, and compares recurrent transfer traces against the claimed formula at twelve even orders through \(40\).

A successful execution prints the five `*_OK` lines included in `verification_output.txt`. These computations certify the stated finite matrix identities, not the independent validity of the code or a bibliographic uniqueness assertion. The proof of the all-order conclusion is in `RESULT.md`. No external independent audit has been performed.
