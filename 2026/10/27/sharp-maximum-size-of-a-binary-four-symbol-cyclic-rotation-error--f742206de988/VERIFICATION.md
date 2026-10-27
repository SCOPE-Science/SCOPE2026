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

## Reproducibility
Run `python3 verify_cyclic4.py` using Python 3 and its standard library. The executable checks the exact 32-state recurrence, the lexicographic length-six suffix vector, the componentwise identity at lengths six and eleven, all 2,048 binary words of length eleven grouped by their last five bits, and the complete local-versus-direct ball enumeration through length eleven. It additionally tests the periodic attaining word through length one hundred.

`VERIFY_OK` was obtained from the packaged source before delivery. The finite recurrence together with its componentwise translation identity proves the result for every length, not only those directly enumerated.

## Limitations
No independent external audit has been performed. The finite verifier proves the stated all-length result only together with the written structural arguments establishing the locality formula and recurrence. It does not address general permutations, nonbinary alphabets, or multiple bursts.
