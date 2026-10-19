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

# Reproduction and limits

Place the four embedded source files `verify_fast.cpp`, `verify_independent.cpp`, `verify_family.py`, and `verify.py` together. Run `python3 verify.py`; this requires Python 3 and `g++` with C++17 support. The script rebuilds both enumeration engines from these exact sources, verifies all canonical words using at least three letters for lengths three through twelve, and requires zero merge-resistant strings before twelve and precisely the displayed word at twelve. It uses integer arithmetic, scaling the exponents by the least common multiple of possible periods. Both engines report the independent per-length counts given in the proof.

`verify_family.py` directly checks the complete run triples and exact rational exponent sums for all four words for suffix lengths two through nine, plus supplementary tests for ten, twelve, twenty, and forty. The proof's uniform-tail lemma—not the longer tests—establishes the family statement for arbitrarily long suffixes.

Checks actually executed from the included source files: both C++ engines matched all ten counts, including 4,211,549 canonical cases and exactly one witness at length twelve; the family checker returned `FAMILY_VERIFY_OK`, and the orchestration script returned `VERIFY_OK`.

These are ordinary reproducible calculations paired with a mathematical proof. There has been no independently commissioned scientific audit, and the checks do not establish the global extremal values of the unrestricted or binary run-exponent sum.
