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

# Verification
Run `python3 verify.py` from the directory containing this document and the companion standalone checker. This program independently constructs each matching-deleted complete bipartite graph, simulates three-colour forcing to closure, checks final colouring properness, and enumerates initial assignments of size at most three for every \(4\le n\le7\) and \(1\le t\le n\). It tests both classification directions and the count \(12t(n-1)\). It also exhaustively excludes forcing assignments of fewer than \(n\) seeds for intact \(K_{n,n}\) at \(n=4,5,6\), and checks constructive seeds of size \(n\). Observed checker output: `ALL CHECKS PASSED; partial assignments tested: 401389`.

These finite tests do not certify the claims for arbitrary \(n\). The unrestricted proof, exact parameter quantifiers, and critical first-step logic are in RESULT.md. Mathematical review of correctness, originality and value is recorded separately; an independent audit has not been performed.
