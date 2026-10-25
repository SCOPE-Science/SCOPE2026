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

# Verification details

`verify.py` is a Python 3 standalone standard-library checker. Running `python3 verify.py` yielded:

```
CYCLE_SPECTRA_ARITHMETIC_OK 18054 1600 4900 1584
```

The four counts indicate modular finite-semigroup/gcd instances, prime-power witnesses, exact singleton-length witnesses, and additional signed/zero-generator components. In each case the direct residue computation was compared with the symbolic gcd or divisibility prediction. The program does not enumerate all infinite regular expressions or all formulas, and therefore is not a certificate of the general theorem. The full result is established by induction and effective semilinearity as written in `RESULT.md`. No outside expert or independent audit has checked the proof.
