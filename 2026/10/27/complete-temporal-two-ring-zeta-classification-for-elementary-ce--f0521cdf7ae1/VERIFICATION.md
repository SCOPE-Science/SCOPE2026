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

Every data file and checking program is directly included. Using Python 3 and only the standard library, run in this directory:

```sh
python3 build_tables.py
python3 verify.py
```

The generator performs exact integer computations for all 256 ECA truth tables. The validator independently reconstructs the one-step and two-step de Bruijn matrices, evaluates their determinant coefficients via exact Newton identities, reduces all ratios over the rational numbers, and compares each record against the three CSV data tables. It also directly enumerates all binary cyclic configurations for every ring length from one to eight and compares both temporal fixed-set counts to independent matrix traces.

Expected successful messages are:

```text
TABLES_OK 51 25 256
VERIFY_OK rules=256 pair_types=51 second_fixed_zeta_types=40 exact_two_zeta_types=25 temporally_two_rules=149 max_witness_ring=6
```

The finite computation enumerates all **256 rules** exhaustively and all required coefficients up to degree sixteen; these are exact integer operations, not floating-point estimates. The independent short-ring tests are corroborative only. The proof that the computed determinants control **all** ring lengths is in `RESULT.md`. The claim is limited to exact temporal periods one and two. No independent human audit has been performed. The full text of a relevant October 2026 spectral classification could not be inspected, so literature priority is not certified.
