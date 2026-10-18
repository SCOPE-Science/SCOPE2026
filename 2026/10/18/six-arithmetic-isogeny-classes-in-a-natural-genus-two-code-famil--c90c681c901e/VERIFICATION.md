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

The characteristic-19 automorphisms, the quotient fixed fields and the splitting of the two differential invariant lines are proved in `RESULT.md`; they are not inferred from finite enumeration. The quartic elliptic quotient has two rational points at infinity. Every one of the fifteen rational-character sums in `VERIFY.py` exhaustively evaluates all nineteen base-field elements.

Run `python3 VERIFY.py` with Python 3 and no external dependencies. `COUNT_CERTIFICATE.txt` contains actual output. It asserts the exact admissible parameter set, the six-class trace dictionary, and independently counts the genus-two curves over the base and quadratic extension fields. Quadratic-extension field multiplication is explicit and the quadratic character is computed from the norm. This checks the first two Frobenius-power traces for all fifteen curves, independently of the elliptic quotient sums.

Exact tested domain: all fifteen admissible parameters in \(\mathbb F_{19}\). Unproved outside that domain: classification for other base fields, full polarized isomorphism classes, and automorphism-equivalence of coding constructions. The complete zeta assertion follows algebraically from the elliptic-quotient isogeny, not by assuming agreement in only two extension degrees.
