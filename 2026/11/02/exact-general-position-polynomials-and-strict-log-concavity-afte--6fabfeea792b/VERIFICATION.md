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

# Reproducible mathematical checks

Execute \(`python3 verify.py`\) with Python 3.10 or later; the expected final marker is \(`VERIFY_OK`\). All arithmetic for polynomial coefficients, root-free inequality checks, and strict log-concavity slacks uses exact Python integers. No third-party dependencies or downloaded data are required.

Every path/cycle component multiset with total order \(5\) through \(13\) is enumerated once. The counts by order are \(11,19,29,46,70,106,156,232,334\), totaling \(1003\). The minimum positive log-concavity slacks are \(15,21,28,36,45,55,66,78,91\). For all 175 types of orders \(5\) through \(9\), a separate graph-distance routine independently counts general-position sets and checks the complete polynomial. Additional nonexhaustive stress tests cover orders up to \(100\).

Finite enumeration proves the nine bounded orders only. The argument for every \(n\ge14\) is an ordinary mathematical proof from a complete induced-subgraph classification, the negative-real-rooted path/cycle independence polynomials, Newton's inequalities, and explicit uniform independent-set coefficient bounds; it does not depend on extrapolating numerical experiments. Independent mathematical auditing has not been performed. Publication priority remains subject to possible unindexed or unnoticed stronger literature.
