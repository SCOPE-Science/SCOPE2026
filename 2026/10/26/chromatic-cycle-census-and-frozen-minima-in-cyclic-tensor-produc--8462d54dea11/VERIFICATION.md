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

The standalone program `checker.py` uses no external packages. Run `python checker.py`.

The program checks the formula and absence of token-jump pairs for the seven parameter pairs \((k,q)=(2,3),(2,4),(2,5),(3,3),(3,4),(4,3),(5,3)\). For the three cases \((2,3),(2,4),(3,3)\), a separate exhaustive checker constructs the original graph and scans **every** vertex subset of size at most \(2k\), verifying independence and domination from adjacency. The two independently generated minimum-set collections coincide in those cases.

The finite verifier does not establish correctness for infinitely many \(k,q\); the mathematical proof in RESULT.md is the general argument. The ordinary independent domination number and the general fiber-label framework have published antecedents; novelty and priority still require independent literature assessment.
