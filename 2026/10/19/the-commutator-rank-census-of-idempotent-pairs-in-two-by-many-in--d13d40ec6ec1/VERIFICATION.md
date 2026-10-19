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

# Mathematical verification

The stand-alone `verify_commutator.py` enumerates all two-bit diagonal choices and all permitted edge coefficients for every idempotent, then directly computes the commutator block and its ordinary matrix rank, independently of the line-sum proof. It checks \((q,m)=(2,1),(2,2),(2,3),(3,1),(3,2)\) and confirms \((196,128,0)\), \((2404,3648,672)\), \((29524,78608,34752)\), \((400,624,0)\), and \((10048,42912,21024)\), respectively.

Run `python verify_commutator.py` from the extracted files; a successful replay prints `VERIFY_COMMUTATOR_OK`. This is exhaustive for the named small prime fields only. The formula for all prime powers follows from the independent, characteristic-free Hamming-distance proof in `RESULT.md`. No computer certificate is asserted for infinitely many fields; no external independent review has been performed.
