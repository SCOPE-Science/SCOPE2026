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

# Reproduction and verification

The coefficient data in `SPECTRUM.csv` is verified by running from a clean directory containing the supplied source and the CSV file:

```sh
cc -O3 -std=c11 -Wall -Wextra -pedantic -o verify verify.c
./verify
python3 crosscheck.py
```

Expected output is `VERIFY_OK` and `CROSSCHECK_OK`. The main verifier exhaustively counts all words satisfying Hasse syndrome conditions for each code index 0–11 and all unique generator messages for indices 12–32. It compares every weight coefficient, row sum, minimum positive weight, and minimum multiplicity. The independent Python checker repeats direct generator enumeration for selected indices and evaluates a separate cyclic four-state transfer matrix for the all-nonzero-triplet coefficient of the whole binary space. No random checks or timeout-based impossibility claims are used.

The table is finite and covers exactly length 32, read window length 3, and the 33 binary cyclic ideals. Correctness review is self-review only; independent audit has not been performed.
