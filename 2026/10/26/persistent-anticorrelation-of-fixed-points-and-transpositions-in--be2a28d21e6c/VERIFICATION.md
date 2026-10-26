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
# Verification record

Run the standalone program with Python 3 using `python3 verify.py`. It depends only on the Python standard library and executes an independent exact-state recursion for \(n=5,6,7\), checks 1,085 exact dimension/eigenvalue/sign assertions over the declared finite grid, and verifies the rational counterexample \(6/25\). The saved console output is in `checks.txt`.

The proof of the infinite assertion depends on the remove/add branching rule, the transposition character-ratio identity, and strict convexity; no finite check certifies all \(n,t\). No external or independent audit was performed.
