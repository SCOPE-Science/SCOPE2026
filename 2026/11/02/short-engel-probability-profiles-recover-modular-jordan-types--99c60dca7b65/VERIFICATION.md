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

Run `python3 CHECK_DIRECT.py` and `python3 CHECK_INVERSION.py` using an ordinary Python 3 interpreter with the standard library. Both should end with `VERIFY_OK`. Compare their standard output byte-for-byte with `CHECK_DIRECT.out` and `CHECK_INVERSION.out` respectively. No installed mathematical package, internet connection, computer algebra, or external data are needed.

The first program implements the group law, group inverses, and iterated commutators without calling the theorem's algebraic normal-form calculations. It exhaustively checks all ordered pairs for several small modular semidirect products against each predicted probability measure.

The second program separately checks finite probabilities, reconstructs Jordan partitions from these probabilities, compares signatures of all partition types within its declared finite range, and checks the exact sharpness witnesses.

The symbolic proof in RESULT.md establishes the statements for every odd prime, all dimensions, all nilpotent endomorphisms of nilpotency index at most \(p\), and all word lengths. The finite checks do not claim to exhaust those infinite parameter ranges or to independently certify novelty. Self-review is recorded separately; independent audit has not been performed.
