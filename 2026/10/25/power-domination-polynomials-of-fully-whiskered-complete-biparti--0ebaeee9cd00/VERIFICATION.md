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

The artifact `verify.py` builds \(K_{p,q}\circ K_1\) directly as a graph, applies the closed-neighborhood initial observation and subsequent unique-unobserved-neighbor forcing until no change is possible, and independently counts successful subsets by size. The graph simulator does not implement the proof's support classification. It compares the resulting coefficients to a separately coded expansion of the six terms in the theorem.

Eight instances, with \((p,q)\) equal to \((2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4)\), cover 173,312 vertex subsets. Every coefficient agreed. A further 361 parameter pairs with \(2\le p,q\le20\) were checked by exact integer polynomial arithmetic for the minimum-degree and degree-two-coefficient assertions. The recorded output terminates in `VERIFY_OK`.

Reproduce with `python3 verify.py` in any standard Python 3 environment; no third-party packages are required. The exact recorded output is in `verification_output.txt`. The verifier is a finite test, not a formal proof for unbounded \(p,q\). The infinite argument is given in `RESULT.md`.
