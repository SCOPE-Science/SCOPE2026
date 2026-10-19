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

Place the two additional package files, `verify.py` and `spectrum.csv`, in one directory. Run `python3 verify.py` under Python 3. The script has no dependencies beyond the standard library and performs exact integer and rational computations.

The check traverses all 65536 directed-edge bijection assignments and independently generates Euler circuits by depth-first search. It asserts that the resulting sets of 2048 rotation classes are identical. It computes all periodic autocorrelation coefficients in two different ways and verifies their exact equality, aggregates the full joint energy-versus-peak histogram, compares each of the 47 CSV rows, computes moments, and checks the extremal symmetry orbits.

An execution produced:

```
VERIFY_OK independent_complete_generators=2 local_pairings=65536 order5_cycles=2048 independent_correlation_methods=2 cyclic_correlation_values=65536 energy_levels=47 energy_min=192:12 energy_max=1952:4 minimizer_symmetry_orbits=3 maximizer_symmetry_orbits=1 mean=2813/4 variance=1336631/16
```

Published-data cross-check: the exact histogram gives average normalized per-sequence RMS sidelobes of about 0.145958, 0.123429 and 0.077771 for the whole family, the peak-at-most-eight family, and the peak-at-most-four family. Rounded to three decimal places these reproduce Spinsante–Andrenacci–Gambi (2011), Table 3. This comparison corroborates the normalization, but the finite exact proof is the independently implemented cycle and correlation enumeration.

Finite exhaustion proves only the asserted order-five case. No claim of third-party validation, all-order extrapolation, or historical-priority certification is made.
