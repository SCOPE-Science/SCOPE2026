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

# Verification record

The standalone `verify_nl_ai.py` has no nonstandard dependencies. Run `python3 verify_nl_ai.py`. It tests normal-form coefficient matrices; an independent evaluation-rank oracle for all odd-weight truth tables in four variables; affine-distance nonlinearities; and all maximum-period five-stage feedback functions using full state-cycle traversal. The oracle constructs every degree-at-most-two monomial evaluation matrix on each of the two 16-point graphs and computes its binary row rank.

Expected output:

```
ODD_FEEDBACK_NL_ANNIHILATOR [((1, 4), 512), ((3, 2), 17920), ((5, 0), 14336)]
DEBRUIJN_5_NL_ANNIHILATOR [((2, 4), 24), ((6, 2), 1128), ((10, 0), 896)]
VERIFY_OK
```

The three normal-form matrices and graph-restriction rank identity are also established mathematically in the proof; finite software checks merely corroborate these elementary finite pieces. The 2012 nonlinearity counts belong to the cited literature, not to a novel enumeration claim. Historical priority and independent mathematical review are outstanding.
