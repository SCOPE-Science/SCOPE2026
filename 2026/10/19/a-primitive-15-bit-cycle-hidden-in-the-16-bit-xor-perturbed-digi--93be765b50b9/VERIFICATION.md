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

# Reproducible checks

Run `python3 verify_tent.py` in the directory containing this file. Python 3 standard library suffices.

The program compares two independent expressions for the state update on all 65,536 possible 16-bit inputs, checks the exact parity hyperplane as the image, and confirms all 32,768 periodic and all 32,768 strictly one-step transient states. Exact finite-field arithmetic verifies the irreducibility gcds and the nonunit primitive-order residues of the degree-15 polynomial `0xBFFF`. It traverses all 32,767 nonzero periodic states and confirms a single cycle; the zero cycle has two states in its full basin after including its external predecessor.

The analytic proof in `RESULT.md` establishes the general word-length image/kernel assertions and the characteristic polynomial. The exhaustive numerical check is limited to 16 bits; it is not a proof of any claim about other word lengths. An external independent mathematical review has not been performed.
