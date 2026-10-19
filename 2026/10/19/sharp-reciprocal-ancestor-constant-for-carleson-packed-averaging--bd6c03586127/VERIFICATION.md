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

## Reproduction

Run `python3 verify.py` from the directory containing this document and the standalone `verify.py` program. Python 3's standard library suffices. A successful run prints `VERIFY_OK` and states the scope of the finite tests.

## Checks actually performed

The rational-arithmetic verifier passed for 35 distinct parameters. It checked the exact greedy recursion and closed geometric tail, all measurable subsets of the finite eight-point witness spaces (one for each nonendpoint parameter), and enumerated admissible rational four-coordinate prefixes. The witness Carleson constant and infinite tail were also reconstructed directly in the mathematical proof.

## Proof versus finite tests

The program has no ability to establish inequalities for uncountably many \(\Lambda\) values or all nested families. Those claims rely on the coordinatewise-minimal recurrence argument, the explicit solution and the arbitrary finite-family witness in the proof. No computer calculation or finite enumeration is used as an infinite proof. At \(\Lambda=1\), the one-ancestor conclusion follows directly from the Carleson condition. The file does not represent independent checking or certification.
