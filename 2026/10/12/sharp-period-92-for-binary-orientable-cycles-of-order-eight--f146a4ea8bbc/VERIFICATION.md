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

# Exact verification

Keep `verify.py`, `DUAL.txt`, and `WITNESS.txt` together and invoke `python3 verify.py` with standard assertions enabled. Only the Python 3 standard library is required.

The program deterministically reconstructs the 120 nonpalindromic eight-bit reversal pairs, 72 seven-bit reversal orbits, 240 labeled ports and 330 graph edges. It checks the pivotal signed-incidence identity for both orientations of every reversal pair at every nonpalindromic orbit, then verifies the complete 240-integer dual vector: its sum is exactly 28 and every edge satisfies its integer inequality. Consequently every induced perfect matching has omission cost at least 28.

Separately the program checks all 92 cyclic length-eight windows of `WITNESS.txt`, including uniqueness, absence of palindromes, and pairwise reversal incompatibility. The observed replay was:

```text
VERIFY_OK order=8 pair_orbits=120 quotient_vertices=72 ports=240 certificate_edges=330 dual_sum=28 upper_bound=92 witness_period=92
```

The dual feasibility alone supplies the finite upper-bound certificate, conditional on the stated mathematical reduction from orientable cycles to perfect matchings; the executable also checks its local identity but cannot substitute for understanding that reduction. No exhaustive enumeration of all binary cycles is asserted. No generalization beyond window length eight has been proved here.
