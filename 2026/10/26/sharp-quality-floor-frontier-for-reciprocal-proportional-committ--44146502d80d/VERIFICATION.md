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
# Verification

Reproduce the exact rational checks with Python 3:

```
python3 check_quality_floor.py
```

The script examines 15,191 rational inequalities and finite witness identities, including monotone approach to the asymptotic limit. Its observed exit status was zero with output `ALL EXACT CHECKS PASSED (15191 rational tests)`. No third-party packages or network accesses are needed. The analytic proof treats arbitrary real quality floors, unbounded finite committee sizes and full axiom satisfaction; the code alone does not prove these infinite conclusions. Those parts depend on the written proof and the cited proportional rule constructions of Boehmer, Dong, Kreisel and Utke, arXiv:2609.08830, Appendix G.

No independent audit has been performed.
