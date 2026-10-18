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

The accompanying standard-library checker `verify_reshuffling.py` enumerates both reshuffling permutations and all four independent-with-replacement two-draw index sequences. It uses exact `fractions.Fraction` arithmetic, confirming the derived expected-objective gap, independent Euclidean second-moment formula, and the half-parameter equality across 3,795 rational parameter pairs. Run `python verify_reshuffling.py` in the directory containing this document and the script. The unrestricted theorem rests on the written path enumeration and derivative proof rather than those finite checks. No external audit has been performed.
