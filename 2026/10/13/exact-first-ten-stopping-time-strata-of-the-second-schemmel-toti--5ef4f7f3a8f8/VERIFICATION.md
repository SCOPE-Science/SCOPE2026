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

# Exact reproduction

Run `python3 verify.py` with a standard Python 3 installation. The program uses no third-party modules, downloads or probabilistic tests. It computes each inverse fiber exactly, checks all forward edges, and independently checks direct stopping-time values for every odd integer from three through fifty thousand. Its expected final line begins with `EXACT_CERTIFICATE_OK` and gives the ten rank/count/maximum/uniqueness quadruples.

The finite-depth proof depends on the inverse-prime-power lemma and uniqueness of factorization, as spelled out in `RESULT.md`. Correctness is not inferred merely from code execution: the lemma proves enumeration completeness; the executable provides the exact finite arithmetic certificate.

The certificate does not prove Conjecture 20 for rank eleven or greater, and it does not establish that a separate investigator has audited the proof or code. The earlier restricted-domain iteration literature remains a possible source of unrecorded overlap.
