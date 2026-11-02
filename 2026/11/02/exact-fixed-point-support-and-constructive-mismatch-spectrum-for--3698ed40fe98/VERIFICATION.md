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
# Reproducible verification

The standalone `check_support.py` requires Python 3 and only the standard library. Invoke `python3 check_support.py` in a directory containing the file. `CHECK_LOG.txt` records its exact normal output.

The checker evaluates exact integer coefficients by a cached recursion for remaining color multiplicities. All ordered positive compositions of sizes 1 through 11 are checked; each positive support point also has an explicit, independently checked constructive witness. The checks cover 2,047 profiles and 19,714 support cells; none of the reported counts uses Monte Carlo sampling.

The general existence and impossibility statements require the proof in `RESULT.md`; no finite test certifies every integer multiplicity. The work has not undergone independent mathematical audit.
