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

# Reproducibility and scope

Run `python verify.py` with Python 3.8 or later and the standard library. It uses exact rational fractions, not floating-point tolerances. The executable independently integrates the relevant preimage intervals and compares the outcome with the closed-form overlap identity, compares exact enumeration of all short base-selection words with the weighted residue matrix, checks the two-map sixth-cell formula against a binomial sum, and tests finite-cutoff examples.

The expected output is `PASS: {'direct': 1300, 'matrix': 220, 'special': 72, 'cutoff': 10, 'stationarity': 208}`. The proof covers arbitrary integers and finite supports; the code checks finitely many cases and therefore does not independently establish all-dimensional quantifiers, historical priority, or mathematical value. No external audit has been carried out.
