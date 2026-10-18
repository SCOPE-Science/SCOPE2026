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

# Verification

The finite theorem is reproducible with `python3 verify.py` and the Python standard library. The script contains two independent exhaustive 2048-cycle generators, one via complete Eulerian edge tours starting with the unique `00000` edge and one via all 65,536 incoming-to-outgoing local edge bijections. Set equality is asserted; each cycle is checked to contain exactly 32 distinct cyclic five-bit factors.

For all 32 distinct linear cuts of all 2048 cycles, one palindrome-partition algorithm uses a literal comparison of each candidate suffix with its reverse; another expands every possible odd/even palindrome center. Their optimal costs are asserted equal on all 65,536 rooted words. The observed rooted histogram, the complete per-cycle best/worst histogram, both total counts, and two exceptional canonical strings are checked with exact integer comparisons.

Successful execution from the packaged script produced:

```
VERIFY_OK binary_debruijn_order5_cycles=2048 rooted_words=65536 independent_cycle_generators=2 independent_palindrome_parsers=2 root_spectrum=4:384,5:3554,6:18266,7:29118,8:12138,9:2030,10:46 exceptional_min9_cycles=2 minmax_cells=14
```

The graph and dynamic-programming completeness arguments appear in `RESULT.md`. No finite sampling, statistical inference, network access, specialized proof assistant, or third-party library is used. External independent mathematical audit is not performed, and all-order consequences remain unproved.
