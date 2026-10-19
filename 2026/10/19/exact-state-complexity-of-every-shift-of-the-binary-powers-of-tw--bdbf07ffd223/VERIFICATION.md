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

# Verification details

The mathematical argument uses right quotients, distinguishes all claimed residual languages by cardinality or suffix length, and handles the smallest shift \(c=1\) and power-of-two shifts separately. The complete-DFA convention includes a reachable rejecting sink.

Run `python3 shifted_powers_checker.py`. The program independently constructs an NFA for the regular expression for each shift, determinizes by subset construction, computes the output partition's fixed-point refinement, and compares exact state counts for shifts \(1\) through \(4095\). For shifts \(1\) through \(100\), it also checks direct arithmetic membership for indices \(0\) through \(179\), using both standard and leading-zero-padded representations. The recorded output is in `shifted_powers_checks.txt`.

Finite computations do not establish the theorem for all shifts; the Myhill–Nerode classification in `RESULT.md` supplies the infinite proof. No independently performed audit or formal certification is claimed.
