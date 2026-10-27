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
# Reproducibility and limits

Run `python3 verify.py` using the standard Python library. The expected terminal success marker is `DYCK_ABELIAN_BORDERS_PASS`. The executable enumerates complete Dyck families for semilengths \(1\) through \(12\) by the Catalan first-return decomposition and tests literal Parikh vectors without using the theorem's height-return criterion. The latter criterion is calculated separately and compared word by word. It then checks independently enumerated pairs through semilength \(6\), and performs exact-integer generating-function recurrences through semilength \(30\).

The computational checks are finite. They cannot establish the all-length bijections or the limit. Those parts are justified by the combinatorial decomposition, the exact Catalan-square partial-sum identity and singularity analysis in RESULT.md. No independent mathematical audit or external certification is asserted.
