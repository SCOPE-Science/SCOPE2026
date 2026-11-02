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

Run `python3 support_refinement.py` and `python3 extension_count_audit.py` with Python 3 and its standard library. Compare their standard output with `support_refinement_output.txt` and `extension_count_audit_output.txt` respectively. Both recorded outputs were produced by running the scripts from this scientific package.

The first program generates projective coordinate planes over fields with \(2,3,4,5,7\) elements. It enumerates enhanced three-object types and supports of all one-object extensions, exhausting all triples through order four; it does not exhaust every triple for the last two orders. The second program independently represents the same planes as affine planes with their lines and points at infinity, and verifies the exact counts for the five geometrical configurations and their duals.

The mathematical claim for every finite projective plane, including non-Desarguesian planes and orders absent from the tests, follows from the symbolic incidence-count identities and the infinite four-pebble strategy in `RESULT.md`. No finite test implies that assertion in isolation. Source comparisons are limited to the identified and materially inspected literature; independent validation and exhaustive historical-priority verification are not performed.
