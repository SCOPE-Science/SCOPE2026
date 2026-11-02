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

# Reproduction and verification

Run `python3 verify.py` with Python 3 using only the standard library. The script constructs all 16 motifs of the form \(ab\overline a\overline b\), verifies the explicit length-26 cyclic cover, constructs the four size-four permutation orbits, checks every length-one and length-two motif overlap, and executes a Held–Karp minimum-cost cycle computation on the sixteen target vertices. The returned minimum is 26 and the run ends with `VERIFY_OK`.

The mathematical proof in `RESULT.md` supplies the general lower bound for all possible cyclic covering words; the finite dynamic program is an independent exhaustive check for this exact alphabet and target set. Nothing in these tests establishes a larger-alphabet or longer-motif theorem. No external independent audit has been performed.
