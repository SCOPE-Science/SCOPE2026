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

# Verification of the stated finite remanent language results

Run `python3 verify.py` in a directory containing this file and `verify.py`. The entire verification program uses Python's standard library; `checks.txt` contains the exact output of an actual execution.

The program constructs the \(2^n\) orientations explicitly for each \(n\in\{3,5,7,9\}\), computes all signed subset transitions by bitmask union, determinizes their intersection with an absorbing empty-component dead state, and enumerates all reachable states. Partition refinement begins from acceptance and stops only when no further block split is possible. A separate assertion checks that output and both quotient transitions are invariant on every equivalence class.

It then checks all three strictness witnesses against every lower-cycle orientation and supplies one rejecting mask for the next cycle. Recorded exact pairs of reachable states and minimal DFA classes are \((6,6)\), \((24,18)\), \((230,102)\), and \((8936,1098)\).

The general language-inclusion statement is proved mathematically by an explicit graph homomorphism in `RESULT.md`. The verifier does not establish a closed formula for cycle orders beyond nine. No independent scientific audit has been performed.
