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

# Reproduction and limitations

Run `python3 verify.py` with Python 3 (standard library only). The checker constructs all claimed witness boards for 114 tested dimension pairs and checks every empty cell against the graph's original row-and-column adjacency. It enumerates all smaller-weight labelings for eight small boards (308540 examined) to exclude a smaller feasible value in those specific instances. The checker also tests the lower-bound palette inequalities for 44 size pairs. The reproduced output terminates in `VERIFY_OK`.

The all-parameter lower bound is established by the row/column palette proof in `RESULT.md`, not by finite enumeration. The code does not test all dimension pairs or all priority-relevant literature. No independent audit or external certification has been performed.
