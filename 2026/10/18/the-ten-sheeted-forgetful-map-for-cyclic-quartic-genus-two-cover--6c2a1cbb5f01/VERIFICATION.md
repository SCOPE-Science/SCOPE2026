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

# Reproduction and scientific limits

Run `python3 verify.py` with an ordinary Python 3 interpreter; no external library is needed. The checker uses exact arithmetic in the characteristic-two polynomial ring with two indeterminates, in a prime-power field with 256 elements, and in the one-variable characteristic-two polynomial ring. Expected final line: `VERIFY_OK`.

The checker tests the identity transforming the Witt presentation into its quintic Artin–Schreier equation; it then enumerates all 255 nonzero parameters of the chosen finite field, recomputes the proposed invariant two ways, tests every same-invariant scaling in that field when the cubic coefficients are nonzero, and checks the degree and formal derivative of the rational map exactly. The assertions are executed by the checker; an execution log is not itself a certificate.

The proof for arbitrary algebraically closed fields depends on hyperelliptic-coordinate rigidity, comparisons of leading odd coefficients, the solvability of a degree-sixteen translation equation, and the separable-fiber argument, which are written explicitly in `RESULT.md`. The finite tests are corroboration rather than an infinite-field proof. Originality, broader implications, and fields-of-definition descent are not settled by the checker.
