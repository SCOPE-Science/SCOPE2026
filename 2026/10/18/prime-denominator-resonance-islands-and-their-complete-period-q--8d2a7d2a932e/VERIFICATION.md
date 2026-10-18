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

The statement is established by an analytical argument, not by numerical orbit sampling: the primitive-root minimal polynomial forces all \(q\) branch signs to coincide; a branch-center average then gives the orientation obstruction; the remaining inequalities form two regular polygons with inradius \(-\tfrac12\cot(\pi p/q)\). The perimeter–inradius formula produces the exact area.

Run `python CHECK.py` from the directory containing this file. It requires only the Python standard library and reports 4236 finite checks, including exact integer checks for all sign words at \(q=5,7,11\), plus floating-point polygon and orbit checks. Universal statements, all boundary cases and asymptotics are proved in `RESULT.md`, not inferred from those finite tests.

Limits: the result concerns prime denominators at least five, this precise discontinuity convention, and the period-dividing-\(q\) locus. An independent mathematical audit has not been performed.
