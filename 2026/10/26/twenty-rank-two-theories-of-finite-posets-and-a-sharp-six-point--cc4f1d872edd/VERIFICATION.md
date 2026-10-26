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

Run `python3 verify.py` from this directory using Python 3.8 or later; no third-party packages are required. `witnesses.json` lists twenty transitive strict orders on at most six points. `verification_output.txt` contains the observed standard-output trace.

The checker validates the witness encodings and spectra, enumerates all forward-order relation seeds on one through six vertices and closes them transitively, checks exact minimum representative sizes, and evaluates all 210 unordered pairs of witness posets and 1000 additional comparisons against posets of orders at most four with an independently coded ordinary two-round Ehrenfeucht--Fraïssé recursion. It prints `CLASSIFICATION_OK` on success.

The finite enumeration does not establish the bound for posets of arbitrary size. That conclusion is supplied by the four-case structural classification in `RESULT.md`. The computations do not assert historical originality or independent validation.
