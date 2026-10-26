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

The proof derives the exact conditional route choice from successful nest excursions, embeds the route counts in independent rate-\(1/\ell_i\) Yule processes, and obtains the stated joint almost-sure limits from the strictly positive exponential martingale limits. The gamma-integral calculation establishes the distribution and moment cutoff.

The included `verify.py` uses only the Python standard library. Command: `python3 verify.py`. Executed successfully: 262 exact finite probability/identity checks, including brute-force weighted spanning-tree enumeration for five route-length patterns and four integer-weight patterns each. This is a finite consistency check, not an exhaustive verification of the infinite-process limits. No independent audit has been performed.
