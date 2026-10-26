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

The theorem is established algebraically over an algebraic closure of \(\mathbb F_5\). In particular, the shared quadratic for the four nonzero fourth powers excludes all possible extra geometric singularities, not only those over finite fields. Nondegenerate Hessians at the two symmetry representatives establish reduced \(A_1\) local schemes throughout each orbit.

The standalone exact checker `CHECK.py` was executed with Python 3 and SymPy, yielding the following reproducible terminal lines:

```text
CHECK_OK total_P3_F5=156 S_F5=96 singular_F5=96; support3=64 support4=32
HESSIAN_DETERMINANTS mod5: 3 3
```

The finite enumeration does not prove geometric completeness: that follows from the case division in `RESULT.md`. The script uses no external datasets or remote services. No calculation of a resolution of the associated double-octic threefold is claimed; external independent validation has not been performed.
