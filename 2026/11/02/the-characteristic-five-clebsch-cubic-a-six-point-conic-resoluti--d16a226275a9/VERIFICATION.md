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

# Verification of the displayed theorem

The accompanying `verify_clebsch_aut.py` uses only Python's standard library. Run:

```sh
python3 verify_clebsch_aut.py
```

It must print `CLEBSCH_CHAR5_BLOWUP_AUT_ZETA_PASS` and the point counts \((5,56)\), \((25,776)\). This execution was performed on the packaged verifier, not on a different file. Direct enumeration also recovers six projective basepoints on the conic, \(120\) distinct permutations induced by the coordinate-permutation subgroup, and the \(21\) rational projective lines with tangent rank profile \(15\) full rank and \(6\) rank deficient.

The proof in RESULT.md, rather than an exhaustive finite enumeration, establishes the global upper bound on the geometric automorphism group, the identification of the minimal resolution, and the point-count formula for every extension degree. The line-scheme profile is corroborative context and is not a new claim. Neither independent expert validation nor a separate independent audit has been conducted.
