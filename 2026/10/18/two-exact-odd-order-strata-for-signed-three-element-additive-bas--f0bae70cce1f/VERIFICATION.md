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

# Reproducible checks

Run `python3 verify.py` with any Python 3 installation (standard library only). It forms exact integer \(h\)-fold sumsets for many construction-lemma parameters, then, for \(h=11,23,\ldots,119\), evaluates all candidate configurations admitted by the independently derived endpoint bounds for coverage at \(N-2\) (and \(N-3\) where applicable). All checked candidates fail the impossible high coverage targets; each constructive family reaches the claimed sharp threshold.

The check does not cover infinitely many orders, does not certify any inaccessible historical literature, and does not constitute an independent audit. The infinite result follows instead from the complete analytic proof in `RESULT.md`.
