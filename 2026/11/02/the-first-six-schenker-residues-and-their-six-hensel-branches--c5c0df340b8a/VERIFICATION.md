---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

## Reproducible computational checks

From the directory containing `verify_schenker.cpp`, compile with `c++ -O2 -std=c++17 verify_schenker.cpp -o verify_schenker` and run `./verify_schenker`. The supplied arithmetic verifier uses two modular evaluations to check the six level-one classes at 2339 within its finite census. It checks that the six divided nondegeneracy residues modulo 2339 are, in increasing order of the underlying root, `843 1662 1732 24 685 1079`. It then checks the six listed lifts directly modulo 2339 squared. The accompanying `schenker_census.csv` checks previously established level-one data. Replay it with `./verify_schenker --census > recomputed.csv` followed by `cmp recomputed.csv schenker_census.csv`.

The congruences and nondegeneracy tests are finite. The all-depth classification uses the last assertion of Miska's Theorem 1, after applying its hypotheses to the six known level-one roots; the code does not check infinitely many levels.
