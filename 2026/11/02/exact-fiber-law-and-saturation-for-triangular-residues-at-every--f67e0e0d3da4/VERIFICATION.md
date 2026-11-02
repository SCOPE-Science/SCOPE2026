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

The reproducibility program `verify_triangular.py` uses explicit integer arithmetic and independent enumeration, rather than reading the proof's input text. Execute it with Python 3 from the same directory as the extracted files. The expected final line is `VERIFY_OK moduli=750 all_fibers=exact primepowers=checked doubling_lift=checked`.

The program compares the claimed root-count product with every first-block fiber for all positive moduli through \(750\); independently enumerates odd prime powers; and tests lifting to powers of two over several odd factors. This validates those finite ranges only. The unlimited theorem is proved using factorization of \(8T(n)+1\), local lifting, CRT, and reflection across the \(2m\) period. No external proof assistant or independent audit was used. Source-based bibliographic priority remains conditional on the inspected literature.