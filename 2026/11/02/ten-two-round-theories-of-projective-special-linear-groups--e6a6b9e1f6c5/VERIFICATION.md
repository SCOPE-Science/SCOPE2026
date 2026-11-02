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
The accompanying verifier enumerates actual finite group elements, checks all ordered pair atomic diagrams in the named-identity ternary multiplication language, and compares the resulting exact sets of rooted one-round types. Run `python3 verify.py` alongside `verify.cpp` using Python 3 and a C++17 compiler. `verification_output.txt` records the successful invocation for seventeen specified fields, with `VERIFY_OK` on the final line.

The small-field check is deliberately supplementary. In particular, it does not establish the infinitely quantified field-order theorem, the sharp bound for the smallest representative of the final class, or the classification of field sizes not enumerated. Those assertions require the proof's standard finite-field torus facts and the two-round game lemma. Independent mathematical audit has not been performed.
