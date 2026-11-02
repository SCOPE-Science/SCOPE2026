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

The finite checker `checker.py` uses two independent word constructions (base-three digit test and iterated substitution) and a prefix-function border finder. It checks every cyclic cut and every predicted shortest border for ranks \(0\) through \(6\) inclusive, every local-period histogram, and the period-based obstruction to longer unbordered factors. Run `python3 checker.py`; a successful run ends with `VERIFY_OK`.

Finite execution does not prove the all-rank assertion: the published mathematical package supplies an induction and the exact four-block local argument. Independent human review and machine formalization have not been performed.
