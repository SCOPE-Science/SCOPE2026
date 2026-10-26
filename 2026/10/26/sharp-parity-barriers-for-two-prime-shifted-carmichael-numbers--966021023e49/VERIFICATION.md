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
# Reproducibility checks
The included `verify.py` uses only the Python standard library. Execute `python3 verify.py` in the extracted package directory. It derives admissible prime pairs directly from the two divisibilities and independently from the integer-parametrization formula for all \(2\le a\le100\), comparing the full sets. It checks all enumerated pairs against both parity-specific upper bounds and the sharp witnesses at \(a=8\) and \(a=11\). Successful finite result:

`VERIFY_OK parameters=99 parameterized_pairs=183 sharp_odd=11 sharp_even=8 independent_enumeration=PASS finite_only=YES`

These calculations do not cover every shift or prove novelty. The general algebraic equivalence and bounds are established in `RESULT.md`; no external certificate or independent audit is asserted.
