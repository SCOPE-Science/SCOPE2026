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

# Verification record

Run `python3 checker.py` with the Python standard library. The checker has no external packages or network requirements. On its direct tests, it prints `FINAL_ALL_CHECKS_PASSED`.

It checks all ordered supports in symmetric types \(A_1\) through \(A_8\) using their 0-Hecke projection action on the identity permutation, compares the full three-index support profile with an independently coded transfer recurrence, and rechecks each pair as endomorphisms on every permutation through \(A_5\). It additionally checks all ordered supports on every signed permutation for \(B_2,B_3,B_4\), and compares component-polynomial and independent graph-enumeration implementations for small paths and stars. These finite checks corroborate a separate algebraic counting proof; they do not establish the theorem for infinitely many ranks by enumeration.

Prior mathematical results used in the proof are Sentinelli (2018), Propositions 3.3–3.5, and standard classification of 0-Hecke monoid idempotents by longest standard parabolics. The output makes no assertion of independent certification.
