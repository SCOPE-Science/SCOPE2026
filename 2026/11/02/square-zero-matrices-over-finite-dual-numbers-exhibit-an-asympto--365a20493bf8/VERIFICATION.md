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

Run `python3 verify.py` from this directory. It needs only Python standard-library modules. The program was executed against the saved package's checker contents, and the resulting complete test set was:

```
CHECK 2 1 1 2 exhaustive_B
CHECK 3 1 1 3 exhaustive_B
CHECK 2 2 2 28 exhaustive_B
CHECK 3 2 2 153 exhaustive_B
CHECK 2 3 2 1184 exhaustive_B
CHECK 3 3 2 44955 linear_kernel
CHECK 2 4 3 226816 linear_kernel
CHECK 4 2 496 GF4_exhaustive
VERIFY_OK
```

For prime-field runs, the code enumerates every \(A\) with \(A^2=0\), determines its rank and the anti-commutator kernel by independent linear elimination, and compares the stratum count with the symbolic formula. In indicated smaller cases it also enumerates every \(B\) and tests \(AB+BA=0\) directly. The \(\mathbb F_4\) case independently uses polynomial-basis field arithmetic. These checks do not establish the asymptotic or the universal quantifiers; those are supplied by the written proof.
