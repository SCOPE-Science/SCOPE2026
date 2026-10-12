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

# Reproducible verification

Execute `python3 verify.py` using Python 3 with the standard library; no files outside this package are required. The verifier checks the arithmetic definition against direct overlapping-substring counts for the first 16,384 indices at every tested parameter, confirms 131,072 carry transitions, and compares all consecutive transitions across 2,097,152 positions for each integer parameter from 2 through 10. It also checks exact event-block locations, all predicted gap types, rational normalization and weighted length totals, and frequency histograms in 32,768 consecutive blocks.

The program terminates with the sentinel:

`VERIFY_OK k=2..10 direct_N=2097152 bitcount_prefix=16384 delta_prefix=131072 exact_direct_spectra=yes event_blocks<=4096 frequency_blocks=32768 normalized_mass_and_mean_length=yes`

These finite checks are consistency tests and cannot prove an infinite statement. The infinite classification and densities are derived in the written proof using binary carries, exact event locations and arithmetic-progression densities. No external or independent audit is asserted.
