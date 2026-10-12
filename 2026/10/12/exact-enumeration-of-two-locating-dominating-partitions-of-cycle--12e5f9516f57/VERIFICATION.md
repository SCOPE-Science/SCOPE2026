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
# Verification

Run `python3 verify.py` from the directory containing the embedded verifier. The file `verification_output.txt` records the exact expected stdout; the verifier requires only the Python 3 standard library.

The verifier independently checks all labeled binary assignments for \(4\le n\le16\) (131,056 words), determines locating domination directly from open-neighborhood set signatures, compares the forbidden-word characterization for \(5\le n\le16\), and computes the trace of even powers of the weighted run automaton through degree 40. Rational coefficient recurrence and independent run counts agree at every order from 5 through 40. The two extraneous formal transfer terms at orders two and four are explicitly checked.

The identity for infinitely many cycle orders is established in the written proof and is not asserted on the basis of bounded enumeration. Independent audit status: not performed.
