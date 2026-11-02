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

# Verification and limits

The proof in `RESULT.md` establishes correctness for every nonnegative shift and every finite LSD-first binary input. The four exceptional shifts, the six always-reachable low-quotient states, separation of all residual functions, absence of high-quotient duplication, and sharp dyadic equalities are derived explicitly.

Execute `python verify.py` with Python 3.8 or later (Python 3.10 or later is recommended for integer `bit_count`). The script uses only the Python standard library. Its successful output is stored in `verification_output.txt`.

The script separately constructs the reachable digit-carry machine and minimizes its output states for shifts from 0 through 4,095; evaluates the automaton output against direct binary-popcount parity for 98,208 inputs; checks all 4,088 dyadic-block shifts for block exponents 3 through 11; and repeats state-count checks on 300 fixed-seed random shifts below \(2^{100}\). The recorded output begins `VERIFY_OK`. No omitted network-dependent package, external certificate, or third-party full paper is needed to replay these checks.

No finite enumeration is used to prove the general theorem. This verification neither establishes publication priority nor constitutes an independent mathematical audit.
