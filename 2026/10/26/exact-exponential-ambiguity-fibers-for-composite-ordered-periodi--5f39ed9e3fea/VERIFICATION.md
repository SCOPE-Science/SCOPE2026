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

# Verification of the composite ordered-cycle ambiguity theorem

The full proof uses only finite permutation theory and is recorded in `RESULT.md`. Two independent routes are distinguished: a construction proving a lower bound for each factorization and a converse proving no other \(n\)-cycle has that exact signature.

The principal converse checkpoints are: \(f^m\) has \(m\) cycles each of length \(r\); the complete signature at time \(m\) has precisely the ordered block endpoints as descending elements; one descent per cycle forces the \(m\) cycle supports to be the consecutive blocks; strict ascent away from the maximum determines the rotation on each block; commutation and time-one comparisons determine the successive block order and each shift; \(f^m\) fixes the sum of shifts modulo \(r\).

Reproduction uses only Python 3 standard-library modules. Run `python check_composite_cycle_signatures.py`; its exact stdout is in `CHECK_OUTPUT.txt`. The checker enumerates every \(n\)-cycle for lengths \(4,6,8,9,10\), compares full \(n(n-1)\)-bit signatures and verifies eight complete fibers. Separately it enumerates all admissible parameter vectors for every \(2\le m,r\le5\), confirms their distinct cycles, equal full signatures and full cycle lengths. The complete range over arbitrary \(m,r\) is not certified by finite experiments; it is established by the analytic combinatorial converse.

No independent audit, exhaustive historical priority certification, or global interval-map period-spectrum comparison has been carried out.
