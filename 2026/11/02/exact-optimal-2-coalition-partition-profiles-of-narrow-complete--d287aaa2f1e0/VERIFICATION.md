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

# Reproducible checks and limits

The accompanying `coalition_template_verifier.py` uses only the standard Python 3 library. Execute `python3 coalition_template_verifier.py` in the directory containing this file and the script. The checker independently computes 2-domination from part occupancies, exhausts all unordered multisets of nonsingleton blocks with fixed excess \(s-1\) for twelve base parameter pairs, compares each exact survivor set with the theorem's seven explicit profiles, and computes labeled multiplicities by factorial counting. It also tests two larger values per smaller-shore size and, by a separate restricted-growth-string enumerator, every labeled vertex partition for \((s,t)=(3,4),(4,5),(5,6)\). Expected output begins with `VERIFY_OK` and includes the number of profiles examined. The mathematical argument for infinite \(t\), the two-singleton stabilization lemma, appears in RESULT.md; these computations are not presented as a substitute for it. No independent mathematical audit has been performed.
