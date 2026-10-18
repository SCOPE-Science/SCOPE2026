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
Compile `verify.cpp` using a C++17 compiler and execute it. The program independently constructs every pair of vertices, tests the exact induced-two-edge-path obstruction, enumerates all vertex subsets of the five small direct products (\(4\times3\), \(4\times4\), \(4\times5\), \(5\times3\), \(5\times4\)), and compares every polynomial coefficient against the stated formula. There are \(4096+65536+1048576+32768+1048576=2199552\) subsets, counted including the empty set. It also checks small-width unimodality through \(r=50\) using exact machine integers (within verified integer ranges).

Run `python3 verify_modal.py` for arbitrary-precision checks of all sizes \(3\le r\le500\) at widths \(4\) and \(5\), the corresponding adjacent-difference identities and eight transition boundary configurations. The logged output files `verification_graph_output.txt` and `verification_modal_output.txt` record actual successful executions of these exact programs.

# Mathematical scope of the certificate
Finite exhaustive checks do not prove the unrestricted result. The proof in `RESULT.md` establishes inequalities for all integer \(r\ge3\), including the endpoint cases, and its only nontrivial structural premise is the complete list of possible general-position subset patterns in this diameter-two family, proved there directly. No external independent scientific validation has been performed.
