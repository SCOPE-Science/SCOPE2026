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

The standalone program `verify_cartier7.py` uses only the Python standard library. Run `python3 verify_cartier7.py` from the directory containing the files. The script constructs all nine regular monomial differential indices, expands \((x^4+ax^2+bx)^j\) symbolically in \(\mathbb F_7[a,b,x]\), selects the terms with \(x\)-exponents congruent to six modulo seven, and checks all entries of the Cartier matrix against the displayed formula in RESULT.md. The observed successful execution printed `VERIFY_OK` and eight nonzero symbolic entries.

The input consists of the polynomial equation and the valuations in RESULT.md, with no hidden datasets, network requests, or third-party dependencies. The symbolic comparison establishes polynomial identities in the coefficient variables; the rank classification is deduced separately from the pivot structure. Neither the script nor the result classifies the full Newton polygon or the Cartier higher-iterate ranks. Independent audit has not been performed.
