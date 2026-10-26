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

# Reproducibility

Run `python3 verify.py` from this directory. It reconstructs every Rudin–Shapiro sign independently using parity of adjacent binary `11` pairs and iterates the actual signed and alternating partial sums. It tests all predicted edge indices and ordered lower-height permutations for \(1\le k\le7\), and cross-checks every predicted inverse visit at every lattice site of those frontiers against all visits found up to the last required index.

The expected output is `PASS: all 515 dyadic edge and point inverses, k=1..7; direct a(n) through n=32767`. Source files include the complete implementation. This is a finite consistency check, not an infinite proof; the all-\(k\) argument is given in RESULT.md. No separate or independent mathematical audit has been performed.
