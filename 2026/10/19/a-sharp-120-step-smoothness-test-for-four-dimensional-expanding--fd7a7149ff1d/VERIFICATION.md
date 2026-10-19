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

# Finite verification and analytical limits

Run `python3 verify.py` from the directory containing this document with Python 3.8 or newer, without third-party packages. The script executes 46 exact assertions: every proposed degree-four witness has the advertised least integer-spectrum power, each index divides 120, the selected fourth-root modular identities hold, the degree-2/4/6/8 Euler-totient preimage lists up to order 200 agree with those appearing in the proof, and the nine indices have least common multiple 120. The script is not an exhaustive infinite enumeration of algebraic integers. Completeness of the index classification rests on the irreducible-factor, norm, reciprocity and cyclotomic arguments in `RESULT.md`; the Markov partition step uses the cited theorem.

Scientific priority was assessed through the accessible originating paper and relevant literature/database comparisons; no independent audit has been performed.
