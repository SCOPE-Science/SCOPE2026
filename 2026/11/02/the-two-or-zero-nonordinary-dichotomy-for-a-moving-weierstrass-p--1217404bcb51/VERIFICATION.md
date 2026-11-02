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
# Reproducible verification and scope

The complete polynomial proof is in `RESULT.md`. Run `python3 verify_linearized_g2.py` using only Python 3 standard-library modules; no network, CAS, downloaded data, random seeds or external dependency is needed. This program checks the displayed coefficient formulas, the Hasse–Witt determinant and its infinity chart, the Bezout polynomial identity, an independently built \(7\times7\) Sylvester determinant for the resultant, complete enumeration of the \(243\) monic quintics over \(\mathbb F_3\), all \(162\) separable cases, and the two explicit \(3\)-rank examples.

Expected exact output:

```text
LINEARIZED_GENUS2_CHAR3_RESULTANT_REDUCED_NONORDINARY_DIVISOR_PASS
Exhausted 162 separable monic quintics over F3; parameter strata={'two': 120, 'double': 42, 'infty': 42}
Explicit genus-two p-rank pair: (t=1,r=1,#F3=6), (t=-1,r=0,#F3=4).
```

The \(243\) parameter checks are finite experiments; they **do not** establish an assertion over arbitrary algebraically closed fields. The universal proof consists of the explicit symbolic polynomial identities together with the standard hyperelliptic Cartier–Manin formula and separability argument. The theorem is restricted to characteristic \(3\), genus \(2\), separable fixed quintic, and the moving-point parameter line. Singular fibers and stack intersection multiplicities are outside its conclusion. Independent mathematical verification and external audit have not occurred.
