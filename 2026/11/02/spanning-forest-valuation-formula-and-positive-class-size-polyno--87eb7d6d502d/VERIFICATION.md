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

The mathematical proof uses the total unimodularity of the oriented incidence matrix and the determinantal-ideal characterization of Smith exponents over a DVR. Both can be checked directly from the argument in `RESULT.md`. The finite checks in the standalone `verify.py` compare predicted class counts with independently computed commutator-matrix minors and directly enumerated commuting pairs. Execution: `python3 verify.py`; expected ending `VERIFY_OK 44`.

Finite experiments are not the proof for infinitely many graphs, levels, or residue fields. The general conclusions follow from the symbolic forest minor identity and the Smith reduction. No independent mathematical audit has been performed.
