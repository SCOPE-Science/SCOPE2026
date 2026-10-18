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

# Reproducible finite checks

Run `python3 prime_root_checker.py` with Python 3 standard library. The script implements permutation composition independently; tests all constructed right-stabilizer distinguishing witnesses for every nonidentity permutation in \(S_n\), \(3\le n\le8\), and every allowed prime in \(\{3,5,7\}\); then constructs the actual two-generator root DFA and performs reachability plus Moore partition minimization through \(n=6\).

The saved `checks.txt` records the exact successful output. The proof's universal upper bound and infinite lower bound are symbolic mathematical arguments in `RESULT.md`; the finite checker is a corroborating independent implementation only. Exact content hashes of these artifacts and this report are recorded in the containing delivery record. The checker makes no claim of external or independent scientific certification.
