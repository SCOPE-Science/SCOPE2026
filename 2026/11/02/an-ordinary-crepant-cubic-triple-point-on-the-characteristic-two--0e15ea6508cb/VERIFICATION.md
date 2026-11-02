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

# Reproducible mathematical checks

Run `python nieto_char2_verify.py` with SymPy installed. The packaged execution output is `nieto_char2_verifier_output.txt`; it finishes with `VERIFY_OK`.

The verifier uses exact symbolic coefficient reductions modulo two, checks the two independent descriptions of the local degree-three and degree-five forms, checks all four gradient squares, enumerates all projective points and all 357 projective lines over the four-element field, and exhaustively counts rational points and singular points of the quintic over the two-element field. It does not infer geometric smoothness, geometric irreducibility, singular locus completeness, or crepancy from finite-field enumeration. These follow from the explicit algebraic proof in `RESULT.md`.

The Fano-line enumeration finds exactly 27 lines over the four-element field, with 15 fixed by Frobenius and 12 arranged into six length-two orbits. The characteristic-two Segre cubic and Barth–Nieto quintic have the same cubic `Q3` only in the stated quotient/tangent-cone sense, not as entire identical varieties.

Scientific limits: the singular-locus statement is set-theoretic; the blowup is local near the isolated point; historical priority remains subject to further full-text checking of some older papers.
