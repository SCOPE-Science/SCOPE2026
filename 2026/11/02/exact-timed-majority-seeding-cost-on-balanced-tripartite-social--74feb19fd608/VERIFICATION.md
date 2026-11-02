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

Run `python verify_tripartite.py` with Python 3.8 or newer from this directory. The program uses only the standard library and reports `PASS 4 labelled graph cases, 60 class-count cases, 30 static seeding cases` when successful.

It computes exact finite optimum costs by a full labelled-state Dijkstra search over all intervention subsets on \(K_{m,m,m}\), for \(m=1,2,3,4\). That solver independently returns \(3,5,6,7\). A separate eight-state type-count dynamic program checks the formula for every integer \(1\le m\le60\). Exhaustive initial count triples verify the best static cost for \(1\le m\le30\). The explicit proposed schedule is also checked for every integer \(1\le m\le60\).

These tests are finite corroboration and do not certify the all-size statement. The general argument is given in `RESULT.md`.
