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

The universal proof is written in `RESULT.md`. The supplied `verify.py` independently constructs the relevant finite prime lists, computes the primorial cutoff, and obtains minimum products by a reverse-sum dynamic program over distinct primes. It verifies the stated radius at products \(2\), \(3\), and \(285\), and checks eligible isolated primes through \(4000\) for four base sets.

Run `python3 verify.py`; the expected final line is `VERIFY_OK`. Such finite evidence is not a substitute for the proof and does not address the existence of isolated primes for arbitrary widths. Independent audit has not been performed.
