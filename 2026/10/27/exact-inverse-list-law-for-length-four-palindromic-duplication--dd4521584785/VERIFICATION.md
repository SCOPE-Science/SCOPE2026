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

# Verification notes

The theorem has a complete analytic argument in `RESULT.md`. A separate executable checker `verify_pal4.py` uses direct received-word enumeration to compute distinct parent strings, rather than the proof's start-separation formula.

Run: `python3 verify_pal4.py`

Executed checks: symbolic overlapping-palindrome constraints at start separations one and two; exhaustive scans over all binary outputs through source length fourteen, ternary outputs through source length eight, quaternary outputs through source length six, and five-letter outputs through source length five (5,037,919 received words in total); construction checks for every length from four through three hundred, with two ordered choices of distinct construction letters per length.

The stored output `verify_pal4.out` ends with `VERIFY_OK`. These finite experiments establish the implementation's tested cases only. The all-length and all-alphabet assertions instead follow from the local-collision lemma and the explicit periodic construction.

Independent audit has not been performed.
