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

# Verification record

The accompanying `verify.py` is dependency-free Python and computes every literal oriented cyclic three-gram multiplicity profile for every binary word of length \(1\) through \(18\), using a direct enumeration of each of the \(2^n\) input words. It independently enumerates possible profile vectors by the four connected-support cases proved in RESULT.md, checks equality of the entire *sets* in each tested length, and compares their sizes to the exact quasipolynomial formula. It additionally checks the formula against the case-parameter enumeration for lengths \(19\) through \(46\).

A successful execution displays three `VERIFY_OK` lines; the last includes \(C_{12}=98\) and \(C_{24}=1247\). Source paths are relative; execute `python3 verify.py` in the directory containing both files. No downloaded data or external packages are needed.

The mathematical all-length assertion rests on the proof of the directed Eulerian support characterization, exhaustive case partition, rational generating-function identity, and coefficient extraction. Finite code execution neither proves infinite validity on its own nor independently establishes publication priority. Independent audit has not been performed.
