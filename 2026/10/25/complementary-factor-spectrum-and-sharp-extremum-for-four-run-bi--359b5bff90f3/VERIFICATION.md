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

# Verification of complementary-factor spectrum and maximum

The proof classifies complementary factors by one, two, three or four constant runs. It proves the polynomial identity, derives the sharp inequality for unequal interior runs, and treats equality for equal interior runs by a concave integer quadratic. Its domain is **all positive** four-run parameters, not merely finite tested ranges.

Running `python3 verify.py` from the artifact directory gave:

```
VERIFY_OK exhaustive_length_spectra=2401 extremal_lengths=4..64 (61)
```

The checker obtains the actual factor spectrum by enumerating unique substring strings and testing whether their bitwise complements are also substrings. In a separate section it checks every four-part positive composition for lengths 4 through 64 and matches all maximum-equality parameter lists. These are finite checks, not independent audits or substitutes for the uniform proof. No arbitrary timeout is used as a mathematical certificate.

The main limits are restriction to contiguous factors, binary alphabet and exactly four runs, and residual risk of unlocated equivalent literature. No external independent audit was performed.
