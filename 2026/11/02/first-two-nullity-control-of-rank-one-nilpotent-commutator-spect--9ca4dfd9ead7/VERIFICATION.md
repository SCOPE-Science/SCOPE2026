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

The source file `check_spectrum.py` uses only Python's standard library. Invoke `python check_spectrum.py` from the directory containing it. Its passing output is `NILPOTENT_RANK_ONE_COMMUTATOR_MOMENT_SPECTRUM_OK 40 34015`.

The enumerator constructs all rank-one square-zero matrices uniquely by choosing a vector with its first nonzero coordinate equal to one and an independent nonzero annihilating covector. It builds every nilpotent Jordan form through all partitions in the checked ranges, multiplies matrices directly over prime fields and over the explicitly defined degree-two extension field, and checks moment multiplicities, commutator ranks, zero-fiber rank counts, characteristic-two minimal-polynomial relations, odd-characteristic cubic relations, and nilpotent-square/cube behavior.

Tested cases: all partitions of every dimension 3 through 6 over the field of two elements, dimensions 3 and 4 over the field of three elements, and dimension 3 over fields of four and five elements. These are finite consistency checks and do not establish the theorem for arbitrary dimensions or fields. The general proof is in `RESULT.md`.
