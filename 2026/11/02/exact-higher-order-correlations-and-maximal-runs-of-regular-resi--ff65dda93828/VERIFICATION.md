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

# Verification of the arithmetic claim

The local theorem was reconstructed in two ways: direct valuation of the defining regularity congruence, and a local count of possible lifts of the starting residue from modulo \(p\) to modulo \(p^a\). These give formula (1), while the Chinese remainder theorem supplies multiplicativity across distinct prime powers. Every displayed branch in formula (2) is covered, including equality at \(L=p\) and \(L=2p\). The histogram proof counts each bounded cyclic maximal run at one starting residue using an exact inclusion–exclusion identity.

The standalone `verify.py` uses the independent gcd characterization instead of relying on the local proof. Its run completed with:

```
VERIFY_OK moduli=319 arbitrary_patterns=3828 consecutive_patterns=3903 exact_run_histograms=612 example_cases=6 exact_integer=yes
```

Executed from the supplied source using `python verify.py`. The test exhaustively enumerates every residue of each of 319 moduli from 2 through 320. It compares arbitrary mixed-shift patterns, consecutive blocks across the predicted cutoff, exact maximal-run counts, and six direct examples. It uses no dependencies other than Python's standard library. The tests are finite corroboration, not an infinite proof or a security assessment. Complete scientific and historical-priority assessment by an independent reviewer has not occurred.
