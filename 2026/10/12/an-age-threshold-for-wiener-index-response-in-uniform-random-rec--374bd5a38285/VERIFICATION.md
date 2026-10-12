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
# Reproducibility and evidence

`verify.py` requires only Python 3 and its standard library. Execute `python3 verify.py` in the same directory. It reports 46,233 enumerated recursive trees, 120 exact conditional identities, eight exact root-degree/Wiener covariances, and 3,689 exact recursion and conditional-parent-averaging identities. Finite checks use `fractions.Fraction` rather than rounded arithmetic. The age-threshold ratio illustrations employ floating point, solely to display the proved large-size result.

The proof of all-size equations (1)–(4) is in `RESULT.md`. Its nonstandard step is the expected sum of distances from a fixed-label vertex: the birth-time boundary and later uniform-attachment recursion are stated explicitly there. Finite enumerations do not establish a universal infinite formula; the algebraic recurrence does. A full historical novelty guarantee and independent audit have not been performed. The older fixed-label distance-distribution article noted in the references was not inspected in complete form.
