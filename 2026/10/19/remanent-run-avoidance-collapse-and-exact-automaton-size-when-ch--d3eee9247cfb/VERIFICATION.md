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

# Verification notes

The mathematical proof does not depend on a finite enumeration. For reproduction with Python 3, run `python3 verify.py` in the directory containing `verify.py` and compare with `checker-output.txt`. The checker implements the oriented-walk semantics directly and does not call the claimed symbolic theorem as an oracle. It exhaustively inspects all orientations of the seven explicitly defined test graphs and independently minimizes the proposed deterministic automata for the tested parameters.

The program checks all binary sign words through length 11 against transitive tournaments for 1 <= k <= 11; all words through length 8 against every orientation of each test graph; all words through length 10 against the explicit deterministic automata; and enumeration through length 12 for 1 <= k <= 8. It checks the explicit C5 orientation rejecting `++-++` while the transitive tournament of order three accepts it.

These are finite cross-checks of premises, conventions, and boundary examples. They do not certify the infinite argument or independently establish historical originality. No independent audit has been performed.
