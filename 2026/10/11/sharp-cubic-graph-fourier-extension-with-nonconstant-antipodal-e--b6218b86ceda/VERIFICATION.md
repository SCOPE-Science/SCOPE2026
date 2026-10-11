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

Run `python3 verify.py` with Python 3's standard library; no external data or packages are required. The checker enumerates all ordered pairs, confirms uniqueness of unordered fibers at every nonzero sum, and computes direct additive-convolution energies and the independent reduced-energy identity. Its field model covers four prime fields and the degree-two extension \(\mathbb F_{25}=\mathbb F_5[\alpha]/(\alpha^2-3)\). For each field it checks forty seeded nonzero random complex functions and a sharp extremizer with independent antipodal phases.

Observed output:

```
q=5: unordered-pair fiber check, 40 random vectors, sharp extremizer checked; sharp fourth-power ratio=2.454545454545
q=7: unordered-pair fiber check, 40 random vectors, sharp extremizer checked; sharp fourth-power ratio=2.600000000000
q=11: unordered-pair fiber check, 40 random vectors, sharp extremizer checked; sharp fourth-power ratio=2.739130434783
q=13: unordered-pair fiber check, 40 random vectors, sharp extremizer checked; sharp fourth-power ratio=2.777777777778
q=25: unordered-pair fiber check, 40 random vectors, sharp extremizer checked; sharp fourth-power ratio=2.882352941176
PASS: 200 non-extremal tests and five sharpness tests.
```

All floating-point comparisons use absolute tolerance \(5\times10^{-12}\). The analytic proof in RESULT.md, including the field-theoretic fiber identity and exact convex optimization, is necessary for arbitrary fields. The checker is finite corroboration and not an exhaustive search for all maximizers even in the tested fields. No independent mathematical audit has been performed.
