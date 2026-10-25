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

# Reproduction

Run `python verify.py` in a Python 3 environment; no third-party packages are used.

The script checks dihedral normal-form group products against the explicit Parikh criterion for \(4{,}445\) triples \((n,x,y)\); for each \(2\le n\le30\), it constructs the claimed reachable quotient automaton, computes exactly which state pairs have different right languages by backwards reachability, and counts equivalence classes with a separate union-find procedure. It independently tests \(11{,}747\) binary words by direct DFA execution. The recorded outcome from the packaged verifier is `VERIFY_OK: 4445 independent group-count cases; 11747 complete word/automaton checks; n=2..30`.

The checker tests only the indicated finite instances. The general assertion relies on the complete symbolic proof in `RESULT.md`, particularly the existence and distinctness of each Myhill–Nerode quotient class. No external auditing or formal proof certification is asserted.
