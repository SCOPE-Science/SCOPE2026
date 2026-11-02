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

# Reproducing the cyclic Golay read-weight census

From a directory containing `GENERATE.py`, `VERIFY.py`, `ZERO_RUN_CENSUS.csv` and `B_SYMBOL_SPECTRA.csv`, use Python 3 with no additional packages:

```sh
python3 GENERATE.py
python3 VERIFY.py
```

The generator program enumerates every message integer from 0 through 4095, builds the standard Golay cyclic code, records all cyclic zero-run partitions and uses an exact window-count formula to construct each b-symbol spectrum. The verifier then independently reconstructs the same code using systematic polynomial division; it scans all 23 cyclic window starts for every word and every width 1 through 23. It checks all supplied coefficients, every zero-run multiplicity, and the exact minimizers and values, including the 23 rotations of the generator for widths 3 through 11.

Observed output: `GENERATED: 81 run types, 23 complete window spectra` followed by `VERIFY_OK: 4096 codewords, 81 zero-run classes, all 23 read lengths`.

The result is limited to the explicitly specified binary length-23 code. The exhaustive 4096-word calculation proves this finite classification, not a result about arbitrary blocklengths or arbitrary coordinate orderings. No external independent scientific audit has been performed.
