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
The standalone `verify.py` uses pure Python standard-library routines. Execute `python verify.py` with a standard Python 3 interpreter. The script enumerates all full-domain diagrams on at most five pairs of vertices, explicitly constructs idempotent factors of the same rank by breadth-first token movement, and compares the diagram product to the input using independent three-layer connectivity. It separately enumerates the idempotent-generated closures of every proper rank ideal through four pairs of vertices.

Expected checked singular-element totals for sizes two through five: `3,46,831,19801`. Rank-ideal closure counts checked: for size two `3`; for size three `10,46`; for size four `37,471,831`. A successful run ends with `VERIFY_OK`.

# Scope and limits
Finite tests corroborate, but cannot prove, the universal statement. The unrestricted mathematical proof is in `RESULT.md`. No external or independent audit has been performed; the available verification consists of reproducible self-checks.
