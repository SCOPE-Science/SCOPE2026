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

Run the two standalone programs using Python 3 with no nonstandard dependencies:

```bash
python3 verify_cartier.py
python3 verify_independent.py
```

Both programs actually completed successfully in the local package directory. The first prints `CARTIER_VERIFY_OK`, and the second prints `INDEPENDENT_VERIFY_OK`; both count \(90\), \(10\), and \(10\) smooth ordered \(\mathbf F_{11}\)-coefficient pairs in the three stated invariant strata. Their coefficient-generation and matrix-rank routines differ. The independent verifier also prints \(\#C_{1,0}(\mathbf F_{121})=210\), \(\#C_{1,5}(\mathbf F_{121})=144\), and \(\#C_{1,1}(\mathbf F_{121})=162\), computed by direct quadratic-extension arithmetic. Independent scientific audit has not been performed. Finite computation cannot establish the classification over all algebraically closed coefficient fields; the proof in `RESULT.md` gives that deduction symbolically.
