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

Run `python3 verify.py` with Python 3.8 or newer. It uses no dependencies outside the standard library. The recorded direct brute-force consistency check returned:

`VERIFY_OK graphs=1103 subset_checks=1106468 even_cycle_graphs=486 strict_differences=486 max_order=7`

Each checked paired-dominating set is constructed as an actual vertex subset of the whiskered graph and independently tested for domination and a perfect matching. The formula is generated from core vertex subsets and induced perfect matching counts. Every simple graph of core orders one through five is exhausted; four further examples at orders six and seven are checked. The even-cycle condition is also checked by a distinct simple-cycle search.

This is a finite computational consistency check, not an exhaustive verification of all finite graphs or a replacement for the universal combinatorial proof. Published scalar paired-domination values are prior work. The spectral statement uses the proof's direct determinant expansion and the standard real-symmetric spectral theorem, not a numerical approximation. Independent audit was not performed.
